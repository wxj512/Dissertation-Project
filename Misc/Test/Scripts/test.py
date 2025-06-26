import numpy as np
from xbout import open_boutdataset
import matplotlib.pyplot as plt
from scipy import ndimage
from boututils import calculus as calc
from scipy.signal import find_peaks
from scipy.optimize import curve_fit


def data_import(_):
    folder = "delta_1"
    filepath = "../Data/Input/" + folder + "/"
    return filepath

def gaussian(x, *params):
	A = params[0]
	x0 = params[1]
	c = params[2]
	y0 = params[3]
	n = int(params[4])
	return y0 + A*np.exp(-((x-x0)/(np.sqrt(2)*c))**n)

def FWHM(c, n):
	FWHM = 2*np.sqrt(2)*(np.log(2)**(1/n))*c 
	return FWHM

filepath = data_import("")

BOUT_inp = filepath + "BOUT.inp"
BOUT_res = filepath + "BOUT.dmp.*.nc"

ds = open_boutdataset(BOUT_res, info=False)
ds = ds.squeeze(drop=True)

ds_data = ds.isel(t=20)
row = int(ds_data["z"].values.size/2)

def n_peak(n, height=0.02):
	peaks = find_peaks(n, height=0.02)

	if not(peaks[0].size > 0):
		max_peak = 0
		peak_2 = 0
	elif peaks[0].size == 1:
		max_peak = np.max(peaks[0])
		peak_2 = max_peak - (np.where(n>1e-02)[0][-1] - max_peak)
	else:
		max_peak = np.max(peaks[0])
		peak_2 = peaks[0][-2]

	return max_peak, peak_2

for j,z_vals in enumerate(ds_data["z"].values):
                
	n = ds_data["n"].values[:,j] - 1

	#Find peaks of rows
	max_peak, peak_2 = n_peak(n)
	
	# Makes sure this condition is fullfilled at j = 0
	if j == 0:
		max_peak_j = 0

	if max_peak == 0:
		continue
	
	if max_peak>max_peak_j:
		max_peak_j = max_peak
		row_j = j
	else:
		continue

width_guess = ((max_peak_j - peak_2)*0.5)*2
        

# peaks = find_peaks(n, height=0.02)
# max_peak = np.max(peaks[0])
# # print(max_peak - (np.where(n>1e-02)[0][-1] - max_peak))
# # print(n)
# if peaks[0].size == 1:
#     width_guess = ((np.where(n>1e-02)[0][-1] - max_peak)*0.5)*2
# else:
#     width_guess = ((max_peak - peaks[0][-2])*0.5)*2

x_array = np.linspace(0, n.size-1, n.size)
mask_n = np.ma.masked_outside(x_array,max_peak_j-(width_guess/2),max_peak_j+(width_guess/2))
mask_n = np.ones_like(mask_n)*n
mask_n[np.where(mask_n.data==1)[0]] = "nan"


guess = [n[max_peak_j], max_peak_j, 1, 0, 2]
bnd = ([-np.inf, -np.inf, -np.inf, -0.001, 2 - 0.1], [np.inf, np.inf, np.inf, 1e-03, 2 + 0.1])
popt, pcov = curve_fit(gaussian, x_array, mask_n, p0 = guess, bounds = bnd, nan_policy = 'omit')
gauss_fit = gaussian(x_array, *popt)
gauss_width = FWHM(popt[2], popt[4])
n_front = max_peak_j + (gauss_width / 2)
# # print(gauss_width)

f1 = plt.figure(1)
ax1 = f1.gca()
ax1.plot(gauss_fit)
ax1.plot(ds_data["n"].values[:,row_j]-1,linewidth=0.5)
ax1.set_ylim(-0.05, 1)
ax1.vlines(n_front, -0.05, 1, linestyles="--")
ax1.scatter([max_peak_j],[ds_data["n"].values[max_peak_j,row_j]-1],marker="x", color="black")


f2 = plt.figure(2)
ds_data["n"].plot(x="x",y="z")
plt.vlines(n_front, 0, max(ds_data["z"].values), linestyles="--", color = "orange")


plt.show()