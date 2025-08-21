import re
import os
import pathlib
from xbout import open_boutdataset
import fileinput
import numpy as np
from tqdm import tqdm

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

def mk_inp(param_array, params, campaign_no, ref_folder = "delta_1", path = ""):

    if not(path == ""):
        run_path = path
    else:
        build_path = pathlib.Path(__file__).parents[8]
        build = "BOUT++5.1.1"
        # path = "../../../../../Builds/BOUT++5.1.1/examples/blob2d/"
        run_path = build_path.joinpath("Builds", build,"examples/blob2d")

    campaign = f"campaign_{campaign_no}"
    BOUT_res = run_path.joinpath(ref_folder, "BOUT.dmp.*.nc")
    BOUT_inp = run_path.joinpath(ref_folder, "BOUT.inp")
    ds_inp = open_boutdataset(BOUT_res, inputfilepath=BOUT_inp, info=False)
    inp_txt = ds_inp.attrs["options"]

    for i, val in enumerate(tqdm(param_array)):
        
        folder = "_".join(["delta_1"] + [f"{t[0]}_" + f"{t[1]:.1E}" for t in val.items()]) 
        filepath = run_path.joinpath(campaign, folder)
        
        if not(os.path.exists(filepath.parent) and os.path.isdir(filepath.parent)):
            os.mkdir(filepath.parent)
            
        if not(os.path.exists(filepath) and os.path.isdir(filepath)):
            os.mkdir(filepath)

        try:
            for p_var in params:
                if val[p_var] > 1e3 or val[p_var] < 1e-3:
                    inp_txt["model"][p_var] = f"{val[p_var]:.1E}"
                else:
                    inp_txt["model"][p_var] = f"{val[p_var]:.1f}"
            inp_file = filepath.joinpath("BOUT.inp")
            pathlib.Path.write_text(inp_file,str(inp_txt))
        except OSError:
            print("Error: no results file in ref folder, creating inp file by reading inp file")
            with fileinput.input(BOUT_inp) as inp, open(filepath.joinpath("BOUT.inp"), 'w') as inp_new:
                
                inp_new.seek(0)

                for j, line in enumerate(inp):
                    for p_vals in params:
                        if p_vals in line:
                            param_val = f"{val[p_vals]:.1f}"
                            line = re.sub(r"(=) (\d*\.*\d+)","= " + param_val, line)
                    inp_new.write(line)

def main():
    params = ["B0", "Te0", "L_par", "R_c"]
    min_max = np.array([[0.1, 3.2], [4, 40], [2.6e0, 1.3e2], [0.25, 0.9]])
    log = [False, False, True, False]
    # n_samples = [10, 10]
    parameters = param_gen(params, min_max)
    samples = 100
    grid_scan = epyscan.LatinHypercubeSampler(parameters).sample(samples)
    # [print(i) for i in grid_scan.sample(samples)]
    mk_inp(grid_scan, params, 3)


if __name__ == "__main__":
    main()