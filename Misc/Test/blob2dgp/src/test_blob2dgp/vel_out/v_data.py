import pathlib
import sys
import numpy as np
from xbout import open_boutdataset
import matplotlib.pyplot as plt
from scipy import ndimage
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

def n_calc(ds, method = "CoM", t = ""):
        n0_scale = consts(ds = ds).n0_scale
        Gridsize = consts(ds = ds).Gridsize

        if t == "":
            tvals = np.linspace(0, ds["t"].shape[0]-1, ds["t"].shape[0], dtype = int)
        else:
            tvals = t

        for i,vals in enumerate(tqdm(tvals)):

            ds_data = ds.isel(t = vals)

            if method == "CoM":
                n_point = np.array([ndimage.center_of_mass(ds_data["n"].values - n0_scale)]) * Gridsize

            if i == 0:
                n_array = np.empty(n_point.size)
                n_array = n_point
            else:
                n_array = np.append(n_array, n_point, axis = 0)
            
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
    n_array = n_calc(ds)

    dist_x, dist_z, vx, vz = vel_calc(n_array)

    # print(np.shape(n_array))

    dist_array = [dist_x]
    vel_array = [vx]
    # print(np.max(vx))
    v_plot(ds["t"].values, dist_array, vel_array)

if __name__ == "__main__":
    main()