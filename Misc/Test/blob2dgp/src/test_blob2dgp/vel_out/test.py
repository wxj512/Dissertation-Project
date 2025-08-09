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
data_input_path = data_path.joinpath("Input")
data_input_path = data_input_path.joinpath(f"campaign_{2}")
total = len(list(data_input_path.glob("*/")))
folder_list = natsorted([folder.name for folder in data_input_path.glob("*/")])
# [print(i) for i in folder_list]
param_var = ["B0", "Te0", "n0", "R_c"] 
parval_array = np.empty((0, len(param_var)))

# for file_i, folder in enumerate(folder_list):
#     print(f"Processing {file_i + 1} of {total}")
#     print(f"Folder: {folder}")

#     folder = f"campaign_{2}/" + folder

#     BOUT_res, BOUT_settings = v_data.data_import(folder = folder)[0:2]

#     with open_boutdataset(BOUT_res, inputfilepath = BOUT_settings, info = False) as ds:

#         ds = ds.squeeze(drop=True)

#         dx = ds["dx"].isel(x = 0).values
#         ds = ds.drop_vars("x")
#         ds = ds.assign_coords(x = np.arange(ds.sizes["x"])*dx)

#         n0_scale = v_data.consts(ds).n0_scale
#         Gridsize = v_data.consts(ds).Gridsize

#         tvals = np.linspace(0, ds["t"].shape[0]-1, ds["t"].shape[0], dtype = int)
#         # n_array = np.empty((0, 2))

        
#         param_val = np.array([[ds.copy().attrs["options"]["model"][var]] for var in param_var]).transpose()
    
#     parval_array = np.append(parval_array, param_val, axis = 0)
#     parval_split = np.empty((0,parval_array.shape[0]))
#     parval_split = [np.append(parval_split, parval_array[:,col]) for col in np.arange(parval_array.shape[1])[::-1]]
#     parval_sort = np.lexsort(parval_split,axis=0)
#     parval_array = parval_array[parval_sort] 

# np.savetxt("./vel_out/parval.txt", parval_array, delimiter = ";")

a = np.loadtxt("./vel_out/parval.txt", delimiter=";")
b = np.loadtxt("./vel_out/parval.txt", delimiter=";")
df = pd.DataFrame(a, columns = param_var)
ds = pd.DataFrame(b, columns = param_var)  
df = pd.concat((df, ds), axis = 1)
print(df)
print(df["B0"])

    #     n_array_nf_all = v_data.n_calc(ds, method = "n_front", row_calc = "all_row")
        # print(Te0)

        # for i,vals in enumerate((tvals)):
        #     ds_data = ds.isel(t = vals).copy()
            # n_point = v_data.n_calc_methods(ds_data, row_calc = "mid_row", n0_scale = n0_scale, Gridsize = Gridsize, method = "CoM")
            # n_array = np.append(n_array, [n_point], axis = 0)

            # def n_array(ds_data, n0_scale, row):
            #     n = ds_data["n"].copy()
            #     if row != "whole_grid":
            #         n = n.isel(z = row)
            #     return np.array(n) - n0_scale
            
            # def n_peak(n, height = 0.01, prominence = 0.005, row_calc = "mid_row", ds_col = 260):
            #     peaks, _ = find_peaks(n, height = height, prominence = prominence)
            #     if not(peaks.size > 0):
            #         max_peak = 0
            #     elif row_calc == "mid_row":
            #         max_peak = np.max(peaks)
            #         max_peak_row = None
            #     else:
            #         max_peak = np.max(peaks % ds_col)
            #         max_peak_row = peaks[np.where((peaks % ds_col) == max_peak)[0][0]] // ds_col
            #     return max_peak, max_peak_row
            
            # ds_col = ds_data["x"].size
            # n_row = "whole_grid"
            # n_flat = np.ravel(n_array(ds_data, n0_scale, n_row), order="F")
            # max_peak, row = n_peak(n_flat, row_calc = "all_row", ds_col = ds_col)
            # print(max_peak, row)
 
        
    # if file_i == total-1:
    #     print(n_array_nf_all)

    

   

