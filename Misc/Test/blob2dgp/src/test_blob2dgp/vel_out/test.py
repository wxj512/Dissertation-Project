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

BOUT_res, BOUT_settings = v_data.data_import("")[0:2]

ds = open_boutdataset(BOUT_res, inputfilepath=BOUT_settings, info=False)
ds = ds.squeeze(drop=True)

dx = ds["dx"].isel(x=0).values
ds = ds.drop_vars("x")
ds = ds.assign_coords(x=np.arange(ds.sizes["x"])*dx)

t = 20

ds_data = ds.isel(t=t)
n_flat = np.ravel(ds_data["n"].values, order="F") - 1

peaks, peak_info = find_peaks(n_flat, height = 0.005)
col = ds_data["x"].size
row = ds_data["z"].size
peak1x = np.max(peaks % col)
peak1z = peaks[np.where((peaks%col) == peak1x)[0][0]] // col

peak2x = peaks[np.where((peaks%col) == peak1x)[0][0] - 1]%col

print(peak1x, peak1z)
print(peak2x)

for j,z_vals in enumerate(ds_data["z"].values):
                
    n = ds_data["n"].values[:,j] - 1

    #Find peaks of rows
    all_peak = find_peaks(n, height = 0.005)

    if not(all_peak[0].size > 0):
        max_peak = 0
        peak_2 = 0
    elif all_peak[0].size == 1:
        max_peak = np.max(all_peak[0])
        peak_2 = max_peak - (np.where(n > 0.0001 * n[max_peak])[0][-1] - max_peak)
    else:
        max_peak = np.max(all_peak[0])
        peak_2 = all_peak[0][-2]


    # Makes sure this condition is fullfilled at j = 0
    if j == 0:
        max_peak_j = 0
        peak_2_j = 0
    elif max_peak == 0:
        continue
    elif max_peak>max_peak_j:
        max_peak_j = max_peak
        row_j = j
        peak_2_j = peak_2
    else:
        continue

print(max_peak_j, row_j)
print(peak_2_j)

plt.plot(n_flat[33280:33540])
plt.plot(ds_data["n"].values[:, 128]-1)
plt.show()
