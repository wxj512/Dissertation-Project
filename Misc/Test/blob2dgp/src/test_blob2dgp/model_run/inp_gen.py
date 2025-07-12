import re
import os
import pathlib
from xbout import open_boutdataset
import fileinput
import numpy as np

import test_blob2dgp.vel_out.v_data as v_data

def mk_inp(param_array, param, ref_folder = "delta_1", path = ""):
    ref_folder = ref_folder

    if not(path == ""):
        run_path = path
    else:
        build_path = pathlib.Path(__file__).parents[8]
        build = "BOUT++5.1.1"
        # path = "../../../../../Builds/BOUT++5.1.1/examples/blob2d/"
        run_path = build_path.joinpath("Builds", build,"examples/blob2d")

    for i, val in enumerate(param_array):

        folder = f"delta_1_B0_{val:.1f}"
        filepath = run_path.joinpath(folder)
        
        if not(os.path.exists(filepath) and os.path.isdir(filepath)):
            os.mkdir(filepath)

        BOUT_res = filepath.parent.joinpath(ref_folder, "BOUT.dmp.*.nc")
        BOUT_inp = filepath.parent.joinpath(ref_folder, "BOUT.inp")
        
        try:
            ds_inp = open_boutdataset(BOUT_res, inputfilepath=BOUT_inp, info=False)
            inp_txt = ds_inp.attrs["options"]
            inp_txt["model"][param] = f"{val:.1f}"
            inp_file = filepath.joinpath("BOUT.inp")
            pathlib.Path.write_text(inp_file,str(inp_txt))
        except OSError:
            print("Error: no results file in ref folder, creating inp file by reading inp file")
            with fileinput.input(BOUT_inp) as inp, open(filepath.joinpath("BOUT.inp"), 'w') as inp_new:
                
                inp_new.seek(0)

                for j, line in enumerate(inp):
                    if param in line:
                        param_val = f"{val:.1f}"
                        line = re.sub(r"(=) (\d*\.*\d+)","= " + param_val, line)
                    inp_new.write(line)

if __name__ == "__main__":
    B0_inp = np.linspace(1.1, 2, 10)
    mk_inp(B0_inp, "B0")