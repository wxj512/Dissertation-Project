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
data_input_path = data_path.joinpath("Output", "vel_max_avg", "campaign_1")
vall_ds = xr.open_dataset(data_input_path.joinpath("v_all.nc"))
vmax_data = vall_ds["v_max"].sel(n_method = "CoM")
B0 = vall_ds["B0"].values
Te0 = vall_ds["Te0"].values
x2,x1 = np.meshgrid(Te0, B0)
x1v = x1.reshape(-1,1)
x2v = x2.reshape(-1,1)
X = np.column_stack((x1v.reshape(-1), x2v.reshape(-1)))
Z = np.empty(0)
Z = [np.append(Z,vmax_data.sel(B0=i, Te0=j)) for i,j in X]
Z = np.reshape(Z,(-1,1))
gprfunc = gpr.gp_reg(X, Z, return_GP=True)

sb_ind = sobol_indices(
    func = sb_func(gprfunc).v_func,
    n = 2**(10),
    dists = [
        uniform(loc = np.min(B0), scale = np.max(B0) - np.min(B0)),
        uniform(loc = np.min(Te0), scale = np.max(Te0) - np.min(Te0))
    ],
    rng = np.random.default_rng()
)

print(sb_ind.first_order)
print(sb_ind.total_order)

sb_boot = sb_ind.bootstrap()

print(sb_boot.first_order.confidence_interval.low, sb_boot.first_order.confidence_interval.high)
print(sb_boot.total_order.confidence_interval.low, sb_boot.total_order.confidence_interval.high)