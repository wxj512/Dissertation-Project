import subprocess
from tqdm import tqdm
import numpy as np


path = "../../../../../Builds/BOUT++5.1.1/examples/blob2d/"

B0_inp = np.round(np.linspace(0.1, 1, 10), 2)

for i, val in enumerate(tqdm(B0_inp)):
    command = ["mpirun", "-n", "4", path + "./blob2d", "-d", path + "delta_1_B0_" + str(val)]

    result = subprocess.run(command, stdout=subprocess.PIPE)

    print(result.stdout.decode('utf-8'))

# print(B0_inp)