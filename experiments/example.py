import os

import matplotlib.pyplot as plt

from src.datasets.dataset import Dataset

def result_generator(
    dataset : Dataset, show_figs=True, save_figs=False, savefigs_root=None, optional_parameter="Value", **kwargs
):
    if save_figs:
        assert (
            savefigs_root is not None
        ), "When saving figures, you need to supply a savefig root"


    # Code generating results here ...





    fig = plt.figure()
    ax = fig.add_subplot()

    # Code plotting results here ...

    plt.title(f"Title of result, {dataset} dataset")

    if save_figs:
        example_figs_subdir = "experiment_name"
        if not os.path.exists(savefigs_root / example_figs_subdir):
            os.mkdir(savefigs_root / example_figs_subdir)
        filepath = (
            savefigs_root / example_figs_subdir / f"result-name_{dataset}.pdf"
        )
        plt.savefig(filepath)

        # TODO: Lagre .tex-fil med figuren
    if show_figs:
        plt.show()
    plt.close()
    return
