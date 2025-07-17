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

class n_calc_methods:
    
    def __init__(self, ds_data, row_calc, n0_scale, Gridsize):
        self.ds_data = ds_data.copy()
        self.row_calc = row_calc
        self.n0_scale = n0_scale
        self.Gridsize = Gridsize
        del ds_data
        
    def n_array(self, row):
        if row == "whole_grid":
            self.n = self.ds_data["n"].values - self.n0_scale
        else:
            self.n = self.ds_data["n"].values[:,row] - self.n0_scale
        return self.n
    
    def CoM(self):
        self.n_point = np.array(ndimage.center_of_mass(self.n_array("whole_grid"))) * self.Gridsize
        del self.ds_data
        return self.n_point
    
    def n_max(self):
        
        def n_max_pos(n, n0_scale, row = ""):
            n_max_pos = np.where((n - n0_scale) == np.max(n - n0_scale))
            if row == "":
                n_max_pos = [int(n_max_pos[0][0]), int(n_max_pos[1][0])]
            else:
                n_max_pos = [int(n_max_pos[0][0]), int(row)]
            return n_max_pos
        
        if self.row_calc == "midrow":
            row = int(self.ds_data["z"].shape[0]/2)
            self.n_point = n_max_pos(self.n_array(row), self.n0_scale, row = row)
        elif self.row_calc == "all_row":
            self.n_point = n_max_pos(self.n_array("whole_grid"), self.n0_scale)
        
        del self.ds_data
        return self.n_point
        
    def n_front(self, FWHM = False):
        
        def n_peak(n, height=0.001, prominence = 0.0006, row_calc = "midrow", ds_col = 260):
            peaks, _ = find_peaks(n, height = height, prominence = prominence)
            if not(peaks.size > 0):
                max_peak = 0
            elif row_calc == "midrow":
                max_peak = np.max(peaks)
                max_peak_row = None
            else:
                max_peak = np.max(peaks % ds_col)
                max_peak_row = peaks[np.where((peaks % ds_col) == max_peak)[0][0]] // ds_col
            return max_peak, max_peak_row
        
        def peak_2(n, max_peak, height=0.001, prominence = 0.0006):
            peaks, _ = find_peaks(n, height = height, prominence = prominence)
            if not(peaks.size > 0):
                peak_2 = 0
            elif peaks.size == 1:
                peak_2 = max_peak - (np.where(n > 0.0001 * n[max_peak])[0][-1] - max_peak)
            else:
                peak_2 = peaks[-2]
            return peak_2
        
        ds_col = self.ds_data["x"].size

        if self.row_calc == "midrow":
            row = int(self.ds_data["z"].shape[0]/2)
            ## max peak row not returned as always returns 0 if only 1 n row specified
            max_peak, _ = n_peak(self.n_array(row), row_calc = self.row_calc)
        elif self.row_calc == "all_row":
            n_flat = np.ravel(self.n_array("whole_grid"), order="F")
            max_peak, row = n_peak(n_flat, row_calc = self.row_calc, ds_col = ds_col)
        
        if FWHM == False:
            self.n_point = [self.ds_data["x"].values[max_peak], self.ds_data["z"].values[row]]
        elif FWHM == True:

            def gaussian(x, *params):
                A = params[0]
                x0 = params[1]
                c = params[2]
                return A * np.exp(-((x - x0)/(np.sqrt(2) * c)) ** 2)

            def FWHM(c):
                FWHM = 2 * np.sqrt(2) * (np.log(2) ** (1/2)) * c 
                return FWHM
            
            #   Mask data
            peak_n = self.n_array(row)
            peak_n2 = peak_2(peak_n, max_peak)
            width_guess = ((max_peak - peak_n2) * 0.5) * 2
            x_array = np.linspace(0, peak_n.size-1, peak_n.size)
            mask_n = np.ma.masked_outside(x_array, max_peak - (width_guess / 2), max_peak + (width_guess / 2))
            mask_n = np.ones_like(mask_n) * peak_n
            mask_n[np.where(mask_n.data == 1)[0]] = "nan"
            # Find gaussian
            guess = [peak_n[max_peak], max_peak * self.Gridsize, 1 / (peak_n[max_peak] * np.sqrt(2 * np.pi))]
            bnd = ([-np.inf, -np.inf, 0], [np.inf, np.inf, np.inf])
            popt, _ = curve_fit(gaussian, x_array * self.Gridsize, mask_n, p0 = guess, nan_policy = 'omit', bounds = bnd)
            gauss_width = FWHM(popt[2])
            n_front = max_peak * self.Gridsize + (gauss_width / 2)
            self.n_point = [n_front, self.ds_data["z"].values[row]]
        del self.ds_data
        return self.n_point

def n_calc(ds, method = "CoM", t = "", row_calc = "midrow"):
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

    for i,vals in enumerate(tqdm(tvals)):

        ds_data = ds.isel(t = vals)

        if method == "CoM":
            n_point = n_calc_methods(ds_data, "", n0_scale, Gridsize).CoM()
        elif method == "n_max":
            n_point = n_calc_methods(ds_data, row_calc, n0_scale, Gridsize).n_max()
        elif method == "n_front":
            n_point = n_calc_methods(ds_data, row_calc, n0_scale, Gridsize).n_front(FWHM=False)
        elif method == "n_front_FWHM":
            n_point = n_calc_methods(ds_data, row_calc, n0_scale, Gridsize).n_front(FWHM=True)

        if i == 0:
            n_array = [n_point]
        else:
            n_array = np.append(n_array, [n_point], axis = 0)
    del ds, ds_data  
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
    
    BOUT_res, BOUT_settings = data_import(folder = "delta_1_B0_0.1")[0:2]

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
    # n_array = n_calc(ds, method="n_front", row_calc="all_row")
    n_array_all = n_calc(ds, method="n_front_FWHM", row_calc="all_row")
    
    # dist_x, dist_z, vx, vz = vel_calc(n_array)
    dist_x_all, dist_z_all, vx_all, vz_all = vel_calc(n_array_all)

    # print(np.shape(n_array))
    title = "for n front with FWHM method"
    dist_array = [dist_x_all]
    vel_array = [vx_all]
    plot_label = ["for \nall row"]
    # print(np.max(vx))
    v_plot(ds["t"].values, dist_array, vel_array, plot_label=plot_label, title=title)

if __name__ == "__main__":
    main()