from git import Repo
from tqdm import tqdm

import test_blob2dgp.vel_out.v_data as v_data

def main():
    data_path = v_data.data_import("")[3]
    repo_path = data_path.parents[2]
    campaign_path = data_path.joinpath("Input", f"campaign_{2}")

    folder_list = [folder.name for folder in campaign_path.glob("*/")]
    folder_i = 0
    batch = 0

    repo = Repo(repo_path)
    main = repo.remote(name = "origin")
    
    for folder in tqdm(folder_list):
        folder_i += 1
        folder_path = r"Misc/Test/Data/Input/campaign_2/"
        folder_path = folder_path + folder + "/."
        repo.git.add(folder_path)
        if folder_i % 5 == 0 or folder_i == len(folder_list):
            batch += 1
            repo.index.commit(f"Adding campaign_2 folder batch {batch}")
            main.push()
            print(f"Pushed batch {batch}")

    # git_push()

if __name__ == "__main__":
    main()