import subprocess
from tqdm import tqdm
import numpy as np


path = "../../../../../Builds/BOUT++5.1.1/examples/blob2d/"

B0_inp = np.round(np.linspace(0.1, 1, 10), 2)

for i, val in enumerate(tqdm(B0_inp)):
    command = ["mpirun", "-n", "4", path + "./blob2d", "-d", path + f"delta_1_B0_{val:.2f}"]

    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)

    print(result.stdout)

# print(B0_inp)