from pathlib import Path

import matplotlib.pyplot as plt

class ResultHandler():
    def __init__(self, result_dir=r".results\\", figure_dir=None, show_figs=True, save_figs=False, presentation_mode=False) -> None:
        if isinstance(result_dir, str): result_dir = Path(result_dir)
        if isinstance(figure_dir, str): figure_dir = Path(figure_dir)
        if figure_dir is None: figure_dir = result_dir

        Path.mkdir(result_dir, exist_ok=True)
        Path.mkdir(figure_dir, exist_ok=True)

        self.result_dir = result_dir
        self.figure_dir = figure_dir
        self.presentation_mode = presentation_mode
        self.figure_filtype = ".pdf" if not presentation_mode else ".png"
        self.show_figs = show_figs
        self.save_figs = save_figs


    def _save_figure(self, fig, figname, experiment_name, other_filetype=None):
        experiment_subdir = Path(self.figure_dir / experiment_name)
        Path.mkdir(experiment_subdir, exist_ok=True)
        filetype = self.figure_filtype if other_filetype is None else other_filetype
        filepath = experiment_subdir / (figname + filetype)
        fig.savefig(filepath)
        # TODO: Lagre .tex-fil med figuren



    def finalize_figure(self, fig, figname, experiment_name, other_filetype=None):
        if self.save_figs: self._save_figure(fig, figname, experiment_name, other_filetype=other_filetype)
            
        if self.show_figs: plt.show()
        plt.close()
        return
