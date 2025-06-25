import numpy as np
from xbout import open_boutdataset
import matplotlib.pyplot as plt
from scipy import ndimage
from boututils import calculus as calc
from scipy.signal import find_peaks

def data_import(_):
    folder = "delta_1"
    filepath = "../Data/Input/" + folder + "/"
    return filepath


filepath = data_import("")

BOUT_inp = filepath + "BOUT.inp"
BOUT_res = filepath + "BOUT.dmp.*.nc"

ds = open_boutdataset(BOUT_res, info=False)
ds = ds.squeeze(drop=True)

def n_calc(ds, Gridsize = 0.3, n0_scale = 1):
    
    for i,vals in enumerate(ds["t"].values):
        print(i)
        ds_data = ds.isel(t = i)

        for j,z_vals in enumerate(ds_data["z"].values):
            
            n = ds_data["n"].values[:,j]-1

            #Find peaks of rows
            peaks = find_peaks(n, height=0.05)
            
            if j == 0:
                max_peak_j = 0

            if not(peaks[0].size > 0):
                continue
            
            max_peak = np.max(peaks[0])
            
            if max_peak>max_peak_j:
                max_peak_j = max_peak
                row_j = j
            else:
                continue
            
            
        # Find furthest x value of grid of furthest n and return row of z with furthest n
        if i == 0:
            row = row_j
            max_x = max_peak_j
            f1 = plt.figure(1)
            ax1 = f1.gca()
            col = plt.cm.plasma(np.linspace(0,1,ds["t"].values.size))
        else:
            row = np.append(row, row_j)
            max_x = np.append(max_x, max_peak_j)
            n = ds_data["n"].values[:,row_j]-n0_scale

        ax1.plot(n, linewidth=0.5)
        ax1.scatter(max_peak_j, n[max_peak_j], color = "orange", marker = "x")
    
    return f1, row, max_x


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

n_plot, row, max_x = n_calc(ds)

print(max_x)

plt.show()