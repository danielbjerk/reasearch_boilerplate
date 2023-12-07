import os

class Experiment():
    def __init__(self, name, savefig_root_dir, data) -> None:   # Data must have __str__ method, for plotting
        self.results_savedir = savefig_root_dir / name
        self.data = data

        self.current_run_ID = -1
        self.all_run_IDs = []

    def prepare(self):
        """Perform necessary preperations /before/ experiment is run
        """
        if not os.path.exists(self.results_savedir):
            os.mkdir(self.results_savedir)

    def run(self, new_data=None):
        """Optional argument ``new_data`` allows for performing 
        """
        if new_data:
            data = new_data
        else:
            data = self.data
        
        try:
            result = run_experiment()       # May return ExperimentError-type or some :error atom
        except ExperimentException as result:
            pass

        match type(result):
            case ExperimentException:
                # handle errors
                pass
            case _:
                print("Success!")
                #write_results?
                pass
        
        #self.results[self.current_run_ID][result_name] = result
        pass
    
    def save_results(self):
        # parquet
        pass

    def load_results(self):
        pass

    def plot_results(self, show_figs=True, save_figs=False):
        #plt.plot(self.results["some_result"])
        pass
