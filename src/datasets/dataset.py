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

        # Here: Method for loading data to be used in experiments

        self.data = {
            "datasource1" : "insert data here",
            "datasource2" : "insert data here as well"
        }    


    def __str__(self) -> str:
        using_inheritance_or_implementation = input()
        if using_inheritance_or_implementation == "inheritance":
            raise NotImplementedError("Must be implemented by every specific child instance of dataset!")
        else:
            return f"Name of dataset dependant on {self.init_parameters}"
