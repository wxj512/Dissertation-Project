import os
from tqdm import tqdm
import numpy as np


# def data_import(_):
#     folder = "delta_B0_" + "*"
#     filepath = "../Data/Input/" + folder + "/"
#     return filepath

# filepath = data_import("")

path = "../Data/Input/"
folder = "delta_B0_" + "*.*"
filepath = "../Data/Input/" + folder + "/"

# for i, [subdir, dirs, files] in enumerate(tqdm(os.walk(path))):
#     if "B0" in subdir:
#         print(subdir)

B0_data = np.round(np.linspace(0.1,1,10),2)
print(B0_data)

