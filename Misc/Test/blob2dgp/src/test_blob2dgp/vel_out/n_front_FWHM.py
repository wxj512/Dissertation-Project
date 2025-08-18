import numpy as np
from xbout import open_boutdataset
import matplotlib.pyplot as plt
from scipy import ndimage
from boututils import calculus as calc
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
from tqdm import tqdm

import v_data


def n_calc(ds, Gridsize = 0.3, n0_scale = 1, row_calc = "mid_row", t = ""):
    
    def gaussian(x, *params):
        A = params[0]
        x0 = params[1]
        c = params[2]
        n = 2
        return A*np.exp(-((x-x0)/(np.sqrt(2)*c))**n)

    def FWHM(c, n):
        FWHM = 2*np.sqrt(2)*(np.log(2)**(1/n))*c 
        return FWHM

    def n_peak(n, height=0.02):
            peaks = find_peaks(n, height=height)
            
            if not(peaks[0].size > 0):
                max_peak = 0
                peak_2 = 0
            elif peaks[0].size == 1:
                max_peak = np.max(peaks[0])
                peak_2 = max_peak - (np.where(n>1e-02)[0][-1] - max_peak)
            else:
                max_peak = np.max(peaks[0])
                peak_2 = peaks[0][-2]

            return max_peak, peak_2
    
    if t == "":
        tvals = np.linspace(0, ds["t"].shape[0]-1, ds["t"].shape[0], dtype = int)
    else:
        tvals = t

    for i,vals in enumerate(tqdm(tvals)):
        
        ds_data = ds.isel(t = vals)
        
        if row_calc == "mid_row":
            row_j = int(ds_data["z"].shape[0]/2)
            n = ds_data["n"].values[:,row_j] - n0_scale
            max_peak_j, peak_2_j = n_peak(n, height=0.015)
        elif row_calc == "all_row":

            for j,z_vals in enumerate(ds_data["z"].values):

                n = ds_data["n"].values[:,j] - n0_scale

                #Find peaks of rows
                max_peak, peak_2 = n_peak(n)
                
                # Makes sure this condition is fullfilled at j = 0
                if j == 0:
                    max_peak_j = 0
                    peak_2_j = 0

                if max_peak == 0:
                    continue
                
                if max_peak>max_peak_j:
                    max_peak_j = max_peak
                    peak_2_j = peak_2
                    row_j = j
                else:
                    continue
            
        # Mask data
        n = ds_data["n"].values[:,row_j] - 1
        width_guess = ((max_peak_j - peak_2_j)*0.5)*2
        x_array = np.linspace(0, n.size-1, n.size)
        mask_n = np.ma.masked_outside(x_array, max_peak_j - (width_guess/2), max_peak_j + (width_guess/2))
        mask_n = np.ones_like(mask_n)*n
        mask_n[np.where(mask_n.data==1)[0]] = "nan"
        # Find gaussian
        guess = [n[max_peak_j], max_peak_j, 1/(n[max_peak_j]*np.sqrt(2*np.pi))]
        popt, pcov = curve_fit(gaussian, x_array, mask_n, p0 = guess, nan_policy = 'omit')
        # gauss_fit = gaussian(x_array, *popt)
        gauss_width = FWHM(popt[2], 2)
        n_front = max_peak_j + (gauss_width / 2)


        # Find furthest x value of grid of furthest n and return row of z with furthest n
        if i == 0:
            # row = row_j
            # max_x = max_peak_j
            n_array = [[n_front*Gridsize, ds["z"].values[row_j]]]
            # f1 = plt.figure(1)
            # ax1 = f1.gca()
   
        else:
            # row = np.append(row, row_j)
            # max_x = np.append(max_x, max_peak_j)
            n_array = np.append(n_array, [[n_front*Gridsize, ds["z"].values[row_j]]], axis = 0)
            # n = ds_data["n"].values[:,row_j]-n0_scale

        # ax1.plot(n, linewidth=0.5, alpha = 0.4)
        # ax1.plot(gaussian(x_array,*popt))
        # ax1.scatter(max_peak_j, n[max_peak_j], color = "orange", marker = "x")
    
    return n_array # ,f1


# ds_data = ds.isel(t=50)
# row = int(ds_data["z"].values.size/2)
# n = ds_data["n"].values[:,row]-1
# peaks = find_peaks(n, height=0)
# max_peak = np.max(peaks[0])
# # print(peaks[0])

# f1 = plt.figure(1)
# ax1 = f1.gca()
# ax1.plot(n,linewidth=0.5)
# ax1.scatter(max_peak,n[max_peak],marker="x", color="orange")


# f2 = plt.figure(2)
# ds_data["n"].plot(x="x",y="z")

