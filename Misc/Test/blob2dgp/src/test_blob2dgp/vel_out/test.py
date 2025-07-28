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
from operator import itemgetter

import v_data


BOUT_res, BOUT_settings = v_data.data_import(folder = "campaign_1/delta_1_B0_0.1_Te0_4.0")[0:2]

ds = open_boutdataset(BOUT_res, inputfilepath=BOUT_settings, info=False)
ds = ds.squeeze(drop=True)
dx = ds["dx"].isel(x=0).values
ds = ds.drop_vars("x")
ds = ds.assign_coords(x=np.arange(ds.sizes["x"])*dx)
t = 47
ds_data = ds.isel(t=t)

front, row, gauss_fit = v_data.n_calc_methods(ds_data, "all_row", 1, 0.3, "n_front_FWHM")
nf_front, row_j = v_data.n_calc_methods(ds_data, "all_row", 1, 0.3, "n_front")

n = ds_data["n"].values[:,row]-1

f1 = plt.figure(1, linewidth = 3, edgecolor = "#000000")
ax1 = f1.gca()
ax1.set_title("z/$\\rho_s$ = " + str(np.round(ds["z"].values[row_j],1)) + ", t/(1/$\\Omega_i$) = " + str(t*500))
ax1.plot(ds_data["x"], n,linewidth=0.8, label="Density profile")
ax1.plot(ds_data["x"], gauss_fit, linewidth=0.8, linestyle = "-.", label="Gaussian fit of last peak")
ax1.scatter(nf_front[0],n[int(np.where(ds_data["x"]==nf_front[0])[0][0])],marker="x", color="orange", label="Peak position")
ax1.vlines(front[0], np.min(n)-0.05, np.max(n)+0.1, linestyle = "--", linewidth=0.5, color="black", label = "Position of \nright side of FWHM")
ax1.set_ylim(np.min(n)-0.05, np.max(n)+0.1)
ax1.set_xlabel("x/$\\rho_s$")
ax1.set_ylabel("Density/(n/$n_0$)")
ax1.legend(fontsize="small")

plt.show()
