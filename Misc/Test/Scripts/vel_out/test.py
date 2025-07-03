import os
from tqdm import tqdm
import numpy as np
from xbout import open_boutdataset
import matplotlib.pyplot as plt


def data_import(_):
    folder = "delta_1_B0_" + "1.0"
    filepath = "../Data/Input/" + folder + "/"
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
ds = ds.squeeze(drop=True)

# dx = ds["dx"].isel(x=0).values
# ds = ds.drop_vars("x")
# ds = ds.assign_coords(x=np.arange(ds.sizes["x"])*dx)

ds["n"].bout.animate2D()

plt.show()