import numpy as np
from xbout import open_boutdataset
import matplotlib.pyplot as plt
from scipy import ndimage
from boututils import calculus as calc


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

def CoM_calc(ds, Gridsize = 0.3, n0_scale = 1, BOUT_inp = ""):
        if not(BOUT_inp == ""):
            n0_scale = consts(BOUT_inp).n0_scale
            Gridsize = consts(BOUT_inp).Gridsize

        for i,vals in enumerate(ds["t"].values):

            ds_data = ds.isel(t = i)
            CoM = np.array([ndimage.center_of_mass(ds_data["n"].values - n0_scale)]) * Gridsize

            if i == 0:
                CoM_array = np.empty(CoM.size)
                CoM_array = CoM
            else:
                CoM_array = np.append(CoM_array, CoM, axis = 0)
            
        return CoM_array

def vel_calc(array):
    for i,vals in enumerate(array):
    
        if i == np.shape(array)[0] - 1:
            break

        p1 = array[i,:]
        p2 = array[i+1,:]

        dist = p2 - p1
        
        if i == 0:
            dist_x = np.zeros(1)
            dist_z = np.zeros(1)
        
        dist_x = np.append(dist_x,dist[0])
        dist_z = np.append(dist_x,dist[1])
        
        vx = np.gradient(np.gradient(array[:,0]))
        vz = np.gradient(np.gradient(array[:,1]))

    return dist_x, dist_z, vx, vz


def v_plot(time_array, dist_array, vel_array):
    f1 = plt.figure(1, linewidth = 3, edgecolor = "#000000")
    ax1 = f1.gca()
    ax2 = ax1.twinx()
    col = plt.cm.plasma([0.1, 0.7])
    ax1.set_title("Distance and velocity of blob")
    ax1.plot(time_array, dist_array, label = "Distance", color = col[0])
    ax2.plot(time_array, vel_array, label = "Velocity", color = col[1])
    ax1.set_xlabel("Time/$\\Omega_i$")
    ax1.set_ylabel("Distance/$\\rho_s$")
    ax2.set_ylabel("Velocity/$c_s$")
    f1.tight_layout()
    f1.legend(loc='upper right', bbox_to_anchor=(0.85, 0.9))
    plt.show()

if __name__ == "__main__":
    filepath = data_import("")

    BOUT_inp = filepath + "BOUT.inp"
    BOUT_res = filepath + "BOUT.dmp.*.nc"

    ds = open_boutdataset(BOUT_res, info=False)
    ds = ds.squeeze(drop=True)

    dx = ds["dx"].isel(x=0).values
    ds = ds.drop_vars("x")
    ds = ds.assign_coords(x=np.arange(ds.sizes["x"])*dx)

    CoM_array = CoM_calc(ds, BOUT_inp=BOUT_inp)

    dist_x, dist_z, vx, vz = vel_calc(CoM_array)

    v_plot(ds["t"].values, dist_x, vx)