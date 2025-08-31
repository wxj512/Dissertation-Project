import xarray as xr
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
from scipy.stats import sobol_indices, uniform
import matplotlib.pyplot as plt

import test_blob2dgp.vel_out.v_data as v_data
import test_blob2dgp.GP.GP_regression as gpr

class sb_func:
    def __init__(self, gprfunc):
        ## Accepts gpr functions from scikit learn
        self.gprfunc = gprfunc

    def v_func(self, x):
        ## Transform x into column array
        x = np.transpose(x)
        y_mean = self.gprfunc.predict(x).transpose()
        return y_mean

def sobol(sb_func, bnds, n = 2**(14)):
    sb_ind = sobol_indices(
        func = sb_func,
        n = n,
        ## Requires bnds in the form of [array(x1 lb, x1 ub), array(x2 lb, x2 ub)...]
        dists = [uniform(loc = i[0], scale = i[1] - i[0]) for i in bnds],
        rng = np.random.default_rng()
    )
    return sb_ind

def main():
    data_path = v_data.data_import("")[3]
    data_input_path = data_path.joinpath("Output", "vel_max_avg", "campaign_1")
    vall_ds = xr.open_dataset(data_input_path.joinpath("v_all.nc"))
    vmax_data = vall_ds["v_max"].sel(n_method = "CoM")
    B0 = vall_ds["B0"].values
    Te0 = vall_ds["Te0"].values
    x2,x1 = np.meshgrid(Te0, B0)
    x1v = x1.reshape(-1,1)
    x2v = x2.reshape(-1,1)
    # vall_df = pd.read_csv(data_input_path.joinpath("v_max.csv"), index_col=0)
    # vmax_data = vall_df[["CoM", "n_front_all", "FWHM_all"]]
    # param_val = vall_df[["B0", "Te0", "R_c"]]
    X = np.column_stack((x1v.reshape(-1), x2v.reshape(-1)))
    Z = [vmax_data.sel(B0=i, Te0=j) for i,j in X]
    Z = np.reshape(Z,(-1,1))
    # Z = vmax_data["CoM"].values.reshape(-1,1)
    # X = param_val.values

    gprfunc, x_train, x_test, y_train, y_test = gpr.gp_reg(X, Z, len_scale_bnds = ((1e-10, 1e5),) * 2, noise_bnds = (1e-10, 1e5), restarts = 9,
                                 return_data = True)
    cv_score = cross_val_score(gprfunc, x_train, y_train, cv=5)
    print(cv_score, cv_score.mean())
    print(gprfunc.score(x_test, y_test))
    v_func = sb_func(gprfunc).v_func
    # sb_bnds = [np.array([np.min(vall_ds[dim]), np.max(vall_ds[dim])]) for dim in vall_ds]
    # gprfunc = gpr.gp_reg(X, Z, return_GP=True)
    # v_func = sb_func(gprfunc).v_func
    sb_bnds = [np.array([np.min(vall_ds[dim]), np.max(vall_ds[dim])]) for dim in vall_ds.coords if dim != "n_method"]
    sb_ind = sobol(v_func, sb_bnds)
    # print(sb_ind.first_order)
    # print(sb_ind.total_order)
    sb_boot = sb_ind.bootstrap()
    # print(sb_boot.total_order.confidence_interval.low, sb_boot.total_order.confidence_interval.high)

    params = [r"$B_0$", r"$T_{e,0}$"]
    sb_dict = {
        "First Order": sb_ind.first_order,
        "Total Order": sb_ind.total_order
    }
    sb_err = {
        "First Order": [sb_boot.first_order.confidence_interval.low, sb_boot.first_order.confidence_interval.high],
        "Total Order": [sb_boot.total_order.confidence_interval.low, sb_boot.total_order.confidence_interval.high]
    }

    print(sb_err["First Order"][0])
    x = np.arange(len(params))
    width = 0.1
    multiplier = 0
    print(sb_err.items())
    
    f1 = plt.figure(1, linewidth = 3, edgecolor = "#000000")
    ax1 = f1.gca()
    box = ax1.get_position()
    ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    ax1.set_title(r"Sobol indicies for $v_{max}$")
    for order, index in sb_dict.items():
        offset = width * multiplier
        err = [index - sb_err[order][0], sb_err[order][1] - index]
        rects = ax1.bar(x + offset, index, width, label = order, yerr = err, capsize = 3)
        # ax1.bar_label(rects, padding=0.5)
        multiplier += 1
    # ax1.set_xlim(0, 0.4)
    ax1.set_xticks(x + (width/2), params)
    ax1.set_ylim(0, 1)
    ax1.set_xlabel("Parameters")
    ax1.set_ylabel("Sobol Index Value")
    f1.legend(bbox_to_anchor = (0.97, 0.9), fontsize = "small")
    
    
    plt.show()

if __name__ == "__main__":
    main()