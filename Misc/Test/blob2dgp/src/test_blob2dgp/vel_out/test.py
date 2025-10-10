import pathlib
import sys
import numpy as np
from xbout.plotting import animate
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


BOUT_res, BOUT_settings = v_data.data_import(folder = "delta_1/")[0:2]

ds = open_boutdataset(BOUT_res, inputfilepath=BOUT_settings, info=False)
ds = ds.squeeze(drop=True)

dx = ds["dx"].isel(x=0).values
ds = ds.drop_vars("x")
ds = ds.assign_coords(x=np.arange(ds.sizes["x"])*dx)


anim = ds["n"].bout.animate2D(aspect="equal", animate_over="t", x="x", y="z", fps=20, controls=None, save_as="n_anim")
# anim.ax.set_title("Test")


plt.show()

