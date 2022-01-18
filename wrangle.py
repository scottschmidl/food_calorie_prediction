import pandas as pd
import numpy as np

class Wrangle:

    def get_food_data(self):
        """get_food_data: get data from csv

        Returns:
            pandas dataframe: used for analysis and modeling
        """
        filename1 = "Food_Log.csv"
        filename2 = "Nutrition_transposed.csv"
        filename3 = "Nutrition.csv"

        try:
            return pd.read_csv(filename1), pd.read_csv(filename2), pd.read_csv(filename3)

        except FileNotFoundError:
            print(f"{filename} not found. Please go to https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/0OR9HL to download the files.")