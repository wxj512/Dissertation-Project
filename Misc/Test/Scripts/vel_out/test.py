import numpy as np
from xbout import open_boutdataset
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from scipy import ndimage
from boututils import calculus as calc
from scipy.signal import find_peaks
from scipy.optimize import curve_fit


def data_import(_):
    folder = "delta_1"
    filepath = "../Data/Input/" + folder + "/"
    return filepath

filepath = data_import("")

BOUT_inp = filepath + "BOUT.inp"
BOUT_res = filepath + "BOUT.dmp.*.nc"

ds = open_boutdataset(BOUT_res, info=False)
ds = ds.squeeze(drop=True)

n_hmap_ani = ds["n"].bout.animate2D(cmap=plt.cm.plasma)


plt.show()