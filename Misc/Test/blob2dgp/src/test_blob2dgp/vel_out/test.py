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

BOUT_res, BOUT_settings = v_data.data_import(folder="delta_1_B0_0.1")[0:2]

ds = open_boutdataset(BOUT_res, inputfilepath=BOUT_settings, info=False)
ds = ds.squeeze(drop=True)

dx = ds["dx"].isel(x=0).values
ds = ds.drop_vars("x")
ds = ds.assign_coords(x=np.arange(ds.sizes["x"])*dx)

t = 44

ds_data = ds.isel(t=t)

n_point = v_data.n_calc_methods(ds_data, row_calc="all_row", n0_scale=1, Gridsize=0.3).n_front(FWHM=True)

print(n_point)

n = ds_data["n"][:,int(n_point[1]/0.3)] - 1

plt.plot(n)
plt.show()