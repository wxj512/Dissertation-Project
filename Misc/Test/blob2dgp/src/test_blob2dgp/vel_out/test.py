import os
from tqdm import tqdm
import numpy as np
from scipy.ndimage import sobel
from scipy.signal import find_peaks
# from skimage import feature
from xbout import open_boutdataset
import matplotlib.pyplot as plt
import pathlib


def data_import(_):
    folder = "delta_1_B0_" + "0.1"
    top_level_dir = pathlib.Path(__file__).parent.parent
    project_top_level = top_level_dir.parent.parent.parent
    filepath = str(project_top_level) + "/Data/Input/" + folder + "/"
    return filepath

filepath = data_import("")

# path = "../Data/Input/"
# folder = "delta_B0_" + "*.*"
# filepath = "../Data/Input/" + folder + "/"

# for i, [subdir, dirs, files] in enumerate(tqdm(os.walk(path))):
#     if "B0" in subdir:
#         print(subdir)

BOUT_inp = filepath + "BOUT.inp"
BOUT_res = filepath + "BOUT.dmp.*.nc"

ds = open_boutdataset(BOUT_res, info=False)
# ds = ds.squeeze(drop=True)

# dx = ds["dx"].isel(x=0).values
# ds = ds.drop_vars("x")
# ds = ds.assign_coords(x=np.arange(ds.sizes["x"])*dx)

# t = 50
# ds_data = ds.isel(t=t)

# fil = sobel(ds_data["n"].values - 1)
# # fil2 = feature.canny(ds_data["n"].values - 1, sigma=0.1)


# col = 141
# fil = fil.transpose()
# # fil2 = np.transpose(fil2)
# line = fil[:, int(col)]
# # line = fil2[:, int(col)]
# # print(line)
# # peaks, info = find_peaks(line, height=1e-04)
# f1 = plt.figure(1)
# ax1 = f1.gca()
# # ax1.plot(line)
# # ax1.set_xlim(0,256)
# ax1.imshow(fil, extent=[0,260,0,256])
# # ax1.scatter(peaks, line[peaks])
# # f2= plt.figure(2)
# # ax2 = f2.gca()
# # # ax2.imshow(fil2, extent=[0,260,0,256])
# # ax2.vlines(col,0,256)


# plt.show()