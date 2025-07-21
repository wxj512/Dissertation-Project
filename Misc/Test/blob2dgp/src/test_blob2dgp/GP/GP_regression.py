import numpy as np
import xarray as xr
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel
import matplotlib.pyplot as plt

import test_blob2dgp.vel_out.v_data as v_data

def gp_reg(x_train, y_train, x_arr, restarts = 9, len_scale = 1e-2):
    kernel_CoM = 1 * RBF(length_scale = len_scale, length_scale_bounds = (1e-2, 1e3)) + WhiteKernel(
        noise_level = 1e-4, noise_level_bounds = (1e-10, 1e-1))
    GP_CoM = GaussianProcessRegressor(kernel = kernel_CoM, alpha = 0.0, n_restarts_optimizer = restarts)
    GP_CoM.fit(x_train, y_train)
    mean_prediction, stdev_prediction = GP_CoM.predict(x_arr, return_std=True)
    return mean_prediction, stdev_prediction

def gp_plot(ds_x, ds_y, x_train, y_train, mean_prediction, stdev_prediction, n_method, fig_no, vel_type = "max"):
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
    data_input_path = data_path.joinpath("Output", "vel_max_avg", "B0_0.1_1.0")
    vall_ds = xr.open_dataset(data_input_path.joinpath("v_all.nc"))
    
    # v_max plots
    for i, n_method in enumerate(vall_ds["n_method"].values):
        ds_x = vall_ds["B0"].values.reshape(-1, 1)
        ds_y = vall_ds["v_max"].sel(n_method = n_method).values.reshape(-1, 1)
        # ds_y = vall_ds["v_avg"].sel(n_method = n_method).values.reshape(-1, 1)

        # Random sampling from dataset
        rng = np.random.RandomState(1)
        training_indices = rng.choice(np.arange(ds_y.size), size = int(0.7 * ds_y.size), replace = False)
        x_train, y_train = ds_x[training_indices], ds_y[training_indices]

        mean_prediction, stdev_prediction = gp_reg(x_train, y_train, ds_x)

        gp_plot(ds_x, ds_y, x_train, y_train, mean_prediction, stdev_prediction, n_method, fig_no = i, vel_type = "max")
        

    plt.show()

if __name__  == "__main__":
    main()