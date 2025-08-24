import os
import pandas as pd
import xarray as xr
import numpy as np
from scipy.stats import sobol_indices, uniform
from SALib import ProblemSpec
import matplotlib.pyplot as plt

import test_blob2dgp.vel_out.v_data as v_data
import test_blob2dgp.GP.GP_regression as gpr

class sb_func:
    def __init__(self, gprfunc):
        self.gprfunc = gprfunc

    def v_func(self, x):
        # x = np.transpose(x)
        gpfunc = self.gprfunc
        y_mean = gpfunc.predict(x).transpose()
        return y_mean
    

data_path = v_data.data_import("")[3]
campaign = 3
data_input_path = data_path.joinpath("Output", "vel_max_avg", f"campaign_{campaign}")
vmax_df = pd.read_csv(data_input_path.joinpath("v_max.csv"), index_col=0)
avg_df = pd.read_csv(data_input_path.joinpath("v_avg.csv"), index_col=0)
vmax_data = vmax_df[["CoM", "n_front_all", "FWHM_all"]]
param_val = vmax_df[["B0", "Te0", "L_par", "R_c"]]
Z = vmax_data["CoM"].values.reshape(-1,1)
X = param_val.values

gprfunc, x_train, x_test, y_train, y_test = gpr.gp_reg(X, Z, len_scale_bnds = ((1e-10, 1e5),) * 4, noise_bnds = (1e-10, 1e5), restarts = 49,
                                return_data = True)
print(gprfunc.score(x_test, y_test))
v_func = sb_func(gprfunc).v_func
sb_bnds = [np.array([np.min(param_val[dim]), np.max(param_val[dim])]) for dim in param_val.columns]
# print(Z)

sp = ProblemSpec({
    "names": list(param_val.columns.values),
    "groups": None,
    "bounds": np.array(sb_bnds),
    "outputs": ["Y"],
})

sp.sample_sobol(1024, calc_second_order=True)
sp.evaluate(v_func)
sp.analyze_sobol(calc_second_order=True)

y = sp.analysis
samples_col = ["vmax_CoM", "B0", "Te0", "L_par", "R_c"]
res = np.concatenate((sp.results.reshape(-1,1),sp.samples), axis=1)
samples_df = pd.DataFrame(res, columns=samples_col)
sb_col = ["S1", "S1_conf", "ST", "ST_conf", "S2_B0", "S2_Te0", "S2_L_par", "S2_R_c", "S2_B0_conf", "S2_Te0_conf", "S2_L_par_conf", "S2_R_c_conf"]
sb_index = ["B0", "Te0", "L_par", "R_c"]
sb_res = np.empty((y["S1"].size,0))
sb_res = np.column_stack(list(y.values()))
sb_df = pd.DataFrame(sb_res, columns = sb_col, index = sb_index)

data_output_path = data_input_path.parents[1].joinpath("sobol_ind", f"campaign_{campaign}")
if not(os.path.exists(data_output_path) and os.path.isdir(data_output_path)):
            os.mkdir(data_output_path)
# samples_df.to_csv(data_output_path.joinpath("samples.csv"))
# sb_df.to_csv(data_output_path.joinpath("sobol_ind.csv"))
print(sb_df)
# print(data_output_path)

# params = [r"$B_0$"f"\n"r"($B_0, T_{e,0}$)", r"$T_{e,0}$"f"\n"r"($T_{e,0}, R_c$)", r"$R_c$"f"\n"r"($R_c, B_0$)"]
# x = np.arange(len(params))
# width = 0.2
# multiplier = 0

# pos = [0,2,1]
# S2 = y["S2"]
# S2 = S2[~np.isnan(S2)]
# S2 = S2[pos]
# S2err = y["S2_conf"]
# S2err = S2err[~np.isnan(S2err)]
# S2err = S2err[pos]

# sb_dict = {
#     "First Order": y["S1"],
#     "Second Order": S2,
#     "Total Order": y["ST"]
# }
# sb_err = {
#     "First Order": y["S1_conf"],
#     "Second Order": S2err,
#     "Total Order": y["ST_conf"]
# }



# f1 = plt.figure(1, linewidth = 3, edgecolor = "#000000")
# ax1 = f1.gca()
# box = ax1.get_position()
# ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])
# ax1.set_title(r"Sobol indicies for $v_{max}$")
# for order, index in sb_dict.items():
#     offset = width * multiplier
#     # err = [index - sb_err[order][0], sb_err[order][1] - index]
#     if order == "Second Order":
#         lowers = np.minimum(sb_err[order],index)
#         rects = ax1.bar(x + offset, index, width, label = order, yerr = [lowers, sb_err[order]], capsize = 3)
#     else:
#         rects = ax1.bar(x + offset, index, width, label = order, yerr = sb_err[order], capsize = 3)
#     # ax1.bar_label(rects, padding=0.5)
#     multiplier += 1
# # ax1.set_xlim(0, 0.4)
# ax1.set_xticks(x + (width), params)
# ax1.set_xlabel("Parameters")
# ax1.set_ylabel("Sobol Index Value")
# ax1.set_ylim(0,1)
# ax1.set_yticks(np.arange(0, 1.1, 0.1))
# f1.legend(bbox_to_anchor = (0.97, 0.9), fontsize = "small")

f1 = sp.plot()

plt.show()

