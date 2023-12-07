import os

import matplotlib.pyplot as plt

def result_generator(
    data, dataset_name, show_figs=True, save_figs=False, savefigs_root=None
):
    if save_figs:
        assert (
            savefigs_root is not None
        ), "When saving figures, you need to supply a savefig root"


    # Code here ...

    plt.title(f"Title of result, {dataset_name} dataset")

    if save_figs:
        example_figs_subdir = "experiment_name"
        if not os.path.exists(savefigs_root / example_figs_subdir):
            os.mkdir(savefigs_root / example_figs_subdir)
        filepath = (
            savefigs_root / example_figs_subdir / f"result-name_{dataset_name}.pdf"
        )
        plt.savefig(filepath)
    if show_figs:
        plt.show()
    plt.close()
    return
