import subprocess
import pathlib
from tqdm import tqdm
import numpy as np

def main(path = ""):
    if not(path == ""):
        run_path = path
    else:
        build_path = pathlib.Path(__file__).parents[8]
        build = "BOUT++5.1.1"
        # path = "../../../../../Builds/BOUT++5.1.1/examples/blob2d/"
        run_path = build_path.joinpath("Builds", build,"examples/blob2d")

    B0_inp = np.linspace(0.1, 1, 10)

    for i, val in enumerate(tqdm(B0_inp)):
        command = ["mpirun", "-n", "4", str(run_path) + "/blob2d", "-d", str(run_path) + f"/delta_1_B0_{val:.1f}"]

        result = subprocess.run(command, stdout=subprocess.PIPE, text=True)

        print(result.stdout)

if __name__ == "__main__":
    main()

# print(B0_inp)