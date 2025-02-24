"""Abstract dataset class

Use this when experiments require use of multiple datasets of similar structure,
which all experiments require a consistent interface with.

This also enables minimal imports, as only the abstract dataset requires to import
functions for reading data, while implementations/inherited datasets 
"""

class Dataset():
    def __init__(self, *args, **kwargs) -> None:

        for key, val in kwargs.items():
            self.__setattr__(key, val)

        # Here: Method for loading data to be used in experiments ..., based on inputs such as filepath

        self.data = {
            "datasource1" : "insert data here",
            "datasource2" : "insert data here as well"
        }

        # TODO: Better way of storing this?
        self.units = {
            "datasource1" : "kW",
            "datasource2" : "kWh"
        }

    def __str__(self) -> str:
        # Set by specific child instances, or by some parameter
        return "Dataset"

    def __getitem__(self, arg):
        if arg in self.data:
            return self.data[arg]
        else:
            return self.__getattribute__(arg)

    def __setitem__(self, key, val):
        self.data[key] = val

    def preprocess(self, *args, **kwargs):
        # Abstract preprocessing function to be overwritten by every child dataset
        return
