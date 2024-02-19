from pathlib import Path
import os

from experiments.example import result_generator


def run_all():
    b_savefigs = True
    b_showfigs = False

    dataset1 = "Something"
    dataset2 = "Something else"
    all_datasets = [dataset1, dataset2]

    all_experiments = [result_generator]#, second_generator]
    all_kwargs = [
        {"optional_parameter" : "Some other value"},        # optional parameters of experiment result_generator
        #{}                                                 # Empty dict for experiments with no kwargs
    ]

    project_root = Path(r"C:\Users\danielbje\Documents")
    savefigpath_root =  project_root / "figures"
    if not os.path.exists(savefigpath_root): os.mkdir(savefigpath_root)

    for experiment, kwargs in zip(all_experiments, all_kwargs):
        for dataset in all_datasets:
            print(f"Running {experiment.__name__} with {dataset} dataset ...")
            experiment(dataset, show_figs=b_showfigs, save_figs=b_savefigs, savefigs_root=savefigpath_root, **kwargs)


    #TODO: Add functionality for timing each experiment

if __name__=="__main__":
    run_all()