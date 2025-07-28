import pathlib
import sys
import numpy as np
from xbout import open_boutdataset
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
from tqdm import tqdm


def data_import(folder = ""):
    if folder == "":
        folder = "delta_1"
    else:
        folder = folder
    top_level_dir = pathlib.Path(__file__).parents[1]
    scripts_top_level = top_level_dir.parents[2]
    data_path = scripts_top_level.joinpath("Data")
    filepath = scripts_top_level.joinpath("Data", "Input", folder)
    BOUT_res = filepath.joinpath("BOUT.dmp.*.nc")
    BOUT_settings = filepath.joinpath("BOUT.settings")
    BOUT_inp = filepath.joinpath("BOUT.inp")
    return BOUT_res, BOUT_settings, BOUT_inp, data_path,

class consts:
# With reference to .settings file
    def __init__(self, ds = None, folder = None):
        if ds is not None:
            ds = ds
        else:
            print("No ds specified, checking folder")
            if folder is None:
                print("Folder default to delta_1/")
                folder = "delta_1"
            else:
                folder = folder
            BOUT_res, BOUT_settings = data_import(folder = folder)[0:2]
            ds = open_boutdataset(BOUT_res, inputfilepath=BOUT_settings , info=False)
        
        try:
            self.Te0 = ds.attrs["options"]["model"]["Te0"]
            self.n0 = ds.attrs["options"]["model"]["n0"]
            self.n0_scale = ds.attrs["options"]["n"]["scale"]
            self.Gridsize = ds.attrs["options"]["mesh"]["dx"]
            self.B0 = ds.attrs["options"]["model"]["B0"]
        except TypeError:
            print("Error: check if ds has specified inputfilepath for .settings")
            sys.exit()

def n_calc_methods(ds_data, row_calc, n0_scale, Gridsize, method):
        
    def n_array(ds_data, n0_scale, row):
        if row == "whole_grid":
            n = ds_data["n"].values - n0_scale
        else:
            n = ds_data["n"].values[:,row] - n0_scale
        return n
    
    if method == "CoM":
        row = "whole_grid"
        return np.array(ndimage.center_of_mass(n_array(ds_data, n0_scale, row))) * Gridsize
    
    if method == "n_max":
        
        def n_max_pos(n, n0_scale, row = ""):
            n_max_pos = np.where((n - n0_scale) == np.max(n - n0_scale))
            if row == "":
                n_max_pos = [int(n_max_pos[0][0]), int(n_max_pos[1][0])]
            else:
                n_max_pos = [int(n_max_pos[0][0]), int(row)]
            return n_max_pos
        
        if row_calc == "mid_row":
            row = int(ds_data["z"].shape[0]/2)
            return n_max_pos(n_array(ds_data, n0_scale, row), n0_scale, row = row)
        elif row_calc == "all_row":
            row = "whole_grid"
            return n_max_pos(n_array(ds_data, n0_scale, row), n0_scale)
        
    if method == "n_front" or "n_front_FWHM":
        
        def n_peak(n, height = 0.01, row_calc = "mid_row", ds_col = 260):
            peaks, _ = find_peaks(n, height = height)
            if not(peaks.size > 0):
                max_peak = 0
            elif row_calc == "mid_row":
                max_peak = np.max(peaks)
                max_peak_row = None
            else:
                max_peak = np.max(peaks % ds_col)
                max_peak_row = peaks[np.where((peaks % ds_col) == max_peak)[0][0]] // ds_col
            return max_peak, max_peak_row
        
        ds_col = ds_data["x"].size

        if row_calc == "mid_row":
            row = int(ds_data["z"].shape[0]/2)
            ## max peak row not returned as always returns 0 if only 1 n row specified
            max_peak, _ = n_peak(n_array(ds_data, n0_scale, row))
        elif row_calc == "all_row":
            row = "whole_grid"
            n_flat = np.ravel(n_array(ds_data, n0_scale, row), order="F")
            max_peak, row = n_peak(n_flat, row_calc = row_calc, ds_col = ds_col)
        
        if max_peak == (ds_data["x"].size - 1) or method == "n_front":
            return [ds_data["x"].values[max_peak], ds_data["z"].values[row]]#, row

        def peak_2(n, max_peak, height=0.01):
            peaks, _ = find_peaks(n, height = height)
            if not(peaks.size > 0):
                peak_2 = 0
            elif peaks.size == 1:
                peak_2 = max_peak - (np.where(n > 0.0001 * n[max_peak])[0][-1] - max_peak)
            else:
                peak_2 = peaks[-2]
            return peak_2
        
        def gaussian(x, *params):
            A = params[0]
            x0 = params[1]
            c = params[2]
            return A * np.exp(-((x - x0)/(np.sqrt(2) * c)) ** 2)

        def FWHM(c):
            FWHM = 2 * np.sqrt(2) * (np.log(2) ** (1/2)) * c 
            return FWHM
        
        #   Mask data
        peak_n = n_array(ds_data, n0_scale, row)
        peak_n2 = peak_2(peak_n, max_peak)
        width_guess = ((max_peak - peak_n2) * 0.5) * 2
        x_array = np.linspace(0, peak_n.size-1, peak_n.size)
        mask_n = np.ma.masked_outside(x_array, max_peak - (width_guess / 2), max_peak + (width_guess / 2))
        mask_n = np.ones_like(mask_n) * peak_n
        mask_n[np.where(mask_n.data == 1)[0]] = "nan"
        # Find gaussian
        param_1 = peak_n[max_peak]; param_2 = max_peak * Gridsize; param_3 = 1 / (peak_n[max_peak] * np.sqrt(2 * np.pi))
        guess = [param_1, param_2, param_3]
        bnd = ([-np.inf, -np.inf, 0], [np.inf, np.inf, np.inf])
        popt, _ = curve_fit(gaussian, x_array * Gridsize, mask_n, p0 = guess, nan_policy = 'omit', bounds = bnd)
        gauss_width = FWHM(popt[2])
        gauss_fit = gaussian(x_array*0.3, *popt)
        if max_peak * Gridsize + (gauss_width / 2) >= ds_data["x"].values.max():
            n_front = ds_data["x"].values.max()
        else:
            n_front = max_peak * Gridsize + (gauss_width / 2)
        return [n_front, ds_data["z"].values[row]]#, row, gauss_fit


