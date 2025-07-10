import re
import os
import xarray as xr
import numpy as np
import pandas as pd
from test_blob2dgp.vel_out import v_data

filepath = v_data.data_import("")
print(filepath)