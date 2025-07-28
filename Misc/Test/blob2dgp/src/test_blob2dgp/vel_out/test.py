import pathlib
import sys
import numpy as np
from xbout import open_boutdataset
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
from tqdm import tqdm
import xarray as xr
from operator import itemgetter

import v_data


ax = np.array([[1,1,2,2,3,3,4,4,5,5], [1,2,1,2,1,2,1,2,1,2]]).transpose()
a = np.array([[2,2,2], [3,3,3], [5,5,5], [1,1,1], [4,4,4], [8,8,8], [6,6,6], [7,7,7], [9,9,9], [10,10,10]])
np.random.shuffle(ax)

temp = np.empty((0,10))
temp = [np.append(temp, ax[:,col]) for col in np.arange(ax.shape[1])[::-1]]

print(temp)
ax_sort = np.lexsort(temp,axis=0)

print(ax)
ax = ax[ax_sort]
print(ax)



