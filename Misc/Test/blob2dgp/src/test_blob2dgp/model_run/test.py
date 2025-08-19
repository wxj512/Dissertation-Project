from git import Repo
from tqdm import tqdm
from xbout import open_boutdataset
import numpy as np
from scipy.stats import norm
import test_blob2dgp.vel_out.v_data as v_data


def main():
    conf_level = 0.95
    Z = norm.ppf(0.5 + conf_level / 2)
    vals = norm.ppf([0.05, 0.5, 0.95])

    print(vals)

if __name__ == "__main__":
    main()