import re
import os
import xarray as xr
import numpy as np
import pandas as pd


array = np.append([np.linspace(0.1, 1, 10)], [np.linspace(10, 100, 10)],axis=0).transpose()

ds = pd.DataFrame(array,columns = ["B0", "Te0"])
print(ds.columns.size)