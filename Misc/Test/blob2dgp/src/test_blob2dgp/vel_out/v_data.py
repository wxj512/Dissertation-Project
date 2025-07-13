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
    data_path = scripts_top_level.joinpath("Data", "Input")
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

def n_calc(ds, method = "CoM", t = "", row_calc = "midplane"):
# All n calculation methods:
# CoM = Center of mass method
# max_n = Maximum density method
# n_front = Density front method
# n_front_FWHM = Density front with FWHM method
    n0_scale = consts(ds = ds).n0_scale
    Gridsize = consts(ds = ds).Gridsize

    def n_max(n, n0_scale, row = ""):
        n_max_pos = np.where((n - n0_scale) == np.max(n - n0_scale))

        if row == "":
            n_max_pos = [int(n_max_pos[0][0]), int(n_max_pos[1][0])]
        else:
            n_max_pos = [int(n_max_pos[0][0]), int(row)]
    
        return n_max_pos
    
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
    
    def gaussian(x, *params):
        A = params[0]
        x0 = params[1]
        c = params[2]
        n = 2
        return A*np.exp(-((x-x0)/(np.sqrt(2)*c))**n)

    def FWHM(c, n):
        FWHM = 2*np.sqrt(2)*(np.log(2)**(1/n))*c 
        return FWHM

    if t == "":
        tvals = np.linspace(0, ds["t"].shape[0]-1, ds["t"].shape[0], dtype = int)
    else:
        tvals = t

    for i,vals in enumerate(tqdm(tvals)):

        ds_data = ds.isel(t = vals)

        if method == "CoM":
            n_point = np.array(ndimage.center_of_mass(ds_data["n"].values - n0_scale)) * Gridsize
        if method == "max_n" or "n_front" or "n_front_FWHM":
            if row_calc == "midplane":
                row_j = int(ds_data["z"].shape[0]/2)
                n = ds_data["n"].values[:,row_j] - n0_scale
                if method == "max_n":
                    n_point = n_max(n, n0_scale, row_j)
                elif method == "n_front" or "n_front_FWHM":
                    max_peak_j, peak_2_j = n_peak(n)
            elif row_calc == "all_row":
                if method == "max_n":
                    n = ds_data["n"].values - n0_scale
                    n_point = n_max(n, n0_scale)
                elif method == "n_front" or "n_front_FWHM":
                    for j,z_vals in enumerate(ds_data["z"].values):
                        n = ds_data["n"].values[:,j] - n0_scale
                        #Find peaks of rows
                        max_peak, peak_2 = n_peak(n)
                        # Makes sure this condition is fullfilled at j = 0
                        if j == 0:
                            max_peak_j = 0
                            if method == "n_front_FWHM":
                                peak_2_j = 0
                        elif max_peak == 0:
                            continue
                        elif max_peak>max_peak_j:
                            max_peak_j = max_peak
                            row_j = j
                            if method == "n_front_FWHM":
                                peak_2_j = peak_2
                                peak_n = n
                        else:
                            continue

            if method == "n_front":
                n_point = [ds["x"].values[max_peak_j], ds["z"].values[row_j]]
            elif method == "n_front_FWHM":
                #   Mask data
                width_guess = ((max_peak_j - peak_2_j)*0.5)*2
                x_array = np.linspace(0, n.size-1, n.size)
                mask_n = np.ma.masked_outside(x_array, max_peak_j - (width_guess/2), max_peak_j + (width_guess/2))
                mask_n = np.ones_like(mask_n) * peak_n
                mask_n[np.where(mask_n.data == 1)[0]] = "nan"
                # Find gaussian
                guess = [peak_n[max_peak_j], max_peak_j, 1 / (peak_n[max_peak_j] * np.sqrt(2 * np.pi))]
                popt, pcov = curve_fit(gaussian, x_array, mask_n, p0 = guess, nan_policy = 'omit')
                # gauss_fit = gaussian(x_array, *popt)
                gauss_width = FWHM(popt[2], 2)
                n_front = max_peak_j + (gauss_width / 2)
                n_point = [n_front * Gridsize, ds["z"].values[row_j]]

        if i == 0:
            n_array = [n_point]
        else:
            n_array = np.append(n_array, [n_point], axis = 0)
        
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
    
    BOUT_res, BOUT_settings = data_import("")[0:2]

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
    n_array = n_calc(ds, method="CoM")
   
    dist_x, dist_z, vx, vz = vel_calc(n_array)

    # print(np.shape(n_array))

    dist_array = [dist_x]
    vel_array = [vx]
    # print(np.max(vx))
    v_plot(ds["t"].values, dist_array, vel_array)

if __name__ == "__main__":
    main()