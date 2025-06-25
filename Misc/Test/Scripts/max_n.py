import numpy as np
from xbout import open_boutdataset
import matplotlib.pyplot as plt
from scipy import ndimage
from boututils import calculus as calc

def data_import(_):
    folder = "delta_1"
    filepath = "../Data/Input/" + folder + "/"
    return filepath

def n_calc(ds, Gridsize = 0.3, n0_scale = 1):
    # Time value set for every 10 t
    for i,vals in enumerate(np.linspace(0,ds["t"].values.size-1,int(ds["t"].values.size/10)+1)):

        ds_data = ds.isel(t = int(vals))

        # Find max n value of grid and return row of max n
        row = np.where(ds_data["n"].values==np.max(ds_data["n"].values))[1]

        n = ds_data["n"].values[:,int(row[0])]-n0_scale

        if i == 0:
            f1 = plt.figure(1)
            ax1 = f1.gca()
            col = plt.cm.plasma(np.linspace(0,1,ds["t"].values.size))
        
        ax1.plot(n, label = "t="+str(vals), linewidth=0.5)
    ax1.legend()

filepath = data_import("")

BOUT_inp = filepath + "BOUT.inp"
BOUT_res = filepath + "BOUT.dmp.*.nc"

ds = open_boutdataset(BOUT_res, info=False)
ds = ds.squeeze(drop=True)

nplot = n_calc(ds)

f2 = plt.figure(2)
ds_data = ds.isel(t=0)
ds_data["n"].plot(x="x",y="z")


plt.show()