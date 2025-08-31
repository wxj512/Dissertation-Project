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
from natsort import natsorted
import pandas as pd

import v_data


data_path = v_data.data_import("")[3]
campaign = 0
data_input_path = data_path.joinpath("Output", "vel_max_avg", f"campaign_{campaign}")
vmax_df = pd.read_csv(data_input_path.joinpath("v_max.csv"), index_col=0)
vavg_df = pd.read_csv(data_input_path.joinpath("v_avg.csv"), index_col=0)

vmax_B0 = vmax_df[vmax_df["Te0"] == 5.0][vmax_df["L_par"] == 10.0][vmax_df["R_c"] == 1.5]
vmax_Te0 = vmax_df[vmax_df["B0"] == 0.35][vmax_df["L_par"] == 10.0][vmax_df["R_c"] == 1.5]
vmax_L_par = vmax_df[vmax_df["Te0"] == 5.0][vmax_df["B0"] == 0.35][vmax_df["R_c"] == 1.5]
vmax_R_c = vmax_df[vmax_df["Te0"] == 5.0][vmax_df["L_par"] == 10.0][vmax_df["B0"] == 0.35]

vavg_B0 = vavg_df[vavg_df["Te0"] == 5.0][vavg_df["L_par"] == 10.0][vavg_df["R_c"] == 1.5]
vavg_Te0 = vavg_df[vavg_df["B0"] == 0.35][vavg_df["L_par"] == 10.0][vavg_df["R_c"] == 1.5]
vavg_L_par = vavg_df[vavg_df["Te0"] == 5.0][vavg_df["B0"] == 0.35][vavg_df["R_c"] == 1.5]
vavg_R_c = vavg_df[vavg_df["Te0"] == 5.0][vavg_df["L_par"] == 10.0][vavg_df["B0"] == 0.35]
# print(vmax_R_c)

var = "R_c"
var_label = r"$R_{c}$"
var_units = "/m"
vmax_dataset = vmax_R_c
vavg_dataset = vavg_R_c
f1 = plt.figure(1, linewidth = 3, edgecolor = "#000000")
ax1 = f1.gca()
ax1.set_title(r"$v_{max}$" + " vs " + var_label)
box1 = ax1.get_position()
ax1.set_position([box1.x0, box1.y0, box1.width * 0.8, box1.height])
ax1.plot(vmax_dataset[var], vmax_dataset["CoM"], label = "CoM")
ax1.plot(vmax_dataset[var], vmax_dataset["n_front_all"], label = "n front\nall rows")
ax1.plot(vmax_dataset[var], vmax_dataset["FWHM_all"], label = "n front + FWHM\nall rows")
ax1.set_xlim(0, 1.05 * np.max((vmax_dataset[var])))
ax1.set_ylim(0, 1.1 * np.max((vmax_R_c[["CoM", "n_front_all", "FWHM_all"]])))
ax1.set_ylabel(r"$v_{max}/c_s$")
ax1.set_xlabel(var_label + var_units)
f1.legend(bbox_to_anchor = (0.98, 0.97), fontsize = "small")

f2 = plt.figure(2, linewidth = 3, edgecolor = "#000000")
ax2 = f2.gca()
ax2.set_title(r"$v_{avg}$" + " vs " + var_label)
box2 = ax2.get_position()
ax2.set_position([box2.x0, box2.y0, box2.width * 0.8, box2.height])
ax2.plot(vavg_dataset[var], vavg_dataset["CoM"], label = "CoM")
ax2.plot(vavg_dataset[var], vavg_dataset["n_front_all"], label = "n front\nall rows")
ax2.plot(vavg_dataset[var], vavg_dataset["FWHM_all"], label = "n front + FWHM\nall rows")
ax2.set_xlim(0, 1.05 * np.max(vavg_dataset[var]))
ax2.set_ylim(0, 1.1 * np.max(vavg_R_c[["CoM", "n_front_all", "FWHM_all"]]))
ax2.set_ylabel(r"$v_{avg}/c_s$")
ax2.set_xlabel(var_label + var_units)
f2.legend(bbox_to_anchor = (0.98, 0.97), fontsize = "small")
plt.show()

