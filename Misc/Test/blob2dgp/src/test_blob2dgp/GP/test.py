import pathlib
import numpy as np
import xarray as xr
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
import matplotlib.pyplot as plt


import test_blob2dgp.vel_out.v_data as v_data


# X = np.linspace(start=0, stop=10, num=1_000).reshape(-1, 1)
# y = np.squeeze(X * np.sin(X))



def main(): 
    data_path = v_data.data_import("")[3]
    data_input_path = data_path.joinpath("Output", "vel_max_avg", "campaign_1")
    vall_ds = xr.open_dataset(data_input_path.joinpath("v_all.nc"))
    
    # ds_x = vall_ds["B0"].values.reshape(-1, 1)
    # ds_y = vall_ds["v_max"].values.reshape(-1, 1)

    # # Random sampling from dataset
    # rng = np.random.RandomState(1)
    # training_indices = rng.choice(np.arange(ds_y.size), size = int(0.6 * ds_y.size), replace = False)
    # x_train, y_train = ds_x[training_indices], ds_y[training_indices]

    vall_data = vall_ds.sel(Te0 = 40, method="nearest")
    vall_data["v_avg"].plot(x="B0")
    plt.show()
    # print(vall_ds["Te0"])
    
if __name__ == "__main__":
    main()
