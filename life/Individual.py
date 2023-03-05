import pandas as pd 
import numpy as np 


class Individual: 
    """A class to represent an individuals life"""

    name = "Unknown"
    age = 0

    # Constructor 
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def import_data(self, file_name):
        """Import data from a csv file"""
        self.data = pd.read_csv(file_name)