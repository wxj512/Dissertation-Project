import pathlib
import numpy as np
import xarray as xr
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from inference.plotting import matrix_plot

import test_blob2dgp.vel_out.v_data as v_data


# X = np.linspace(start=0, stop=10, num=1_000).reshape(-1, 1)
# y = np.squeeze(X * np.sin(X))



def main(): 
    data_path = v_data.data_import("")[3]
    data_input_path = data_path.joinpath("Output", "vel_max_avg", "campaign_1")
    vall_ds = xr.open_dataset(data_input_path.joinpath("v_all.nc"))
    vmax_data = vall_ds["v_max"].sel(n_method = "CoM")
    
    



    ls = (1,) * 2
    bounds_l = ((1e-2,100.),) * 2
    kernel_CoM_1 = RBF(length_scale = ls, length_scale_bounds = bounds_l) + WhiteKernel(
        noise_level = 1e-3, noise_level_bounds = (1e-10, 100.))
    GP_CoM_1 = GaussianProcessRegressor(kernel = kernel_CoM_1, n_restarts_optimizer = 9)
    
    B0 = vall_ds["B0"].values
    Te0 = vall_ds["Te0"].values
    x2,x1 = np.meshgrid(Te0, B0)
    x1v = x1.reshape(-1,1)
    x2v = x2.reshape(-1,1)
    X = np.column_stack((x1v.reshape(-1), x2v.reshape(-1)))
    Z = np.empty(0)
    Z = [np.append(Z,vmax_data.sel(B0=i, Te0=j)) for i,j in X]
    Z = np.reshape(Z,(-1,1))
    X_train, X_test, Y_train, Y_test = train_test_split(X, Z, test_size=0.4)
    GP_CoM_1.fit(X_train, Y_train)
    print(GP_CoM_1.kernel_)
    print(GP_CoM_1.score(X,Z))
    Zfit, Zstd = GP_CoM_1.predict(X, return_std=True)
    Zfit = Zfit.reshape(10,10)
    Zstd = Zstd.reshape(10,10)

    
    f1 = plt.figure(1, linewidth = 3, edgecolor = "#000000")
    ax1 = f1.add_subplot(projection='3d')
    surf = vmax_data.plot.surface(x="B0", y="Te0", cmap="plasma", add_colorbar=False, alpha=0.6, linewidth=0.3, 
                                  label=r"$v_{max}$ for CoM method")
    ax1.plot_wireframe(x1,x2,Zfit, label = "Mean prediction")
    ax1.plot_surface(x1,x2,Zfit - 1.96 * Zstd, color="gray", alpha=0.2, label=f"95% confidence interval")
    ax1.plot_surface(x1,x2,Zfit + 1.96 * Zstd, color="gray", alpha=0.2)
    ax1.scatter(X_train[0,0], X_train[0,1], Y_train[0], color="black", marker="x", label="Observations")
    [ax1.scatter(val[0],val[1],val[2], color="black", marker="x") for i,val in enumerate(zip(X_train[:,0], X_train[:,1], Y_train)) if i > 0]
    # print(list(zip(X_train[:,0], X_train[:,1], Y_train))[0])
    f1.colorbar(surf, shrink=0.8, pad=0.2)
    ax1.axes.set_xlabel(r"$B_0/T$")
    ax1.axes.set_ylabel(r"$T_{e,0}/eV$")
    ax1.axes.set_zlabel(r"$v_{max}/c_s$")
    ax1.set_xlim(0,vmax_data["B0"].max())
    ax1.set_ylim(0,vmax_data["Te0"].max())
    ax1.set_zlim(0,vmax_data.max() * 1.1)
    f1.legend(bbox_to_anchor = (1, 1), fontsize = "small")
    # ax1.set_zlim(0,np.ceil(vmax_data.values.max()))


    
    # N = 20
    # x = np.linspace(1, N, N)
    
    # samples = GP_CoM_1.sample_y(X)
    # samples = samples.reshape(10,10, order="C")
    # print(samples)

    # s1, s2 = np.meshgrid(samples_1, samples_2)
    # print(s1, s2)
    # print(np.max(samples), np.min(samples))
    
    # samples_1 = GP_CoM_1.sample_y(x.reshape(-1,1), 20000).transpose()
    # # samples_1 = samples_1.reshape(-1,1)
    # # samples_2 = samples_2.reshape(-1,1)
    # # samples = np.column_stack([samples_1, samples_2]).transpose()
    # samples_1 = [samples_1[:, i] for i in range(N)]
    # samples_1 = [samples_1[:, i] for i in range(N)]
    
    # K = GP_CoM_1.kernel_(np.column_stack((np.unique(X[:,0]),np.unique(X[:,1]))))
    # D = GP_CoM_1.kernel_.diag(np.column_stack((np.unique(X[:,0]),np.unique(X[:,1]))))
    # f2 = plt.figure(2, linewidth = 3, edgecolor = "#000000")
    # ax2 = f2.gca()
    # pcplot = ax2.imshow(np.diag(D**-0.5).dot(K).dot(np.diag(D**-0.5)), cmap="plasma")
    
    # f2.colorbar(pcplot)
    # ax2.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
    # ax2.set_title("Dimensions",fontsize=10)
    # ax2.set_xlabel(r"$\ell_{RBF}$= " + f"{GP_CoM_1.kernel_.get_params()["k1__length_scale"][0]:.2f}, {GP_CoM_1.kernel_.get_params()["k1__length_scale"][1]:.2f}, " + r"${\lambda^2}_{WN}$= " + f"{GP_CoM_1.kernel_.get_params()["k2__noise_level"]:.2f}")
    # ax2.set_ylabel("Dimensions")
    # ax2.set_aspect('equal')
    # ax2.set_xticks([])
    # ax2.set_yticks([])

    plt.show()

if __name__ == "__main__":
    main()
