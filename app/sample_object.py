import pandas as pd
import numpy as np

class sample_object:

    def __init__(self,file):
        self.csv_file = open(file)
        self.dataframe = pd.DataFrame.from_csv(self.csv_file)

    def generate_list(self):
        self.point_list = self.dataframe.values.tolist()

    def display_list(self):
        for i in self.point_list:
            print(i)

    def csv_has_read(file):
        f = open("file", 'r')
        pd.read_csv()
        print("Successfully Loaded!")

    def get_csv_file(self):
        return self.csv_file

    def display_csv_file(self):
        print(pd.read_csv(self.csv_file))

    def get_data_frame(self):
        return self.dataframe

    def display_data_frame(self):
        print(self.dataframe)

    def get_mean_column1(self):
        return self.dataframe.mean()
