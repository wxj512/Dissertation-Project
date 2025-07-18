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

n_point = v_data.n_calc_methods(ds_data, row_calc = "all_row", n0_scale = 1, Gridsize = 0.3, method = "n_front_FWHM")
n_point_nf = v_data.n_calc_methods(ds_data, row_calc = "all_row", n0_scale = 1, Gridsize = 0.3, method = "n_front")



n = ds_data["n"][:,int(n_point_nf[1]/0.3)] - 1
print(n_point_nf)
print(n_point)
f1 = plt.figure(1, linewidth = 3, edgecolor = "#000000")
ax1 = f1.gca()
ax1.plot(ds["x"].values,n, label = "Density profile", linewidth = 1)
ax1.set_title(r"z/$\rho_s$ = " + f" {n_point_nf[1]:.1f}, " r"t/(1/$\Omega_i$) = " + f"{t*500}")
# ax1.vlines(n_point_nf[0], np.min(n) * 1.1, np.max(n) * 1.1, linestyle = "--")
ax1.vlines(n_point[0], np.min(n) * 1.2, np.max(n) * 1.2, linestyle = "--", color = "orange", linewidth = 1, 
           label = "Peak position\nfrom n front method")
ax1.set_xlim(0, ds["x"].values.max() * 1.003)
ax1.set_ylim(np.min(n) * 1.2, np.max(n) * 1.2)
ax1.set_xlabel(r"x/$\rho_s$")
ax1.set_ylabel(r"Density/(n/$n_0$)")
ax1.legend(fontsize = "small")

f2 = plt.figure(2)
ds_data["n"].plot(x="x", y="z")
plt.show()