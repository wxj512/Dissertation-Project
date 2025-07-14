import pathlib
import sys
import numpy as np
from xbout import open_boutdataset
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
from tqdm import tqdm
import xarray

import v_data



class n_calc_methods:
    
    def __init__(self, ds_data, row_calc, n0_scale, Gridsize):
        self.ds_data = ds_data
        self.row_calc = row_calc
        self.n0_scale = n0_scale
        self.Gridsize = Gridsize
        
    
    def n_array(self, row):
        if row == "whole_grid":
            self.n = self.ds_data["n"].values - self.n0_scale
        else:
            self.n = self.ds_data["n"].values[:,row] - self.n0_scale
        return self.n
    
    def CoM(self):
        self.n_point = np.array(ndimage.center_of_mass(self.n_array("whole_grid") - self.n0_scale)) * self.Gridsize
        return self.n_point
    
    def n_max(self):
        
        def n_max_pos(n, n0_scale, row = ""):
            n_max_pos = np.where((n - n0_scale) == np.max(n - n0_scale))
            if row == "":
                n_max_pos = [int(n_max_pos[0][0]), int(n_max_pos[1][0])]
            else:
                n_max_pos = [int(n_max_pos[0][0]), int(row)]
            return n_max_pos
        
        if self.row_calc == "midrow":
            row = int(self.ds_data["z"].shape[0]/2)
            self.n_point = n_max_pos(self.n_array(row), self.n0_scale, row = row)
        elif self.row_calc == "all_row":
            self.n_point = n_max_pos(self.n_array("whole_grid"), self.n0_scale)
        return self.n_point
        
    def n_front(self, FWHM = False):
        
        def n_peak(n, height=0.005):
            peaks = find_peaks(n, height=height)
            if not(peaks[0].size > 0):
                max_peak = 0
                peak_2 = 0
            elif peaks[0].size == 1:
                max_peak = np.max(peaks[0])
                peak_2 = max_peak - (np.where(n > 0.0001 * n[max_peak])[0][-1] - max_peak)
            else:
                max_peak = np.max(peaks[0])
                peak_2 = peaks[0][-2]
            return max_peak, peak_2
        
        if self.row_calc == "midrow":
            row = int(self.ds_data["z"].shape[0]/2)
            max_peak_j, peak_2_j = n_peak(self.n_array(row))
            peak_n = self.n_array(row)
        elif self.row_calc == "all_row":
            for j,z_vals in enumerate(self.ds_data["z"].values):
                        #Find peaks of rows
                        max_peak, peak_2 = n_peak(self.n_array(j))
                        # Makes sure this condition is fullfilled at j = 0
                        if j == 0:
                            max_peak_j = 0
                            peak_2_j = 0
                        elif max_peak == 0:
                            continue
                        elif max_peak>max_peak_j:
                            max_peak_j = max_peak
                            row = j
                            peak_2_j = peak_2
                            peak_n = self.n_array(row)
                        else:
                            continue
        
        if FWHM == False:
            self.n_point = [self.ds_data["x"].values[max_peak_j], self.ds_data["z"].values[row]]
        elif FWHM == True:

            def gaussian(x, *params):
                A = params[0]
                x0 = params[1]
                c = params[2]
                return A * np.exp(-((x - x0)/(np.sqrt(2) * c)) ** 2)

            def FWHM(c):
                FWHM = 2 * np.sqrt(2) * (np.log(2) ** (1/2)) * c 
                return FWHM
            
            #   Mask data
            width_guess = ((max_peak_j - peak_2_j) * 0.5) * 2
            x_array = np.linspace(0, peak_n.size-1, peak_n.size)
            mask_n = np.ma.masked_outside(x_array, max_peak_j - (width_guess / 2), max_peak_j + (width_guess / 2))
            mask_n = np.ones_like(mask_n) * peak_n
            mask_n[np.where(mask_n.data == 1)[0]] = "nan"
            # Find gaussian
            guess = [peak_n[max_peak_j], max_peak_j * self.Gridsize, 1 / (peak_n[max_peak_j] * np.sqrt(2 * np.pi))]
            bnd = ([-np.inf, -np.inf, 0], [np.inf, np.inf, np.inf])
            popt, pcov = curve_fit(gaussian, x_array * self.Gridsize, mask_n, p0 = guess, nan_policy = 'omit', bounds = bnd)
            gauss_fit = gaussian(x_array * self.Gridsize, *popt)
            gauss_width = FWHM(popt[2])
            n_front = max_peak_j * self.Gridsize + (gauss_width / 2)
            self.n_point = [n_front, self.ds_data["z"].values[row]]

        return self.n_point, gauss_fit, row


BOUT_res, BOUT_settings = v_data.data_import(folder = "delta_1_B0_0.1")[0:2]

ds = open_boutdataset(BOUT_res, inputfilepath=BOUT_settings, info=False)
ds = ds.squeeze(drop=True)

dx = ds["dx"].isel(x=0).values
ds = ds.drop_vars("x")
ds = ds.assign_coords(x=np.arange(ds.sizes["x"])*dx)

ds_data = ds.isel(t=50)
del ds
print(ds)