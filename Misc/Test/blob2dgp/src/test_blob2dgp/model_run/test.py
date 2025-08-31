from git import Repo
from tqdm import tqdm
from xbout import open_boutdataset
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

import test_blob2dgp.vel_out.v_data as v_data
import inp_gen
import epyscan


def main():
    params = ["x", "y"]
    min_max = np.array([[0.5, 9.5], [0.5, 9.5]])
    n_samples = [10, 10]
    parameters = inp_gen.param_gen(params, min_max, n_samples=n_samples)
    grid_scan = epyscan.GridScan(parameters)
    lhs_samples = 30
    lhs_scan = epyscan.LatinHypercubeSampler(parameters).sample(lhs_samples)
    rng_samples = 30
    rng = np.random.default_rng()
    rng_scan = {
        "x": (rng.random(size = rng_samples) * 9) + 0.5,
        "y": (rng.random(size = rng_samples) * 9) + 0.5,

    }
    print(rng_scan)

    # [print(i) for i in lhs_scan]

    # samples = 50
    # lhs_scan = epyscan.LatinHypercubeSampler(parameters).sample(samples)
    f1 = plt.figure(1, linewidth = 3, edgecolor = "#000000")
    ax1 = f1.gca()
    # for i, ival in enumerate(grid_scan):
    #     ax1.scatter(ival[params[0]], ival[params[1]], marker = "x", color = "orange")
    #     if i == len(grid_scan) - 1:
    #         ax1.scatter(ival[params[0]], ival[params[1]], marker = "x", color = "orange", label = "Uniform Parameter\nScan")
    for j, jval in enumerate(lhs_scan):
        ax1.scatter(jval[params[0]], jval[params[1]], marker = "x", color = "tab:blue")
        if j == len(lhs_scan) - 1:
            ax1.scatter(jval[params[0]], jval[params[1]], marker = "x", color = "tab:blue", label = "Latin-Hypercube\nSampling")
    ax1.scatter(rng_scan["x"], rng_scan["y"], marker = "x", color = "tab:green", label = "Random\nSampling")
        
    # ax1.set_xticks(np.arange(11))
    # ax1.set_yticks(np.arange(11))
    # ax1.grid(visible=True, which="both")
    for tickx in ax1.xaxis.get_major_ticks():
        tickx.tick1line.set_visible(False)
        tickx.label1.set_visible(False)
    for ticky in ax1.yaxis.get_major_ticks():
        ticky.tick1line.set_visible(False)
        ticky.label1.set_visible(False)
    ax1.set_xlabel("Param 1")
    ax1.set_ylabel("Param 2")
    f1.legend(bbox_to_anchor = (0.97, 0.87), fontsize = "small")
    box = ax1.get_position()
    ax1.set_position([box.x0, box.y0, box.width * 0.7, box.height])
    ax1.set_aspect("equal")
    plt.show()

if __name__ == "__main__":
    main()