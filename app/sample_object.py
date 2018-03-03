import pandas as pd
import numpy as np
"""
Prototype for the statistical object used in data-analyzer.
[3/3/2018] - Instantiates properly with csv file argument,
contains a list of all data values, and access to elementary
statistical operations.

@author Christopher Curtis
"""
class sample_object:

    # Constructor
    def __init__(self,file):
        """Stores csv and generated Pandas DataFrame as data fields"""
        self.csv_file = open(file)
        self.dataframe = pd.DataFrame.from_csv(self.csv_file)

    def generate_list(self):
        """Initializes a list of values from the dataframe data field"""
        self.point_list = self.dataframe.values.tolist()

    def display_list(self):
        """Prints data entries in the dataframe data field"""
        for i in self.point_list:
            print(i)

    # USED IN TESTING NO LONGER IMPLEMENTED!
    def csv_has_read(file):
        f = open("file", 'r')
        pd.read_csv()
        print("Successfully Loaded!")

    # USED IN TESTING NO LONGER IMPLEMENTED
    def get_csv_file(self):
        return self.csv_file

    def display_csv_file(self):
        """Displays csv file contents"""
        print(pd.read_csv(self.csv_file))

    def get_data_frame(self):
        """Getter for the dataframe data field"""
        return self.dataframe

    def display_data_frame(self):
        """Display method for viewing the dataframe data field"""
        print(self.dataframe)

    def get_mean(self):
        """Returns the mean(s) obtained from dataframe"""
        return self.dataframe.mean()

    def get_median(self):
        """Returns the median(s) obtained from dataframe"""
        return self.dataframe.median()

    def get_quartiles(self):
        """Returns the quartiles obtained from dataframe"""
        return [self.dataframe.quantile(.25),
                self.dataframe.quantile(.5),
                self.dataframe.quantile(.75)]

    def get_var(self):
        """Returns the variance obtained from dataframe"""
        return self.dataframe.var()

    def get_quantile_column1(self, x): # Implement in later builds
        return self.dataframe.quantile(x)
