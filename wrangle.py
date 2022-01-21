import pandas as pd
pd.options.display.max_columns = 110

class Wrangle:

    def get_food_data(self):
        """get_food_data: get data from csv

        Returns:
            pandas dataframe: used for analysis and modeling
        """
        filename = "MyFoodData Nutrition Facts SpreadSheet Release 1.4 - SR Legacy and FNDDS.csv"

        try:
            return pd.read_csv(filename)

        except FileNotFoundError:
            print(f"{filename} not found. Please go to https://tools.myfooddata.com/nutrition-facts-database-spreadsheet.php to download the file.")