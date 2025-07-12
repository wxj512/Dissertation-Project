import pathlib

build_path = pathlib.Path(__file__).parents[8]
build = "BOUT++5.1.1"
path = "../../../../../Builds/BOUT++5.1.1/examples/blob2d/"
run_path = build_path.joinpath("Builds", build,"examples/blob2d", " ")

print(str(run_path) + "./blob2d")

