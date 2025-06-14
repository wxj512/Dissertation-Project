import numpy as np
from xbout import open_boutdataset
import matplotlib.pyplot as plt
from scipy import ndimage

def data_import(_):
    folder = "delta_1"
    filepath = "../Data/Input/" + folder + "/"
    return filepath

def CoM_calc(ds):
        for i,vals in enumerate(ds["t"].values):

            ds_data = ds.isel(t=i)
            CoM = np.array([ndimage.center_of_mass(ds_data["n"].values-1)])*0.3

            if i == 0:
                CoM_array = np.empty(CoM.size)
                CoM_array = CoM
                continue
            
            CoM_array = np.append(CoM_array, CoM, axis=0)

        return CoM_array

def vel_calc(array):
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
        
    return dist_array, vel_array

if __name__ == "__main__":
    filepath = data_import("")

    ds = open_boutdataset(filepath + "BOUT.dmp.*.nc")
    ds = ds.squeeze(drop=True)

    dx = ds["dx"].isel(x=0).values
    ds = ds.drop_vars("x")
    ds = ds.assign_coords(x=np.arange(ds.sizes["x"])*dx)

    #ds_data["n"].plot(x="x", y="z")

    CoM_array = CoM_calc(ds)

    dist_array, vel_array = vel_calc(CoM_array)

    plt.plot(ds["t"].values, dist_array, ds["t"].values, vel_array)

    plt.show()