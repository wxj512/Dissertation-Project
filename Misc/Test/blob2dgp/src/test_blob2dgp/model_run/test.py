import pathlib
from xbout import open_boutdataset

build_path = pathlib.Path(__file__).parents[8]
build = "BOUT++5.1.1"
# path = "../../../../../Builds/BOUT++5.1.1/examples/blob2d/"
run_path = build_path.joinpath("Builds", build,"examples/blob2d")
camp = 1
camp_path = run_path.joinpath(f"campaign_{camp}")
f = camp_path.glob("*")
folders = []
folders = [str(obj) for obj in camp_path.glob("*")]
print(folders)