import matplotlib.pyplot as plt

from src.datasets.dataset import Dataset        # TODO: Move dataset to experiments module
from .result_handler.result_handler import ResultHandler

from package1.calculation import advanced_calc

def result_generator(dataset : Dataset, figure_handler : ResultHandler, optional_parameter="Value", **kwargs):

    # Code generating results here ...
    x = dataset["x"]
    y = dataset["y"]

    result = advanced_calc.perform_advanced_calc(x, y)


    # Code plotting results here ...
    fig = plt.figure()
    ax = fig.add_subplot()

    plt.plot(result)

    #plt.xlabel(f"Value [{dataset.units["x"]}]")
    #plt.ylabel(f"Value [{dataset.units["y"]}]")
    plt.title(f"Title of result, {dataset} dataset")
    plt.tight_layout()

    figure_handler.finalize_figure(fig, figname=f"result-title-shortened_{dataset}", experiment_name="result_generator")
