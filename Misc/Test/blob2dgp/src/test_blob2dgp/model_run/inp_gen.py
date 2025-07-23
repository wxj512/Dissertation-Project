import re
import os
import pathlib
from xbout import open_boutdataset
import fileinput
import numpy as np
import epyscan

def param_gen(params: str, min_max, n_samples = None, log = None, endpoint = None):
## Parameter generation for epyscan gridscan or latinhypercube

## min_max in the form of np array:
## For param a,b: min_max = [[min(a), max(a)], [min(b), max(b)]]
    parameters = {}
    for i, p_val in enumerate(params):
        parameters.update({
            p_val: {"min": min_max[i][0], "max": min_max[i][1]}
        })

        if n_samples is not None and isinstance(n_samples[i], int) == True:
            parameters[p_val].update({"n_samples": n_samples[i]})

        if log is not None and log[i] == True:
            parameters[p_val].update({"log": True})

        if endpoint is not None and endpoint[i] == False:
            parameters[p_val].update({"endpoint": False})
    return parameters

def mk_inp(param_array, params, ref_folder = "delta_1", path = "", campaign_no = 1):

    if not(path == ""):
        run_path = path
    else:
        build_path = pathlib.Path(__file__).parents[8]
        build = "BOUT++5.1.1"
        # path = "../../../../../Builds/BOUT++5.1.1/examples/blob2d/"
        run_path = build_path.joinpath("Builds", build,"examples/blob2d")

    for i, val in enumerate(param_array):
        campaign = f"campaign_{campaign_no}"
        folder = ["delta_1"] + [f"{t[0]}_" + f"{t[1]:.1f}" for t in val.items()] 
        folder = "_".join(folder)
        filepath = run_path.joinpath(campaign, folder)
        
        if not(os.path.exists(filepath.parent) and os.path.isdir(filepath.parent)):
            os.mkdir(filepath.parent)
        elif not(os.path.exists(filepath) and os.path.isdir(filepath)):
            os.mkdir(filepath)

        BOUT_res = filepath.parents[1].joinpath(ref_folder, "BOUT.dmp.*.nc")
        BOUT_inp = filepath.parents[1].joinpath(ref_folder, "BOUT.inp")
        
        try:
            ds_inp = open_boutdataset(BOUT_res, inputfilepath=BOUT_inp, info=False)
            inp_txt = ds_inp.attrs["options"]
            for p_var in params:
                inp_txt["model"][p_var] = f"{val[p_var]:.1f}"
            inp_file = filepath.joinpath("BOUT.inp")
            pathlib.Path.write_text(inp_file,str(inp_txt))
        except OSError:
            print("Error: no results file in ref folder, creating inp file by reading inp file")
            with fileinput.input(BOUT_inp) as inp, open(filepath.joinpath("BOUT.inp"), 'w') as inp_new:
                
                inp_new.seek(0)

                for j, line in enumerate(inp):
                    if params in line:
                        param_val = f"{val:.1f}"
                        line = re.sub(r"(=) (\d*\.*\d+)","= " + param_val, line)
                    inp_new.write(line)

def main():
    params = ["B0", "Te0"]
    min_max = np.array([[0.1, 1.0], [11, 20]])
    n_samples = [10, 10]
    parameters = param_gen(params, min_max, n_samples = n_samples)
    grid_scan = epyscan.GridScan(parameters)
    mk_inp(grid_scan, params)


if __name__ == "__main__":
    main()