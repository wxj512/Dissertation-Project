import numpy as np
from xbout import open_boutdataset
import matplotlib.pyplot as plt
from scipy import ndimage
from boututils import calculus as calc
from scipy.signal import find_peaks
from tqdm import tqdm

import v_data

def data_import(_):
    folder = "delta_1_B0_0.1"
    filepath = "../Data/Input/" + folder + "/"
    return filepath

def n_calc(ds, Gridsize = 0.3, n0_scale = 1, row_calc = "midplane", t = ""):
    
    def n_peak(n, height=0.02):
            peaks = find_peaks(n, height=height)
            
            if not(peaks[0].size > 0):
                max_peak = 0
            else:
                max_peak = np.max(peaks[0])

            return max_peak
    
    if t == "":
        tvals = np.linspace(0, ds["t"].shape[0]-1, ds["t"].shape[0], dtype = int)
    else:
        tvals = t

    for i,vals in enumerate(tqdm(tvals)):

        ds_data = ds.isel(t = vals)
        
        if row_calc == "midplane":
            row_j = int(ds_data["z"].shape[0]/2)
            n = ds_data["n"].values[:,row_j] - n0_scale
            max_peak_j = n_peak(n)
        elif row_calc == "all_row":

            for j,z_vals in enumerate(ds_data["z"].values):
                
                n = ds_data["n"].values[:,j] - n0_scale

                #Find peaks of rows
                max_peak = n_peak(n)
                
                # Makes sure this condition is fullfilled at j = 0
                if j == 0:
                    max_peak_j = 0

                if max_peak == 0:
                    continue
                
                if max_peak>max_peak_j:
                    max_peak_j = max_peak
                    row_j = j
                else:
                    continue
            
            
        # Find furthest x value of grid of furthest n and return row of z with furthest n
        if i == 0:
            # row = row_j
            # max_x = max_peak_j
            n_array = [[ds["x"].values[max_peak_j], ds["z"].values[row_j]]]
            # f1 = plt.figure(1)
            # ax1 = f1.gca()
   
        else:
            # row = np.append(row, row_j)
            # max_x = np.append(max_x, max_peak_j)
            n_array = np.append(n_array, [[ds["x"].values[max_peak_j], ds["z"].values[row_j]]], axis = 0)
            # n = ds_data["n"].values[:,row_j]-n0_scale

        # ax1.plot(n, linewidth=0.5)
        # ax1.scatter(max_peak_j, n[max_peak_j], color = "orange", marker = "x")
    
    return n_array # ,f1

if __name__ == "__main__":

    filepath = data_import("")

    BOUT_inp = filepath + "BOUT.inp"
    BOUT_res = filepath + "BOUT.dmp.*.nc"

    ds = open_boutdataset(BOUT_res, info=False)
    ds = ds.squeeze(drop=True)


    dx = ds["dx"].isel(x=0).values
    ds = ds.drop_vars("x")
    ds = ds.assign_coords(x=np.arange(ds.sizes["x"])*dx)
    ds_data = ds.isel(t=10)

    # for j,z_vals in enumerate(ds_data["z"].values):
                
    #             n = ds_data["n"].values[:,j] - 1

    #             #Find peaks of rows
    #             peaks = find_peaks(n, height=0.02)
               
    #             # Makes sure this condition is fullfilled at j = 0
    #             if j == 0:
    #                 max_peak_j = 0

    #             if not(peaks[0].size > 0):
    #                 max_peak = 0
    #             else:
    #                 max_peak = np.max(peaks[0])

    #             if max_peak == 0:
    #                 continue
                
    #             if max_peak>max_peak_j:
    #                 max_peak_j = max_peak
    #                 row_j = j
    #             else:
    #                 continue
    # row = row_j
    # n = ds_data["n"].values[:,row]-1
    # peaks = find_peaks(n, height=0)
    # max_peak = np.max(peaks[0])
    # print(ds["z"].values[row_j])

    # f1 = plt.figure(1, linewidth = 3, edgecolor = "#000000")
    # ax1 = f1.gca()
    # ax1.set_title("z/$\\rho_s$ = " + str(np.round(ds["z"].values[row_j],1)) + ", t/(1/$\\Omega_i$) = " + str(10*500))
    # ax1.plot(n,linewidth=0.5, label="Density profile")
    # ax1.scatter(max_peak_j,n[max_peak_j],marker="x", color="orange", label="Peak position")
    # ax1.set_xlabel("x/$\\rho_s$")
    # ax1.set_ylabel("Density/(n/$n_0$)")
    # ax1.legend(fontsize="small")


    # f2 = plt.figure(2)
    # ds_data["n"].plot(x="x",y="z")

    n_array = n_calc(ds)
    n_array_all = n_calc(ds, row_calc = "all_row")

    dist_x, dist_z, vx, vz = v_data.vel_calc(n_array)
    
    dx_all, dz_all, vx_all, vz_all = v_data.vel_calc(n_array_all)

    title = "for n front method"
    dist_array = [dist_x, dx_all]
    vel_array = [vx, vx_all]
    plot_label = ["for \nmid row", "for \nall row"]

    f1 = v_data.v_plot(ds["t"],dist_array,vel_array, plot_label=plot_label, title=title)
 
    plt.show()