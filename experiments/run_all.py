from pathlib import Path
import os

from experiments.example import result_generator


def run_all():
    b_savefigs = True
    b_showfigs = False

    dataset1 = "Something"
    dataset2 = "Something else"
    datasets = [dataset1, dataset2]
    dataset_names = ["First dataset", "Second dataset"]

    all_experiments = [result_generator]#, second_generator]

    project_root = Path(r"C:\Users\danielbje\Documents")
    savefigpath_root =  project_root / "figures"
    if not os.path.exists(savefigpath_root): os.mkdir(savefigpath_root)

    for data, name in zip(datasets, dataset_names):
        for experiment in all_experiments:
            print(f"Running {experiment.__name__} ...")
            experiment(data, name, show_figs=b_showfigs, save_figs=b_savefigs, savefigs_root=savefigpath_root)




if __name__=="__main__":
    run_all()