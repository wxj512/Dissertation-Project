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

ds_data = ds.isel(t=50)
row = int(ds_data["z"].values.size/2)
n = ds_data["n"].values[:,row]-1
peaks = find_peaks(n, height=0)
max_peak = np.max(peaks[0])
print(ds_data["n"].values.shape)

# f1 = plt.figure(1)
# ax1 = f1.gca()
# ax1.plot(n,linewidth=0.5)
# ax1.scatter(max_peak,n[max_peak],marker="x", color="orange")


# f2 = plt.figure(2)
# ds_data["n"].plot(x="x",y="z")


plt.show()