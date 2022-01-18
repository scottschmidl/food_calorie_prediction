from prepare import Prepare
from scipy.stats import pearsonr, f_oneway
from split_get_scale import SplitGetScale

class StatTest:

    nutrition_facts = Prepare().get_food_prep()

    sgs = SplitGetScale()
    train, _, _ = sgs.split(nutrition_facts)

    @classmethod
    def __food_group_subsets(cls):

        meats = cls.train["calories"][cls.train["food_group"] == "Meats"]
        vegetables = cls.train["calories"][cls.train["food_group"] == "Vegetables"]
        baked_foods = cls.train["calories"][cls.train["food_group"] == "Baked Foods"]
        fish = cls.train["calories"][cls.train["food_group"] == "Fish"]
        prepared_meals = cls.train["calories"][cls.train["food_group"] == "Prepared Meals"]
        fast_foods = cls.train["calories"][cls.train["food_group"] == "Fast Foods"]
        beverages = cls.train["calories"][cls.train["food_group"] == "Beverages"]
        baby_foods = cls.train["calories"][cls.train["food_group"] == "Baby Foods"]
        soups_sauces = cls.train["calories"][cls.train["food_group"] == "Soups and Sauces"]
        sweets = cls.train["calories"][cls.train["food_group"] == "Sweets"]
        fruits = cls.train["calories"][cls.train["food_group"] == "Fruits"]
        bean_lentils = cls.train["calories"][cls.train["food_group"] == "Beans and Lentils"]
        bfast_cereal = cls.train["calories"][cls.train["food_group"] == "Breakfast Cereals"]
        dairy_egg = cls.train["calories"][cls.train["food_group"] == "Dairy and Egg Products"]
        snack = cls.train["calories"][cls.train["food_group"] == "Snacks"]
        grains_pasta = cls.train["calories"][cls.train["food_group"] == "Grains and Pasta"]
        fats_oils = cls.train["calories"][cls.train["food_group"] == "Fats and Oils"]
        american_indian = cls.train["calories"][cls.train["food_group"] == "American Indian"]
        nuts_seeds = cls.train["calories"][cls.train["food_group"] == "Nuts and Seeds"]
        restaurant_foods = cls.train["calories"][cls.train["food_group"] == "Restaurant Foods"]
        spices_herbs = cls.train["calories"][cls.train["food_group"] == "Spices and Herbs"]

        return meats, vegetables, baked_foods, fish, prepared_meals, fast_foods, beverages, baby_foods, soups_sauces, sweets, fruits,      bean_lentils, bfast_cereal, dairy_egg, snack, grains_pasta, fats_oils, american_indian, nuts_seeds, restaurant_foods, spices_herbs


    def anova(self):

        meats, vegetables, baked_foods, fish, prepared_meals, fast_foods, beverages, baby_foods, soups_sauces, sweets, fruits,      bean_lentils, bfast_cereal, dairy_egg, snack, grains_pasta, fats_oils, american_indian, nuts_seeds, restaurant_foods, spices_herbs = StatTest.__food_group_subsets()

        f, p = f_oneway( meats, vegetables, baked_foods, fish, prepared_meals, fast_foods, beverages, baby_foods, soups_sauces, sweets, fruits, bean_lentils, bfast_cereal, dairy_egg, snack, grains_pasta, fats_oils, american_indian, nuts_seeds, restaurant_foods, spices_herbs, axis=0)

        return f, p

    def pearson_correlation(self, cols: list, y="calories"):

        return {col: pearsonr(self.train[col], self.train[y]) for col in cols}