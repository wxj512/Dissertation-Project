import os
import numpy as np
from xbout import open_boutdataset
import pandas as pd
import xarray as xr
from natsort import natsorted
# import fnmatch
# from tqdm import tqdm
import matplotlib.pyplot as plt

import v_data

def v_all_calc(param_var, n_calc_method = ["CoM"], data_path = None, campaign_no = None, folder_list = None):
    if data_path == None:  
        data_path = v_data.data_import()[3]
        data_input_path = data_path.joinpath("Input")
        if campaign_no != None:
            data_input_path = data_input_path.joinpath(f"campaign_{campaign_no}")

    n_calc_method_no = len(n_calc_method)
    v_max_array = np.empty((0, n_calc_method_no))
    v_avg_array = np.empty((0, n_calc_method_no))
    parval_array = np.empty((0, len(param_var)))
    params = {}
    
    if folder_list == None:
        folder_list = natsorted([folder.name for folder in data_input_path.glob("*/")])
    else:
        folder_list = natsorted(folder_list)
    
    total = len(list(folder_list))
    
    for file_i, folder in enumerate(folder_list):
        print(f"Processing {file_i + 1} of {total}")
        print(f"Folder: {folder}")

        if campaign_no != None:
            folder = f"campaign_{campaign_no}/" + folder
             
        BOUT_res, BOUT_settings = v_data.data_import(folder = folder)[0:2]

        with open_boutdataset(BOUT_res, inputfilepath = BOUT_settings, info = False) as ds:
            ds = ds.squeeze(drop=True)
            Gridsize = v_data.consts(ds).Gridsize
            # dx = ds["dx"].isel(x = 0).values
            ds = ds.drop_vars("x")
            ds = ds.assign_coords(x = np.arange(ds.copy().sizes["x"]) * Gridsize)

            param_val = np.array([[ds.copy().attrs["options"]["model"][var]] for var in param_var]).transpose()
            
            n_vel_dict = {}
            v_max = np.empty((1, 0))
            v_avg = np.empty((1, 0))

            for method in n_calc_method:
                n_vel_dict.update({f"n_array_{method}": v_data.n_calc(ds, method = method, row_calc = "all_row")})
                n_vel_dict.update({f"vx_{method}": v_data.vel_calc(ds, n_vel_dict[f"n_array_{method}"])[2]})
                v_max = np.append(v_max, [[n_vel_dict[f"vx_{method}"].max()]], axis = 1)
                v_avg = np.append(v_avg, [[n_vel_dict[f"vx_{method}"].mean()]], axis = 1)
            # n_array_CoM = v_data.n_calc(ds, method = "CoM")
            # n_array_nf = v_data.n_calc(ds, method = "n_front")
            # n_array_nf_all = v_data.n_calc(ds, method = "n_front", row_calc = "all_row")
            # n_array_FWHM_all = v_data.n_calc(ds, method = "n_front_FWHM", row_calc = "all_row")

        # vx_CoM = v_data.vel_calc(ds, n_array_CoM)[2]
        # vx_nf = v_data.vel_calc(ds, n_array_nf)[2]
        # vx_nf_all = v_data.vel_calc(ds, n_array_nf_all)[2]
        # vx_FWHM_all = v_data.vel_calc(ds, n_array_FWHM_all)[2]

        # v_max = np.array([[np.max(vx_CoM)], [np.max(vx_nf_all)], [np.max(vx_FWHM_all)]]).transpose()
        # v_avg = np.array([[np.mean(vx_CoM)], [np.mean(vx_nf_all)], [np.mean(vx_FWHM_all)]]).transpose()
        # print(v_max, v_max_dict)
        v_max_array = np.append(v_max_array, v_max, axis = 0)
        v_avg_array = np.append(v_avg_array, v_avg, axis = 0)
        parval_array = np.append(parval_array, param_val, axis = 0)
    
    parval_split = np.empty((0,parval_array.shape[0]))
    parval_split = [np.append(parval_split, parval_array[:,col]) for col in np.arange(parval_array.shape[1])[::-1]]
    parval_sort = np.lexsort(parval_split,axis=0)
    
    parval_array = parval_array[parval_sort] 
    v_max_array = v_max_array[parval_sort] 
    v_avg_array = v_avg_array[parval_sort]

    [params.update({f"{var}": parval_array[:, param_var.index(var)]}) for var in param_var]
    return v_max_array, v_avg_array, parval_array, params

