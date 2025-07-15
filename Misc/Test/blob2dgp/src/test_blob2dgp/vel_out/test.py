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

v_max_array = np.linspace(1, 20, 20).reshape((10, 2), order="F")
v_avg_array = np.linspace(21, 40, 20).reshape((10, 2), order="F")

n_calc_method = ["CoM", "n_front midrow"]
B0_data = np.round(np.linspace(0.1,1,10),2)

v_all_ds = xr.Dataset(
    data_vars = dict(
        v_max = (["B0", "n_method"], v_max_array, {"long_name": "maximum velocity", "units": "c_s"}),
        v_avg = (["B0", "n_method"], v_avg_array, {"long_name": "averagevelocity", "units": "c_s"})
    ),
    coords = dict(
        B0 = ("B0", B0_data, {"long_name": "magnetic field", "units": "T"}),
        n_method =  ("n_method", n_calc_method, {"long_name": "density calculation method"})
    ),
)

data_path = v_data.data_import("")[3]
print(data_path)