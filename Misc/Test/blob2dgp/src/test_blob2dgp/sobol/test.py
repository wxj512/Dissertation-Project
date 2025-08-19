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
data_input_path = data_path.joinpath("Output", "vel_max_avg", "campaign_2")
vall_df = pd.read_csv(data_input_path.joinpath("v_max.csv"), index_col=0)
vall_df = pd.read_csv(data_input_path.joinpath("v_max.csv"), index_col=0)
vmax_data = vall_df[["CoM", "n_front_all", "FWHM_all"]]
param_val = vall_df[["B0", "Te0", "R_c"]]
Z = vmax_data["CoM"].values.reshape(-1,1)
X = param_val.values

gprfunc, x_train, x_test, y_train, y_test = gpr.gp_reg(X, Z, len_scale_bnds = ((1e-10, 1e5),) * 3, noise_bnds = (1e-10, 1e5), restarts = 19,
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

sp.sample_sobol(32768, calc_second_order=True)
sp.evaluate(v_func)
sp.analyze_sobol(print_to_console=True, calc_second_order=True)
sp.plot()
plt.show()