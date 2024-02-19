from .result_handler.result_handler import ResultHandler
from .datasets.dataset import Dataset

from experiments.example import result_generator


def run_all():
    res_handler = ResultHandler(r"\\figures\\", show_figs=True, save_figs=False)

    dataset1 = Dataset(x=[1], y=[2])
    dataset2 = Dataset(x=[2], y=[3])
    all_datasets = [dataset1, dataset2]

    all_experiments = [result_generator]#, second_generator]
    all_kwargs = [
        {"optional_parameter" : "Some other value"},        # optional parameters of experiment result_generator
        #{}                                                 # Empty dict for experiments with no kwargs
    ]


    #TODO: Add functionality for timing each experiment
    for experiment, kwargs in zip(all_experiments, all_kwargs):
        for dataset in all_datasets:
            print(f"Running {experiment.__name__} with {dataset} dataset ...")
            experiment(dataset, res_handler, **kwargs)


if __name__=="__main__":
    run_all()