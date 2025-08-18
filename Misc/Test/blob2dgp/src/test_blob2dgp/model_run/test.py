from git import Repo
from tqdm import tqdm
from xbout import open_boutdataset
import numpy as np
import test_blob2dgp.vel_out.v_data as v_data


def main():
    data_path = v_data.data_import("")[3]

    BOUT_res, BOUT_settings = v_data.data_import(folder = "delta_1")[0:2]

    ds = open_boutdataset(BOUT_res, inputfilepath=BOUT_settings, info=False)
    ds = ds.squeeze(drop=True)

    dx = ds["dx"].isel(x=0).values
    ds = ds.drop_vars("x")
    ds = ds.assign_coords(x=np.arange(ds.sizes["x"])*dx)

    print(ds["t"].values)
    # git_push()

if __name__ == "__main__":
    main()