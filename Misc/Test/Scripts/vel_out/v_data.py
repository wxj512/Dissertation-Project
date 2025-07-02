import numpy as np
from xbout import open_boutdataset
import matplotlib.pyplot as plt
from scipy import ndimage
from boututils import calculus as calc
from tqdm import tqdm


def data_import(_):
    folder = "delta_1"
    filepath = "../Data/Input/" + folder + "/"
    return filepath

class consts:
# With reference to blob2d.cxx file
    def __init__(self,BOUT_inp = ""):
        self.m_i = 2 * 1.667e-27 # Ion mass [kg]
        self.m_e = 9.11e-31      # Electron mass [kg]
        self.e = 1.602e-19       # Electron charge [C]
        self.B0 = 0.35           # Constant magnetic field [T]
        if not(BOUT_inp == ""):
            ds_inp = open(BOUT_inp).readlines()
            for i,line in enumerate(ds_inp):
                if "Te0" in line:
                    self.Te0 = float(line.split("=")[-1].strip().split()[0])
                if "n0" in line:
                    self.n0 = float(line.split("=")[-1].strip().split()[0])
                if "size of perturbation" and "[n]" in line:
                    line = open(BOUT_inp).readlines()[i+1]
                    self.n0_scale = float(line.split("=")[-1].strip().split()[0])
                if "Grid spacing" in line:
                    self.Gridsize = float(line.split("=")[-1].strip().split()[0])
        else:
            self.Te0 = 30            # Isothermal temperature [eV]
            self.n0 = 1e19           # Background density [m^-3]

def n_calc(ds, Gridsize = 0.3, n0_scale = 1, BOUT_inp = "", method = "CoM", t=""):
        if not(BOUT_inp == ""):
            n0_scale = consts(BOUT_inp).n0_scale
            Gridsize = consts(BOUT_inp).Gridsize

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
    

if __name__ == "__main__":
    filepath = data_import("")

    BOUT_inp = filepath + "BOUT.inp"
    BOUT_res = filepath + "BOUT.dmp.*.nc"

    ds = open_boutdataset(BOUT_res, info=False)
    ds = ds.squeeze(drop=True)

    dx = ds["dx"].isel(x=0).values
    ds = ds.drop_vars("x")
    ds = ds.assign_coords(x=np.arange(ds.sizes["x"])*dx)

    n_array = n_calc(ds, BOUT_inp=BOUT_inp)

    dist_x, dist_z, vx, vz = vel_calc(n_array)

    dist_array = [dist_x]
    vel_array = [vx]
    print(np.max(vx))
    v_plot(ds["t"].values, dist_array, vel_array)