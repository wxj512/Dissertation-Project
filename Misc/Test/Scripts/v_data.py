import numpy as np
from xbout import open_boutdataset
import matplotlib.pyplot as plt
from scipy import ndimage
from boututils import calculus as calc

def data_import(_):
    folder = "delta_1"
    filepath = "../Data/Input/" + folder + "/"
    return filepath

def CoM_calc(ds, Gridsize=0.3):
        for i,vals in enumerate(ds["t"].values):

            ds_data = ds.isel(t=i)
            CoM = np.array([ndimage.center_of_mass(ds_data["n"].values-1)])*Gridsize

            if i == 0:
                CoM_array = np.empty(CoM.size)
                CoM_array = CoM
            else:
                CoM_array = np.append(CoM_array, CoM, axis=0)
            

        return CoM_array

def vel_calc(array, mode):
    for i,vals in enumerate(array):
    
        if i == np.shape(array)[0] - 1:
            break
             
        p1 = array[i,:]
        p2 = array[i+1,:]
        dist = np.linalg.norm(p2 - p1)
        
        if i == 0:
            dist_array = np.zeros(1)
        
        dist_array = np.append(dist_array,dist)
        
    vel_array = np.gradient(dist_array)
        
    if mode == "vx" or "full":
        vx = np.gradient(np.gradient(array[:,0]))
        vz = np.gradient(np.gradient(array[:,1]))
        return dist_array, vel_array, vx, vz
    else:
        return dist_array, vel_array

    

def v_plot(time_array, dist_array, vel_array):
    f1 = plt.figure(1)
    ax1 = f1.gca()
    ax1.set_title("Distance and velocity of blob")
    ax1.plot(time_array, dist_array, label="Distance")
    ax1.plot(time_array, vel_array, label="Velocity")
    ax1.legend()
    ax1.set_xlabel("Time")
    plt.show()

if __name__ == "__main__":
    filepath = data_import("")

    ds = open_boutdataset(filepath + "BOUT.dmp.*.nc", info=False)
    ds = ds.squeeze(drop=True)

    dx = ds["dx"].isel(x=0).values
    ds = ds.drop_vars("x")
    ds = ds.assign_coords(x=np.arange(ds.sizes["x"])*dx)

    CoM_array = CoM_calc(ds)

    dist_array, vel_array, vx, vz = vel_calc(CoM_array, "full")

    v_plot(ds["t"].values, dist_array, vel_array)