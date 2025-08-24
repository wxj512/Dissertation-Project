import numpy as np
from xbout import open_boutdataset
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from scipy import ndimage
from boututils import calculus as calc
from scipy.signal import find_peaks
from scipy.optimize import curve_fit

import n_front
import n_front_FWHM
import max_n
import v_data

# Plot results on n heatmap for 6 subplots based on time, defined in t

def n_hmap_subplots(t, ds, res_array = None, plotstyle = "line", legend = None):
    f1 = plt.figure(1, linewidth = 3, edgecolor = "#000000", figsize=[6.9*1.8,4.8*1.8])
    # f1.suptitle("Comparison of n front at peak and FWHM for n at different t", fontsize = "large")
    # axs = f1.subplots(2, 3)
    axs = f1.subplot_mosaic([["a)","b)","c)"],["d)","e)","f)"]])
    f1.subplots_adjust(wspace=0.3,hspace=0.005, top = 0.9, left=0.05, bottom=0.01, right=0.92)


    for pos, items in enumerate(axs.items()):
        annotate = items[0]
        ax = items[1]
        tval = t[pos]
        vmin = ds["n"].values.min()
        vmax = ds["n"].values.max()
        n_hmap = ds.isel(t=tval)["n"].plot(x="x",y="z", ax=ax, vmin=vmin, vmax=vmax, cmap="plasma", add_colorbar=False)
        ax.set_title("t/(1/$\\Omega_i$) = " + str(tval*50), fontsize = "medium", fontweight="bold")
        ax.set_title(annotate, loc='left', fontsize='medium', fontweight="bold")
        ax.set_xlabel("x/$\\rho_s$")
        ax.set_ylabel("z/$\\rho_s$")
        if (pos - 2) % 3 == 0:
            cbax = ax.inset_axes([1.05, 0, 0.05, 1])
            f1.colorbar(n_hmap, cax=cbax, label="n/$n_0$")

        cmap = plt.cm.Pastel1.colors[:] 

        if res_array is not None and np.size(res_array > 0): 

            if pos == 0 and not(legend == None):
                legend = legend
            elif np.size(legend) > 1:
                legend = np.full(res_array.shape[1],"")
            else:
                legend = ""

            if plotstyle == "vline":
                if np.size(np.shape(res_array)) > 1:
                    for res in np.linspace(0, res_array.shape[1] - 1, res_array.shape[1]):
                        res = int(res)
                        ax.vlines(res_array[pos,res], 0, ds["z"].values.max(), linestyles="--", color = cmap[res], label=legend[res])
                elif np.size(np.shape(res_array)) == 1:
                    ax.vlines(res_array[pos], 0, ds["z"].values.max(), linestyles="--", color = cmap[0], label=legend)
            elif plotstyle == "scatter": 
                if np.shape(res_array)[1] > 2:
                    for res in np.linspace(0, res_array.shape[1] - 1, res_array.shape[1]):
                        res = int(res)
                        ax.scatter(res_array[pos,(2*res)], res_array[pos,(2*res)+1], marker="x", color = cmap[res], label=legend[res])
                        if res == (res_array.shape[1] / 2) - 1:
                            break
                elif np.shape(res_array)[1] == 2:
                    ax.scatter(res_array[pos,0], res_array[pos,1], marker="x", color = cmap[0], label=legend)
                    print(res_array[pos,0], res_array[pos,1])
            f1.legend(bbox_to_anchor = (0.97, 0.97), fontsize = "small") 
                            
        ax.set_box_aspect(1)

    
    plt.show()

def main():
    
    BOUT_res, BOUT_settings = v_data.data_import(folder = "delta_1")[0:2]

    ds = open_boutdataset(BOUT_res, inputfilepath=BOUT_settings, info=False)
    ds = ds.squeeze(drop=True)

    dx = ds["dx"].isel(x=0).values
    ds = ds.drop_vars("x")
    ds = ds.assign_coords(x=np.arange(ds.sizes["x"])*dx)

    t = [0, 10, 20, 30, 40, 50]

    ## n front
    n_array = v_data.n_calc(ds, t=t, row_calc="all_row", method="n_front")
    n_array_all = v_data.n_calc(ds, t=t, row_calc="all_row", method="n_front_FWHM")
    # n_array_FWHM = n_front_FWHM.n_calc(ds,t=t, row_calc="all_row")
    ## Max n
    # n_array = max_n.n_calc(ds, t=t)
    # n_array_all = max_n.n_calc(ds, t=t, row_calc="all_row")
    ## CoM
    # n_array = v_data.n_calc(ds, t=t)

    ## X-res_array, each coloumn for x-coords (vlines) or every 2 columns for x and z coords (scatter)
    ## For vline
    ## n front
    # For 1 results
    # res_array = n_array[:,0]
    # For 2 results 
    res_array = np.append(n_array[:,0],n_array_all[:,0]).reshape(n_array.shape[0],2, order="F")

    ## For scatter
    # ## Max n
    # n_array_res = np.vstack(([ds["x"].values[n_array[:,0]]],[ds["z"].values[n_array[:,1]]])).transpose()
    # n_array_all_res = np.append([ds["x"].values[n_array_all[:,0]]],[ds["z"].values[n_array_all[:,1]]], axis = 0).transpose()
    # res_array = np.append(n_array_res,n_array_all_res,axis=1)
    ## CoM
    # res_array = np.vstack((n_array[:,0], n_array[:,1])).transpose()
    legend = ["n front\nall row", "n front + FWHM\nall row"]
    n_hmap_subplots(t,ds, res_array = res_array, legend = legend, plotstyle = "vline")
    # print(ds["x"].interp(x=n_array[:,0]).values)

if __name__ == "__main__":
    main()