def main():

    def gaussian(x, *params):
        A = params[0]
        x0 = params[1]
        c = params[2]
        n = 2
        return A*np.exp(-((x-x0)/(np.sqrt(2)*c))**n)

    def FWHM(c, n):
        FWHM = 2*np.sqrt(2)*(np.log(2)**(1/n))*c 
        return FWHM

    def n_peak(n, height=0.02):
            peaks = find_peaks(n, height=height)
            
            if not(peaks[0].size > 0):
                max_peak = 0
                peak_2 = 0
            elif peaks[0].size == 1:
                max_peak = np.max(peaks[0])
                peak_2 = max_peak - (np.where(n>1e-02)[0][-1] - max_peak)
            else:
                max_peak = np.max(peaks[0])
                peak_2 = peaks[0][-2]

            return max_peak, peak_2

    BOUT_res, BOUT_settings = v_data.data_import(folder = "delta_1")[0:2]

    ds = open_boutdataset(BOUT_res, inputfilepath=BOUT_settings, info=False)
    ds = ds.squeeze(drop=True)
    dx = ds["dx"].isel(x=0).values
    ds = ds.drop_vars("x")
    ds = ds.assign_coords(x=np.arange(ds.sizes["x"])*dx)
    t = 10
    ds_data = ds.isel(t=t)

    n0_scale = 1
    row_j = int(ds_data["z"].shape[0]/2)
    n = ds_data["n"].values[:,row_j] - n0_scale
    max_peak_j, peak_2_j = n_peak(n, height=0.02)

    # for j,z_vals in enumerate(ds_data["z"].values):
    
    #     n0_scale = 1
    #     n = ds_data["n"].values[:,j] - n0_scale

    #     #Find peaks of rows
    #     max_peak, peak_2 = n_peak(n)
        
    #     # Makes sure this condition is fullfilled at j = 0
    #     if j == 0:
    #         max_peak_j = 0
    #         peak_2_j = 0

    #     if max_peak == 0:
    #         continue
        
    #     if max_peak>max_peak_j:
    #         max_peak_j = max_peak
    #         peak_2_j = peak_2
    #         row_j = j
    #     else:
    #         continue

    row = row_j
    n = ds_data["n"].values[:,row]-1
    
    # Mask data
    # n = ds_data["n"].values[:,row_j] - 1
    width_guess = ((max_peak_j - peak_2_j)*0.5)*2
    x_array = np.linspace(0, n.size-1, n.size)
    mask_n = np.ma.masked_outside(x_array, max_peak_j - (width_guess/2), max_peak_j + (width_guess/2))
    mask_n = np.ones_like(mask_n)*n
    mask_n[np.where(mask_n.data==1)[0]] = "nan"
    # Find gaussian
    guess = [n[max_peak_j], max_peak_j, 1]
    popt, pcov = curve_fit(gaussian, x_array, mask_n, p0 = guess, nan_policy = 'omit')
    # gauss_fit = gaussian(x_array, *popt)
    gauss_width = FWHM(popt[2], 2)
    n_front = max_peak_j + (gauss_width / 2)
    gauss_fit = gaussian(x_array, *popt)

    f1 = plt.figure(1, linewidth = 3, edgecolor = "#000000")
    ax1 = f1.gca()
    ax1.set_title("z/$\\rho_s$ = " + str(np.round(ds["z"].values[row_j],1)) + ", t/(1/$\\Omega_i$) = " + str(t*50))
    ax1.plot(n,linewidth=0.8, label="Density profile")
    ax1.plot(gauss_fit, linewidth=0.8, linestyle = "-.", label="Gaussian fit of last peak")
    ax1.scatter(max_peak_j,n[max_peak_j],marker="x", color="orange", label="Peak position")
    ax1.vlines(max_peak_j+(gauss_width/2), np.min(n)-0.05, np.max(n)+0.1, linestyle = "--", linewidth=0.5, color="black", label = "Position of \nright side of FWHM")
    ax1.set_xlim(0,260)
    ax1.set_ylim(np.min(n)-0.05, np.max(n)+0.1)
    ax1.set_xlabel("x/$\\rho_s$")
    ax1.set_ylabel("Density/(n/$n_0$)")
    ax1.legend(fontsize="small")

    # n_array = n_calc(ds)
    # n_array_all = n_calc(ds, row_calc = "all_row")

    # dist_x, dist_z, vx, vz = v_data.vel_calc(n_array)
    # dx_all, dz_all, vx_all, vz_all = v_data.vel_calc(n_array_all)

    # title = "for n front + FWHM method"
    # dist_array = [dist_x, dx_all]
    # vel_array = [vx, vx_all]
    # plot_label = ["for \nmid row", "for \nall row"]

    # f1 = v_data.v_plot(ds["t"],dist_array,vel_array, plot_label=plot_label, title=title)

    plt.show()

if __name__ == "__main__":
    main()