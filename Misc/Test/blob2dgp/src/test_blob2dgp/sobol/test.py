import pandas as pd
import xarray as xr
import numpy as np
from scipy.stats import sobol_indices, uniform

import test_blob2dgp.vel_out.v_data as v_data
import test_blob2dgp.GP.GP_regression as gpr

class sb_func:
    def __init__(self, gprfunc):
        self.gprfunc = gprfunc

    def v_func(self, x):
        x = np.transpose(x)
        gpfunc = self.gprfunc
        y_mean = gpfunc.predict(x).transpose()
        return y_mean
    

data_path = v_data.data_import("")[3]
data_input_path = data_path.joinpath("Output", "vel_max_avg", "campaign_2")
vall_df = pd.read_csv(data_input_path.joinpath("v_max.csv"), index_col=0)
print(vall_df.columns)