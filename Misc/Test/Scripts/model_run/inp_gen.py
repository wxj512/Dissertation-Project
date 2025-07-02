import re
import os
import fileinput
import numpy as np

def mk_inp(param_array, ref_folder = "delta_1", path = ""):
    ref_folder = ref_folder

    if not(path == ""):
        path = path
    else:
        path = "../../../../../Builds/BOUT++5.1.1/examples/blob2d/"

    for i, val in enumerate(param_array):

        B0 = np.round(val, 2)

        filepath = path + ref_folder + "_B0_" + str(B0)

        if not(os.path.exists(filepath) and os.path.isdir(filepath)):
            os.mkdir(filepath)

        with fileinput.input(path + ref_folder + "/BOUT.inp") as inp, open(filepath + '/BOUT.inp', 'w') as inp_new:
            
            inp_new.seek(0)

            for j, line in enumerate(inp):
                if "B0" in line:
                    B0_val = str(B0)
                    line = re.sub(r"(=) (\d*\.*\d+)","= " + B0_val, line)
                inp_new.write(line)

if __name__ == "__main__":
    path = "../../../../../Builds/BOUT++5.1.1/examples/blob2d/"
    B0_inp = np.linspace(0.1, 1, 10)
    mk_inp(B0_inp, path=path)