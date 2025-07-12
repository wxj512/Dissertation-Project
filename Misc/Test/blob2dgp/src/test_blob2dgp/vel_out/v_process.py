import os
import numpy as np
from xbout import open_boutdataset
import matplotlib.pyplot as plt

import v_data, n_front, n_front_FWHM 


def data_import(folder = "delta_1", filepath = ""):
    folder = folder
    if not(filepath == ""):
        filepath = filepath + "/"
    else:
        filepath = "../Data/Input/" + folder + "/"
    return filepath

def main():  
    data_path = v_data.data_import("")[3]

    for file_i, [subdir, dirs, files] in enumerate(os.walk(data_path)):
        if "B0" in subdir:
            
            BOUT_res, BOUT_settings = v_data.data_import(folder = subdir)[0:2]

            ds = open_boutdataset(BOUT_res, inputfilepath=BOUT_settings, info=False)
            ds = ds.squeeze(drop=True)

            dx = ds["dx"].isel(x=0).values
            ds = ds.drop_vars("x")
            ds = ds.assign_coords(x=np.arange(ds.sizes["x"])*dx)

            n_array_CoM = v_data.n_calc(ds)
            n_array_nf = n_front.n_calc(ds)
            # n_array_nf_all = n_front.n_calc(ds, row_calc = "all_row")
            # n_array_FWHM = n_front_FWHM.n_calc(ds, row_calc = "all_row")

            dx_CoM, dz_CoM, vx_CoM, vz_CoM = v_data.vel_calc(n_array_CoM)
            dx_nf, dz_nf, vx_nf, vz_nf = v_data.vel_calc(n_array_nf)
            # dx_nf_all, dz_nf_all, vx_nf_all, vz_nf_all = v_data.vel_calc(n_array_nf_all)
            # dx_FWHM, dz_FWHM, vx_FWHM, vz_FWHM = v_data.vel_calc(n_array_FWHM)

            max_v = np.array([[np.max(vx_CoM)], [np.max(vx_nf)]]).transpose()

            try:
                max_v_array = np.append(max_v_array, max_v, axis = 0)
            except NameError: 
                max_v_array = max_v

    B0_data = np.round(np.linspace(0.1,1,10),2)

    f1 = plt.figure(linewidth = 3, edgecolor = "#000000")
    ax1 = f1.gca()
    ax1.plot(B0_data, max_v_array[:,0], label = "CoM method")
    ax1.plot(B0_data, max_v_array[:,1], label = "n front method \nfor mid row")
    # ax1.plot(B0_data, max_v_array[:,2], label = "n front method \nfor all row")
    # ax1.plot(B0_data, max_v_array[:,2], label = "n front + FWHM method")
    ax1.set_xlabel("B0/T")
    ax1.set_ylabel("$v_{max}$/$c_s$")
    ax1.legend()
    plt.show()

if __name__ == "__main__":
    main()


    