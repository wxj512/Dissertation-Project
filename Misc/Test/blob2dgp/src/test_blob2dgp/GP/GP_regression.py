import numpy as np
import xarray as xr
import pandas as pd
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel
from sklearn.model_selection import train_test_split, cross_val_score
import matplotlib.pyplot as plt

import test_blob2dgp.vel_out.v_data as v_data

def gp_reg(x_arr, y_arr, restarts = 9, len_scale = (1,), len_scale_bnds = ((1e-5, 1e5),),
            noise = 1e-2, noise_bnds = (1e-10, 1e5), return_GP = False, return_data = False):
    ## Requires x_arr and y_arr in vertical stack
    cols = np.shape(x_arr)[1]
    if cols > 1:
        if len_scale == (1,):
            len_scale = len_scale * cols
        if len_scale_bnds == ((1e-2, 1e5),):
            len_scale_bnds = len_scale_bnds * cols
    kernel = RBF(length_scale = len_scale, length_scale_bounds = len_scale_bnds) #+ WhiteKernel(
        # noise_level = noise, noise_level_bounds = noise_bnds)
    GP = GaussianProcessRegressor(kernel = kernel, n_restarts_optimizer = restarts)
    x_train, x_test, y_train, y_test = train_test_split(x_arr, y_arr, test_size = 0.4)
    GP.fit(x_train, y_train)
    if return_GP == True:
        return GP
    elif return_data == True:
        return GP, x_train, x_test, y_train, y_test
    mean_prediction, stdev_prediction = GP.predict(x_arr, return_std = True)
    score = GP.score(x_arr, y_arr)
    return mean_prediction, stdev_prediction, score, x_train, x_test, y_train, y_test

def gp_plot_1d(ds_x, ds_y, x_train, y_train, mean_prediction, stdev_prediction, n_method, fig_no, vel_type = "max"):
    fig_dict = {}
    fig_dict[f"{fig_no + 1}"] = plt.figure(fig_no + 1, linewidth = 3, edgecolor = "#000000")
    ax1 = fig_dict[f"{fig_no + 1}"].gca()
    ax1.set_title(r"Gaussian process on $v_{%s}$ of blob" % vel_type + f"\nusing {n_method} method")
    box = ax1.get_position()
    ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    ax1.plot(ds_x, ds_y, label = r"$v_{%s}$" % vel_type, linestyle="--")
    ax1.scatter(x_train, y_train, label="Observations", marker = "x")
    ax1.plot(ds_x, mean_prediction, label="Mean prediction")
    ax1.fill_between(
        ds_x.ravel(),
        mean_prediction - 1.96 * stdev_prediction,
        mean_prediction + 1.96 * stdev_prediction,
        alpha = 0.3,
        label = f"95% confidence \ninterval",
    )
    ax1.set_xlim(0, 1.1 * np.max(ds_x))
    ax1.set_ylim(0, 1.1 * np.max(ds_y))
    ax1.set_ylabel(r"$v_{%s}/c_s$" % vel_type)
    ax1.set_xlabel(r"$B_0/T$")
    fig_dict[f"{fig_no + 1}"].legend(bbox_to_anchor = (0.98, 0.97), fontsize = "small")

def main():
    data_path = v_data.data_import("")[3]
    campaign = 4        
    data_input_path = data_path.joinpath("Output", "vel_max_avg", f"campaign_{campaign}")
    vmax_df = pd.read_csv(data_input_path.joinpath("v_max.csv"))
    # vall_ds = xr.open_dataset(data_input_path.joinpath("v_all.nc"))
    # vmax_data = vall_ds["v_max"].sel(n_method = "FWHM_all")
    # B0 = vmax_data["B0"].values.reshape(-1,1)
    # vmax = vmax_data.values.reshape(-1,1)
    
    param_var = list(("B0", "Te0", "L_par","R_c"))
    params = vmax_df[param_var].values
    vmax_CoM = vmax_df["CoM"].values.reshape(-1,1)
    

    GP, x_train, x_test, y_train, y_test = gp_reg(params, vmax_CoM, len_scale_bnds = ((1e-10, 1e10),) * len(param_var),
                                                   noise_bnds = (1e-10, 1e10), restarts = 49, return_data=True)
    cv_score = cross_val_score(GP, x_train, y_train, cv=5)
    print(cv_score, cv_score.mean())
    print(GP.score(x_test, y_test))

    # gp_plot_1d(B0, vmax, x_train, y_train, mean_prediction, stdev_prediction, "n front + FWHM", 0, vel_type = "max")

    # Z = np.empty(0)
    # Z = [np.append(Z,vmax_data.sel(B0=i, Te0=j)) for i,j in X]
    # Z = np.reshape(Z,(-1,1))
    # GP, x_train, x_test, y_train, y_test = gp_reg(params, vmax_CoM, len_scale_bnds = ((1e-20, 1e40),) * 4, noise_bnds = (1e-10, 1e10), restarts = 499,
    #                              return_data = True)
    # score = cross_val_score(GP, x_train, y_train, scoring = "r2")
    # r2 = GP.score(x_test, y_test)
    # print(score)
    # print(r2)
    # print(GP.kernel_.get_params()["k2__noise_level"])

    # gpfunc = gp_reg(X, Z, return_GP = True)
    # mean = gpfunc.predict(X)
    # print(X)
    # print(mean)    

    plt.show()

if __name__  == "__main__":
    main()