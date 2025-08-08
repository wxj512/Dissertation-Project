import os
import numpy as np
from xbout import open_boutdataset
import xarray as xr
from natsort import natsorted
from tqdm import tqdm
# import matplotlib.pyplot as plt

import v_data

def v_all_calc(campaign_no, param_var, data_path = ""):
    if data_path == "":  
        data_path = v_data.data_import("")[3]
        data_input_path = data_path.joinpath("Input")
        if campaign_no != "":
            data_input_path = data_input_path.joinpath(f"campaign_{campaign_no}")

    v_max_array = np.empty((0, 3))
    v_avg_array = np.empty((0, 3))
    parval_array = np.empty((0, len(param_var)))
    params = {}
    total = len(list(data_input_path.glob("*/")))
    folder_list = natsorted([folder.name for folder in data_input_path.glob("*/")])
    
    for file_i, folder in enumerate(folder_list):
        print(f"Processing {file_i + 1} of {total}")
        print(f"Folder: {folder}")

        if campaign_no != "":
            folder = f"campaign_{campaign_no}/" + folder
             
        BOUT_res, BOUT_settings = v_data.data_import(folder = folder)[0:2]

        ds = open_boutdataset(BOUT_res, inputfilepath = BOUT_settings, info = False)
        ds = ds.squeeze(drop=True)

        dx = ds["dx"].isel(x = 0).values
        ds = ds.drop_vars("x")
        ds = ds.assign_coords(x = np.arange(ds.sizes["x"])*dx)

        param_val = np.array([[ds.attrs["options"]["model"][var]] for var in param_var]).transpose()

        n_array_CoM = v_data.n_calc(ds, method = "CoM")
        # n_array_nf = v_data.n_calc(ds, method = "n_front")
        n_array_nf_all = v_data.n_calc(ds, method = "n_front", row_calc = "all_row")
        n_array_FWHM_all = v_data.n_calc(ds, method = "n_front_FWHM", row_calc = "all_row")

        ds.close()

        vx_CoM = v_data.vel_calc(n_array_CoM)[2]
        # dx_nf, dz_nf, vx_nf, vz_nf = v_data.vel_calc(n_array_nf)
        vx_nf_all = v_data.vel_calc(n_array_nf_all)[2]
        vx_FWHM_all = v_data.vel_calc(n_array_FWHM_all)[2]

        v_max = np.array([[np.max(vx_CoM)], [np.max(vx_nf_all)], [np.max(vx_FWHM_all)]]).transpose()
        v_avg = np.array([[np.mean(vx_CoM)], [np.mean(vx_nf_all)], [np.mean(vx_FWHM_all)]]).transpose()
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
    return v_max_array, v_avg_array, params

def write_nc(v_max_array, v_avg_array, param_var, params, data_path, campaign_no):
    n_calc_method = ["CoM", "n_front_all", "FWHM_all"]

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

    output_folder = f"campaign_{campaign_no}"
    output_path = data_path.joinpath("Output", "vel_max_avg", output_folder)

    if not(os.path.exists(output_path) and os.path.isdir(output_path)):
            os.mkdir(output_path)

    v_all_ds.to_netcdf(output_path.joinpath("v_all.nc"))

def main(): 
    data_path = v_data.data_import("")[3]
    
    param_var = ["B0", "Te0", "n0", "R_c"]   ## Check what parameters was changed for data to specify param_var
    # B0_data = np.round(np.linspace(0.1,1,10),2)

    v_max_array, v_avg_array, params = v_all_calc(2, param_var)

    write_nc(v_max_array, v_avg_array, param_var, params, data_path, 2)

    # f1 = plt.figure(linewidth = 3, edgecolor = "#000000")
    # ax1 = f1.gca()
    # ax1.set_title("Maximum velocity of blob for varying B0")
    # ax1.plot(B0_data, v_max_array[:,0], label = "CoM method")
    # ax1.plot(B0_data, v_max_array[:,1], label = "n front method \nfor mid row")
    # ax1.plot(B0_data, v_max_array[:,2], label = "n front method \nfor all row")
    # ax1.plot(B0_data, v_max_array[:,3], label = "n front + FWHM \nmethod for all row")
    # ax1.set_xlabel("B0/T")
    # ax1.set_ylabel("$v_{max}$/$c_s$")
    # ax1.legend()

    # f2 = plt.figure(linewidth = 3, edgecolor = "#000000")
    # ax2 = f2.gca()
    # ax2.set_title("Average velocity of blob for varying B0")
    # ax2.plot(B0_data, v_avg_array[:,0], label = "CoM method")
    # ax2.plot(B0_data, v_avg_array[:,1], label = "n front method \nfor mid row")
    # ax2.plot(B0_data, v_avg_array[:,2], label = "n front method \nfor all row")
    # ax2.plot(B0_data, v_avg_array[:,3], label = "n front + FWHM \nmethod for all row")
    # ax2.set_xlabel("B0/T")
    # ax2.set_ylabel("$v_{avg}$/$c_s$")
    # ax2.legend()
    # plt.show()

if __name__ == "__main__":
    main()


    