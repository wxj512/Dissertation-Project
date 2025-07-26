import os
import numpy as np
from xbout import open_boutdataset
import xarray as xr
from tqdm import tqdm
import matplotlib.pyplot as plt

import v_data

def v_all_calc(campaign_no, data_path = ""):
    if data_path == "":  
        data_path = v_data.data_import("")[3]
        data_input_path = data_path.joinpath("Input", f"campaign_{campaign_no}")

    param_var = ["B0", "Te0", "n0", "R_c"]
    v_max_array = np.empty(0)
    v_avg_array = np.empty(0)
    parval_array = np.empty((0, len(param_var)))
    params = {}

    for file_i, folder in enumerate(tqdm(data_input_path.glob("*/"), total = len(list(data_input_path.glob("*/"))))):

        BOUT_res, BOUT_settings = v_data.data_import(folder = folder)[0:2]

        ds = open_boutdataset(BOUT_res, inputfilepath = BOUT_settings, info = False, grid_mismatch = "ignore")
        ds = ds.squeeze(drop=True)

        dx = ds["dx"].isel(x = 0).values
        ds = ds.drop_vars("x")
        ds = ds.assign_coords(x = np.arange(ds.sizes["x"])*dx)

        param_val = np.array([[ds.attrs["options"]["model"][var]] for var in param_var]).transpose()

        n_array_CoM = v_data.n_calc(ds, method = "CoM")
        # n_array_nf = v_data.n_calc(ds, method = "n_front")
        # n_array_nf_all =v_data.n_calc(ds, method = "n_front", row_calc = "all_row")
        # n_array_FWHM_all = v_data.n_calc(ds, method = "n_front_FWHM", row_calc = "all_row")

        dx_CoM, dz_CoM, vx_CoM, vz_CoM = v_data.vel_calc(n_array_CoM)
        # dx_nf, dz_nf, vx_nf, vz_nf = v_data.vel_calc(n_array_nf)
        # dx_nf_all, dz_nf_all, vx_nf_all, vz_nf_all = v_data.vel_calc(n_array_nf_all)
        # dx_FWHM_all, dz_FWHM_all, vx_FWHM_all, vz_FWHM_all = v_data.vel_calc(n_array_FWHM_all)

        v_max = np.array([[np.max(vx_CoM)]])
        v_avg = np.array([[np.mean(vx_CoM)]])
        v_max_array = np.append(v_max_array, [v_max])
        v_avg_array = np.append(v_avg_array, [v_avg])
        parval_array = np.append(parval_array, param_val, axis = 0)
        del ds
    
    [params.update({f"{var}": parval_array[:, param_var.index(var)]}) for var in param_var]
    return v_max_array, v_avg_array, params

def write_nc(v_max_array, v_avg_array, data_path, campaign_no):
    n_calc_method = ["CoM", "n_front mid row", "n_front all row", "n_front + FWHM all row"]
    B0_data = np.round(np.linspace(0.1,1,10),2)

    v_all_ds = xr.Dataset(
        data_vars = dict(
            v_max = (["B0", "n_method"], v_max_array, {"long_name": "maximum velocity", "units": "c_s"}),
            v_avg = (["B0", "n_method"], v_avg_array, {"long_name": "averagevelocity", "units": "c_s"})
        ),
        coords = dict(
            B0 = ("B0", B0_data, {"long_name": "magnetic field", "units": "T"}),
            n_method =  ("n_method", n_calc_method, {"long_name": "density calculation method"})
        ),
    )

    output_folder = f"campaign_{campaign_no}"
    output_path = data_path.joinpath("Output", "vel_max_avg", output_folder)

    if not(os.path.exists(output_path) and os.path.isdir(output_path)):
            os.mkdir(output_path)

    v_all_ds.to_netcdf(output_path.joinpath("v_all.nc"))

def main(): 
    data_path = v_data.data_import("")[3]
    B0_data = np.round(np.linspace(0.1,1,10),2)

    v_max_array, v_avg_array, params = v_all_calc(1)

    # write_nc(v_max_array, v_avg_array, data_path, 1)

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


    