import os
# from sklearn.gaussian_process import GaussianProcessRegressor
# from sklearn.gaussian_process.kernels import RBF
import numpy as np
from xbout import open_boutdataset

import test_blob2dgp.vel_out.v_data as v_data


# X = np.linspace(start=0, stop=10, num=1_000).reshape(-1, 1)
# y = np.squeeze(X * np.sin(X))



def main(): 
    data_path = v_data.data_import("")[3]

#     for file_i, [subdir, dirs, files] in enumerate(os.walk(data_path)):
#         if "B0" in subdir:
#             BOUT_res, BOUT_settings = v_data.data_import(folder=subdir)[0:2]
#             ds = open_boutdataset(BOUT_res, info=False)
#             ds = ds.squeeze(drop=True)

#             dx = ds["dx"].isel(x=0).values
#             ds = ds.drop_vars("x")
#             ds = ds.assign_coords(x=np.arange(ds.sizes["x"])*dx)

#             n_array_CoM = v_data.n_calc(ds)
#             dx_CoM, dz_CoM, vx_CoM, vz_CoM = v_data.vel_calc(n_array_CoM)

#             max_v = np.array([np.max(vx_CoM)]).transpose()

#             try:
#                 max_v_array = np.append(max_v_array, max_v, axis = 0)
#             except: 
#                 max_v_array = max_v


# rng = np.random.RandomState(1)
# training_indices = rng.choice(np.arange(y.size), size=6, replace=False)
# X_train, y_train = X[training_indices], y[training_indices]


if __name__ == "__main__":
    main()
