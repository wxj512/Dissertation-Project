import numpy as np
from xbout import open_boutdataset
import matplotlib.pyplot as plt
from scipy import ndimage
from boututils import calculus as calc
from tqdm import tqdm

import v_data


def n_calc(ds, n0_scale = 1, row_calc = "midplane", t = ""):
    
    # Find max n value of grid and return position (x,z) of max n
    def n_max(n, n0_scale, row = ""):
        n_max_pos = np.where((n - n0_scale) == np.max(n - n0_scale))

        if row == "":
            n_max_pos = [int(n_max_pos[0][0]), int(n_max_pos[1][0])]
        else:
            n_max_pos = [int(n_max_pos[0][0]), int(row)]
        
        return n_max_pos

    if t == "":
        tvals = np.linspace(0, ds["t"].shape[0]-1, ds["t"].shape[0], dtype = int)
    else:
        tvals = t

    for i,vals in enumerate(tqdm(tvals)):
        
        ds_data = ds.isel(t = vals)
        
        if row_calc == "midplane":
            row = int(ds_data["z"].size/2)
            n = ds_data["n"].values[:, row]
            n_max_pos = n_max(n, n0_scale, row)
        elif row_calc == "all_row":
            n = ds_data["n"].values
            n_max_pos = n_max(n, n0_scale)

        # n = ds_data["n"].values[:,int(row[0])]-n0_scale

        if i == 0:
            n_array = [n_max_pos]
        else:
            n_array = np.append(n_array, [n_max_pos], axis = 0)
    #         f1 = plt.figure(1)
    #         ax1 = f1.gca()
        
    #     ax1.plot(n, label = "t="+str(vals), linewidth=0.5)
    # ax1.legend()
    return n_array

if __name__ == "__main__":

    filepath = v_data.data_import("")

    BOUT_inp = filepath + "BOUT.inp"
    BOUT_res = filepath + "BOUT.dmp.*.nc"

    ds = open_boutdataset(BOUT_res, info=False)
    ds = ds.squeeze(drop=True)

    n_array_all = n_calc(ds, row_calc = "all_row")
    n_array = n_calc(ds)
    dist_x_all, dist_z_all, vx_all, vz_all = v_data.vel_calc(n_array_all)
    dx, dz, vx, vz = v_data.vel_calc(n_array)

    title = "for max n method"
    dist_array = [dx, dist_z_all]
    vel_array = [vx, vx_all]
    plot_label = ["for \nmid row", "for \nall rows"]

    f1 = v_data.v_plot(ds["t"].values, dist_array, vel_array, plot_label=plot_label, title=title)

    # t = 30

    # f1 = plt.figure(1)
    # ax1 = f1.gca()
    # ds_data = ds.isel(t=t)
    # ds_data["n"].plot(x="x",y="z")
    # ax1.scatter(n_array[t,0], n_array[t,1], marker = "x", color = "orange")

    # plt.show()



