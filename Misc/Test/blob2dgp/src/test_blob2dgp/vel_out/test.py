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


BOUT_res, BOUT_settings = v_data.data_import(folder = "delta_1")[0:2]

ds = open_boutdataset(BOUT_res, inputfilepath = BOUT_settings, info = False)
dx = ds["dx"].isel(x = 0).values
# ds.close()
print(dx)