def write_nc(v_max_array, v_avg_array, param_var, params, data_path, n_calc_method, campaign_no = None, output_folder = None):
    ## Only usable in gridscan situations where data can be arranged into dimensions equally

    v_all_reshape = [np.unique(params[var]).size for var in param_var if np.unique(params[var]).size != 1] + [len(n_calc_method)]
    v_all_param = dict([(var, np.unique(params[var])) for var in param_var] + [("n_method", n_calc_method)])
    
    ## For checking if parameter variables specified matches parameters changed
    assert len(param_var) == len(v_all_reshape) - 1, "parameters not matching specification, check data input parameters changed"

    v_max_array = np.reshape(v_max_array, v_all_reshape)
    v_avg_array = np.reshape(v_avg_array, v_all_reshape)

    vmax_da = xr.DataArray(v_max_array, coords = v_all_param, attrs = {"long_name": "maximum velocity", "units": "c_s"})
    vavg_da = xr.DataArray(v_avg_array, coords = v_all_param, attrs = {"long_name": "average velocity", "units": "c_s"})

    param_attrs = {
        "B0": {"long_name": "magnetic field", "units": "T"},
        "Te0": {"long_name": "electron temperature", "units": "eV"},
        "n0": {"long_name": "background plasma density", "units": "m^-3"},
        "R_c": {"long_name": "radius of curvature", "units": "m"},
        "n_method": {"long_name": "density calculation method"},
    }

    v_all_coords = dict(
        [(var, (var, v_all_param[var], param_attrs[var])) for var in param_var] + [("n_method",("n_method", v_all_param["n_method"], param_attrs["n_method"]))]
    )

    v_all_ds = xr.Dataset(
        data_vars = {
            "v_max": vmax_da,
            "v_avg": vavg_da
        },

        coords = v_all_coords
    )

    if campaign_no != None:
        output_folder = f"campaign_{campaign_no}"
    try:
        output_path = data_path.joinpath("Output", "vel_max_avg", output_folder)
    except:
         "Check if campaign number specified or output_folder = None"

    if not(os.path.exists(output_path) and os.path.isdir(output_path)):
            os.mkdir(output_path)

    v_all_ds.to_netcdf(output_path.joinpath("v_all.nc"))

def write_csv(v_max_array, v_avg_array, param_var, parval_array, data_path, n_calc_method, campaign_no = None, output_folder = None):

    vmax_df = pd.DataFrame(v_max_array, columns = n_calc_method)
    vavg_df = pd.DataFrame(v_avg_array, columns = n_calc_method)
    parval_df = pd.DataFrame(parval_array, columns = param_var)

    vmax_df = pd.concat((vmax_df, parval_df), axis = 1)
    vavg_df = pd.concat((vavg_df, parval_df), axis = 1)

    if campaign_no != None:
        output_folder = f"campaign_{campaign_no}"
    try:
        output_path = data_path.joinpath("Output", "vel_max_avg", output_folder)
    except:
         "Check if campaign number specified or output_folder = None"

    if not(os.path.exists(output_path) and os.path.isdir(output_path)):
            os.mkdir(output_path)

    vmax_df.to_csv(output_path.joinpath("v_max.csv"))
    vavg_df.to_csv(output_path.joinpath("v_avg.csv"))

def main(): 
    data_path = v_data.data_import("")[3]
    # data_input_path = data_path.joinpath("Input")
    
    param_var = ["B0", "Te0", "L_par", "R_c"]   ## Check what parameters was changed for data to specify param_var
    # B0_data = np.round(np.linspace(0.1,1,10),2)

    # folder_list = [folder.name for folder in data_input_path.glob("*/") if fnmatch.fnmatch(folder.name, "delta_1_B0_*") == True]


    ## Specify at least folder_list or campaign_no
    n_calc_method = ["CoM", "n_front", "n_front_FWHM"]
    v_max_array, v_avg_array, parval_array, params = v_all_calc(param_var, n_calc_method = n_calc_method, campaign_no = 0)

    # write_nc(v_max_array, v_avg_array, param_var, params, data_path, n_calc_method, campaign_no = 2)
    write_csv(v_max_array, v_avg_array, param_var, parval_array, data_path, n_calc_method, campaign_no = 0)
    
    # f1 = plt.figure(linewidth = 3, edgecolor = "#000000")
    # ax1 = f1.gca()
    # ax1.set_title("Maximum velocity of blob for varying B0")
    # ax1.plot(B0_data, v_max_array[:,0], label = "CoM method")
    # # ax1.plot(B0_data, v_max_array[:,1], label = "n front method \nfor mid row")
    # ax1.plot(B0_data, v_max_array[:,1], label = "n front method \nfor all row")
    # ax1.plot(B0_data, v_max_array[:,2], label = "n front + FWHM \nmethod for all row")
    # ax1.set_xlabel("B0/T")
    # ax1.set_ylabel("$v_{max}$/$c_s$")
    # ax1.legend()

    # f2 = plt.figure(linewidth = 3, edgecolor = "#000000")
    # ax2 = f2.gca()
    # ax2.set_title("Average velocity of blob for varying B0")
    # ax2.plot(B0_data, v_avg_array[:,0], label = "CoM method")
    # # ax2.plot(B0_data, v_avg_array[:,1], label = "n front method \nfor mid row")
    # ax2.plot(B0_data, v_avg_array[:,1], label = "n front method \nfor all row")
    # ax2.plot(B0_data, v_avg_array[:,2], label = "n front + FWHM \nmethod for all row")
    # ax2.set_xlabel("B0/T")
    # ax2.set_ylabel("$v_{avg}$/$c_s$")
    # ax2.legend()
    # plt.show()

if __name__ == "__main__":
    main()


    