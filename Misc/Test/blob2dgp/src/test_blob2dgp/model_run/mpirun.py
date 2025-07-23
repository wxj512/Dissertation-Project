import subprocess
import pathlib
from tqdm.contrib.concurrent import thread_map

def blob_run(campaign, path = ""):
    def sub_pro_run(folder):
        command = ["mpirun", "-n", "4", str(run_path) + "/blob2d", "-d", str(folder)]
        result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
        return result

    if not(path == ""):
        run_path = path
    else:
        build_path = pathlib.Path(__file__).parents[8]
        build = "BOUT++5.1.1"
        # path = "../../../../../Builds/BOUT++5.1.1/examples/blob2d/"
        run_path = build_path.joinpath("Builds", build,"examples/blob2d")
        camp_path = run_path.joinpath(f"campaign_{int(campaign)}")

    folders = [str(obj) for obj in camp_path.glob("*")]
    status = thread_map(sub_pro_run, folders, max_workers = 4)
    return status

def main():
    blob_run(1)

if __name__ == "__main__":
    main()

# print(B0_inp)