def n_calc(ds, method = "CoM", t = "", row_calc = "mid_row"):
# All n calculation methods:
# CoM = Center of mass method
# max_n = Maximum density method
# n_front = Density front method
# n_front_FWHM = Density front with FWHM method
    n0_scale = consts(ds = ds).n0_scale
    Gridsize = consts(ds = ds).Gridsize

    if t == "":
        tvals = np.linspace(0, ds["t"].shape[0]-1, ds["t"].shape[0], dtype = int)
    else:
        tvals = t

    n_array = np.empty((0, 2))

    for i,vals in enumerate((tvals)):
        ds_data = ds.isel(t = vals)
        n_point = n_calc_methods(ds_data, row_calc, n0_scale, Gridsize, method)
        n_array = np.append(n_array, [n_point], axis = 0)
        ds_data.close()
    return n_array

def vel_calc(array):
        
    dist_x = array[:,0] - array[0,0]
    dist_z = array[:,1] - array[0,1]
    
    vx = np.gradient(dist_x)
    vz = np.gradient(dist_z)

    return dist_x, dist_z, vx, vz


def v_plot(time_array, dist_array, vel_array, plot_label = "", title = ""):

    f1 = plt.figure(1, linewidth = 3, edgecolor = "#000000")
    ax1 = f1.gca()
    ax2 = ax1.twinx()
    if not(title == ""):
        ax1.set_title("Distance and velocity of blob " + title)
    else:
        ax1.set_title("Distance and velocity of blob")
    box = ax1.get_position()
    ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    ax2.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    plots = np.shape(dist_array)[0]
    cmap = plt.cm.tab10.colors[:]

    for no,val in enumerate(np.linspace(0, plots -1, plots)):
        
        if not(plot_label == ""):
            ax1.plot(time_array, dist_array[no], label = "Distance " + plot_label[no], color = cmap[2 * no])
            ax2.plot(time_array, vel_array[no], label = "Velocity " + plot_label[no], color = cmap[2 * no + 1])
        else:
            ax1.plot(time_array, dist_array[no], label = "Distance", color = cmap[2 * no])
            ax2.plot(time_array, vel_array[no], label = "Velocity", color = cmap[2 * no + 1])

    ax1.set_xlabel("Time/(1/$\\Omega_i$)")
    ax1.set_ylabel("Distance/$\\rho_s$")
    ax2.set_ylabel("Velocity/$c_s$")
    f1.legend(bbox_to_anchor = (1, 0.9), fontsize = "small")
    plt.show()

    return f1
    

def main():
    
    BOUT_res, BOUT_settings = data_import(folder = "campaign_1/delta_1_B0_0.1_Te0_4.0")[0:2]

    ds = open_boutdataset(BOUT_res, inputfilepath=BOUT_settings, info=False)
    ds = ds.squeeze(drop=True)

    dx = ds["dx"].isel(x=0).values
    ds = ds.drop_vars("x")
    ds = ds.assign_coords(x=np.arange(ds.sizes["x"])*dx)


    # t = 10
    # n0_scale = 1
    # Gridsize = 0.3
    # ds_data = ds.isel(t=t)
    # n_point = np.array([ndimage.center_of_mass(ds_data["n"].values - n0_scale)]) * Gridsize
    n_array_nf_all = n_calc(ds, method="n_front", row_calc="all_row")
    n_array_FWHM_all = n_calc(ds, method = "n_front_FWHM", row_calc = "all_row")
    
    dist_x, dist_z, vx, vz = vel_calc(n_array_nf_all)
    dist_x_all, dist_z_all, vx_all, vz_all = vel_calc(n_array_FWHM_all)

    # print(np.shape(n_array))
    title = "for n front and \nn front with FWHM method"
    dist_array = [dist_x, dist_x_all]
    vel_array = [vx, vx_all]
    plot_label = ["for n front \nmethod", "for n front +\nFWHM method"]
    # print(np.max(vx))
    v_plot(ds["t"].values, dist_array, vel_array, plot_label=plot_label, title=title)

if __name__ == "__main__":
    main()