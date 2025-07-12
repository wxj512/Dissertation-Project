import pathlib
from xbout import open_boutdataset

ref_folder = "delta_1"

build_path = pathlib.Path(__file__).parents[8]
build = "BOUT++5.1.1"
run_path = build_path.joinpath("Builds", build,"examples/blob2d")

folder = f"delta_1_B0_1.1"
filepath = run_path.joinpath(folder)

BOUT_res = filepath.parent.joinpath(ref_folder, "BOUT.dmp.*.nc")
BOUT_inp = filepath.parent.joinpath(ref_folder, "BOUT.inp")
val=1.1220
ds_inp = open_boutdataset(BOUT_res, inputfilepath=BOUT_inp, info=False)
file_txt = ds_inp.attrs["options"]
file_txt["model"]["B0"]=f"{val:.1f}"
file = filepath.joinpath("BOUT.inp")
pathlib.Path.write_text(file,str(file_txt))
print(file_txt)