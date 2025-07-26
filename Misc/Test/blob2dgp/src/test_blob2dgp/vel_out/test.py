import pathlib
import sys
import numpy as np
from xbout import open_boutdataset
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
from tqdm import tqdm
import xarray as xr

import v_data


BOUT_res, BOUT_settings = v_data.data_import(folder = "delta_1")[0:2]

ds = open_boutdataset(BOUT_res, inputfilepath = BOUT_settings, info=False)
ds = ds.squeeze(drop=True)

dx = ds["dx"].isel(x=0).values
ds = ds.drop_vars("x")
ds = ds.assign_coords(x=np.arange(ds.sizes["x"])*dx)
param_var = ["B0", "Te0", "n0", "R_c"]
params = {}
param_val = np.empty((0, 4))
param_val = np.array([[ds.attrs["options"]["model"][var]] for var in param_var]).transpose()
[params.update({f"{var}": ds.attrs["options"]["model"][var]}) for var in param_var]
a = np.array([[1], [2], [3], [4]]).transpose()
param_val = np.append(param_val, a, axis = 0)

data_path = v_data.data_import("")[3]
data_input_path = data_path.joinpath("Input", f"campaign_{1}")
print(len(list(data_input_path.glob("*/"))))