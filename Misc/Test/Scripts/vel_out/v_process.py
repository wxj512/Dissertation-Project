import os
import numpy as np
import pandas as pd
from xbout import open_boutdataset
import matplotlib.pyplot as plt
from scipy import ndimage
from boututils import calculus as calc
from tqdm import tqdm

import v_data, n_front, n_front_FWHM 


def data_import(folder = "delta_1", filepath = ""):
    folder = folder
    if not(filepath == ""):
        filepath = filepath + "/"
    else:
        filepath = "../Data/Input/" + folder + "/"
    return filepath

if __name__ == "__main__":
    
    path = "../Data/Input/"

    for file_i, [subdir, dirs, files] in enumerate(os.walk(path)):
        if "B0" in subdir:
            filepath = data_import(filepath=subdir)
            print(filepath)
            BOUT_inp = filepath + "BOUT.inp"
            BOUT_res = filepath + "BOUT.dmp.*.nc"

            ds = open_boutdataset(BOUT_res, info=False)
            ds = ds.squeeze(drop=True)

            dx = ds["dx"].isel(x=0).values
            ds = ds.drop_vars("x")
            ds = ds.assign_coords(x=np.arange(ds.sizes["x"])*dx)

            n_array_CoM = v_data.n_calc(ds)
            n_array_nf = n_front.n_calc(ds)
            # n_array_FWHM = n_front_FWHM.n_calc(ds)

            v_CoM = v_data.vel_calc(n_array_CoM)
            v_nf = v_data.vel_calc(n_array_nf)
            # v_FWHM = v_data.vel_calc(n_array_FWHM)

            max_v = np.array([[np.max(v_CoM)], [np.max(v_nf)]]).transpose()

            try:
                max_v_array = np.append(max_v_array, max_v, axis = 0)
            except: 
                max_v_array = max_v

    B0_data = np.round(np.linspace(0.1,1,10),2)

    f1 = plt.figure(linewidth = 3, edgecolor = "#000000")
    ax1 = f1.gca()
    ax1.plot(B0_data, max_v_array[:,0], label = "CoM method")
    ax1.plot(B0_data, max_v_array[:,1], label = "n front method")
    ax1.set_xlabel("B0/T")
    ax1.set_ylabel("$v_{max}$/$c_s$")
    ax1.legend()
    plt.show()


    