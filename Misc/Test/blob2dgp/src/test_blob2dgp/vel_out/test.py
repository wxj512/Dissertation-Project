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


len = 5*4*3*2
arr = np.linspace(1, len, len)

arr = np.reshape(arr, [5, 4, 3, 2])
g = ["a", "b", "c", "d"]
q = ["c", "d"]

dims = {
    "a": [1, 2, 3, 4, 5],
    "b": [6, 7, 8, 9],
    "c": [1, 1, 1],
    "d": [2, 2]
}

dims_attrs = {
    "a": {"long_name": "coord a"},
    "b": {"long_name": "coord b"},
    "c": {"long_name": "coord c"},
    "d": {"long_name": "coord d"}
}

coords = dict(
        [(var, (var, dims[var], dims_attrs[var])) for var in g]
)

da_1 = xr.DataArray(arr, coords = dims, attrs={"long_name": "array 1"})
da_2 = xr.DataArray(arr, coords = dims, attrs={"long_name": "array 2"})
# coords = xr.DataArray(dims, attrs = dims_attrs)

ds = xr.Dataset(
    data_vars = {
    "arr_1": da_1,
    "arr_2": da_2,

    },

    coords = coords

)
# [print(val) for val in dims.values()]
# reshape_list = [np.unique(dims[var].values()).size for var in g if np.unique(dims[var].values()).size != 1]
# print(reshape_list)
# [dims.pop(var, None) for var in list(set(g)-set(q))]
print(itemgetter("a", "b")(dims))