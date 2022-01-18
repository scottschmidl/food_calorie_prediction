import pandas as pd
import numpy as np

class Wrangle:

    def get_food_data(self):
        """get_food_data: get data from csv

        Returns:
            pandas dataframe: used for analysis and modeling
        """
        filename = "MyFoodData Nutrition Facts SpreadSheet Release 1.4 - SR Legacy and FNDDS.csv"
        #filename = "MyFoodData Nutrition Facts SpreadSheet Release 1.4.xlsx"

        try:
            return pd.read_csv(filename)
            #return pd.read_excel(filename, sheet_name="SR Legacy and FNDDS")

        except FileNotFoundError:
            print(f"{filename} not found. Please go to https://tools.myfooddata.com/nutrition-facts-database-spreadsheet.php to download the file.")