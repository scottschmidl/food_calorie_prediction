from wrangle import Wrangle

class Prepare:


    nutrition_facts = Wrangle().get_food_data()

    @classmethod
    def __remove_null(cls):

        #nutrition_facts = Wrangle().get_food_data()

        # removed food group nulls
        nutrition_facts = cls.nutrition_facts.dropna(axis=0, subset=["Food Group"])

        return nutrition_facts

    @classmethod
    def __drop_cols(cls):

        nutrition_facts = Prepare.__remove_null()

        # dropping columns that have every value missing
        cols_drop = ["Added Sugar g", "Soluble Fiber g", "Insoluble Fiber g", "Total sugar alcohols g", "Molybdenum mcg", "Chlorine mg", "Biotin B7 mcg", "NetCarbs g"]
        nutrition_facts = nutrition_facts.drop(columns=cols_drop, axis=1)

        # dropping cols that don't seem to mean much
        more_drop = ["ID", "Name", '183 n3 ccc ALA mg', '205 n3 EPA mg', '225 n3 DPA mg', '226 n3 DHA mg', "Serving Weight 1 g", "Serving Weight 2 g", "Serving Weight 3 g", "Serving Weight 4 g", "Serving Weight 5 g", "Serving Weight 6 g", "Serving Weight 7 g", "Serving Weight 8 g", "Serving Weight 9 g", "200 Calorie Weight g"]
        nutrition_facts = nutrition_facts.drop(columns=more_drop, axis=1)

        return nutrition_facts

    @classmethod
    def __remove_missing_values(cls, prop_required_column=.70, prop_required_row=.70):

        nutrition_facts = Prepare.__drop_cols()

        # drop column if 70% of its rows are empty
        print(prop_required_column, type(prop_required_column))
        threshold = int(prop_required_column*len(nutrition_facts))
        nutrition_facts.dropna(axis=1, thresh=threshold, inplace=True)

        # drop row if 70% of its columns are empty
        # threshold = int(prop_required_row*len(nutrition_facts.columns))
        # nutrition_facts.dropna(axis=0, thresh=threshold, inplace=True)

        return nutrition_facts

    @classmethod
    def __fill_nutrition(cls, fill_value=0):

        nutrition_facts = Prepare.__remove_missing_values()

        nutrition_facts.fillna(fill_value, inplace=True)

        return nutrition_facts

    @classmethod
    def __rename_cols(cls):

        nutrition_facts = Prepare.__fill_nutrition()

        nutrition_facts.columns = nutrition_facts.columns.str.lower()

        cols_rename = {"food group": "food_group", "saturated fats g": "saturated_fats", "pral score": "pral_score", "fat g": "fat", "protein g": "protein", "carbohydrate g": "carbohydrate", "sugars g": "sugars", "fiber g": "fiber", "cholesterol mg": "cholesterol", "calcium mg": "calcium", "iron fe mg": "iron", "potassium k mg": "potassium", "magnesium mg": "magnesium", "vitamin a rae mcg": "vitamin_a", "vitamin c mg": "vitamin_c", "vitamin b12 mcg": "vitamin_b12", "vitamin d mcg": "vitamin_d", "vitamin e alphatocopherol mg": "vitamin_e_alphatocopherol", "water g": "water", "omega 3s mg": "omega_3s", "omega 6s mg": "omega_6s", "phosphorus p mg": "phosphorus", "sodium mg": "sodium", "zinc zn mg": "zinc", "copper cu mg": "copper", "selenium se mcg": "selenium", "thiamin b1 mg": "thiamin_b1", "riboflavin b2 mg": "riboflavin_b2", "niacin b3 mg": "niacin_b3", "vitamin b6 mg": "vitamin_b6", "folate b9 mcg": "folate_b9", "folic acid mcg": "folic_acid", "food folate mcg": "food_folate", "folate dfe mcg": "folate_dfe", "choline mg": "choline", "retinol mcg": "retinol", "carotene beta mcg": "carotene_beta", "carotene alpha mcg": "carotene_alpha", "lycopene mcg": "lycopene", "lutein + zeaxanthin mcg": "lutein_plus_zeaxanthin", "vitamin k mcg": "vitamin_k", "fatty acids total monounsaturated mg": "fatty_acids_total_monounsaturated", "fatty acids total polyunsaturated mg": "fatty_acids_total_polyunsaturated", "alcohol g": "alcohol", "caffeine mg": "caffeine", "theobromine mg": "theobromine"}

        nutrition_facts = nutrition_facts.rename(mapper=cols_rename, axis=1)

        return nutrition_facts

    def get_food_prep(self):

        nutrition_facts = Prepare.__rename_cols()
        return nutrition_facts