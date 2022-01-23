# Food Group, Calorie Prediction Project
This repo contains my food calorie regression project with Codeup.

## About
This data is sourced from the USDA Food Data Central.

### Goal
The goal of this project is to understand which vitamins, minerals, and other nutrients are the best predictors of calories, does the quantity matter, and how accurately can calories be predicted. Additionally, how accuractely can a food group be predicted based off of the vitamins, minerals, and other nutrients that make up the foods.

### Description
It is important for people to understand what they are eating and how it may affect their bodies and physical goals. Furthermore, is it important to make sure that foods are marketed correctly, making the ability to predict a foods group imperative.

### Initial Questions
<p>1) Are the mean calories for a each food group equal?</p>
<p>2) Is there a relationship between protein intake and calories</p>
<p>3) Are carbhohyrdrates and calories correlated?</p>
<p>4) What kind of relationship exists between fats and calories?</p>

### Data Dictionary
<table>
<thead><tr>
<th>Target</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>calories</td>
<td>amount of calories in the food item</td>
</tr>
</tbody>
</table>

<table>
<thead><tr>
<th>Variable</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>food_group</td>
<td>into what group does the food fall</td>
</tr>
<tr>
<td>fat</td>
<td>amount in grams</td>
</tr>
<tr>
<td>protein</td>
<td>amount in grams</td>
</tr>
<tr>
<td>carbohydrate</td>
<td>amount in grams</td>
</tr>
<tr>
<td>sugars</td>
<td>amount in grams</td>
</tr>
<tr>
<td>fiber</td>
<td>amount in grams</td>
</tr>
<tr>
<td>saturated fats</td>
<td>amount in grams</td>
</tr>
<tr>
<td>water</td>
<td>amount in grams</td>
</tr>
<tr>
<td>alcohol</td>
<td>amount in grams</td>
</tr>
<tr>
<td>cholesterol</td>
<td>amount in milligram</td>
</tr>
<tr>
<td>calcium</td>
<td>amount in milligram</td>
</tr>
<tr>
<td>iron</td>
<td>amount in milligram</td>
</tr>
<tr>
<td>potassium</td>
<td>amount in milligram</td>
</tr>
<tr>
<td>magnesium</td>
<td>amount in milligram</td>
</tr>
<tr>
<td>vitamin c</td>
<td>amount in milligram</td>
</tr>
<tr>
<td>vitamin e alphatocopherol</td>
<td>amount in milligram</td>
</tr>
<tr>
<td>omega 3s</td>
<td>amount in milligram</td>
</tr>
<tr>
<td>omega 6s</td>
<td>amount in milligram</td>
</tr>
<tr>
<td>phosphorus</td>
<td>amount in milligram</td>
</tr>
<tr>
<td>sodium</td>
<td>amount in milligram</td>
</tr>
<tr>
<td>zinc</td>
<td>amount in milligram</td>
</tr>
<tr>
<td>copper</td>
<td>amount in milligram</td>
</tr>
<tr>
<td>thiamin b1</td>
<td>amount in milligram</td>
</tr>
<tr>
<td>riboflavin b2</td>
<td>amount in milligram</td>
</tr>
<tr>
<td>niacin b3</td>
<td>amount in milligram</td>
</tr>
<tr>
<td>vitamin b6</td>
<td>amount in milligram</td>
</tr>
<tr>
<td>choline</td>
<td>amount in milligram</td>
</tr>
<tr>
<td>fatty acids total monounsaturated</td>
<td>amount in milligram</td>
</tr>
<tr>
<td>fatty acids total polyunsaturated</td>
<td>amount in milligram</td>
</tr>
<tr>
<td>caffeine</td>
<td>amount in milligram</td>
</tr>
<tr>
<td>theobromine</td>
<td>amount in milligram</td>
</tr>
<tr>
<td>vitamin a</td>
<td>amount in micrograms</td>
</tr>
<tr>
<td>vitamin b12</td>
<td>amount in micrograms</td>
</tr>
<tr>
<td>vitamin d</td>
<td>amount in micrograms</td>
</tr>
<tr>
<td>selenium</td>
<td>amount in micrograms</td>
</tr>
<tr>
<td>folate b9</td>
<td>amount in micrograms</td>
</tr>
<tr>
<td>folic acid</td>
<td>amount in micrograms</td>
</tr>
<tr>
<td>food folate</td>
<td>amount in micrograms</td>
</tr>
<tr>
<td>folate dfe</td>
<td>amount in micrograms</td>
</tr>
<tr>
<td>retinol</td>
<td>amount in micrograms</td>
</tr>
<tr>
<td>carotene beta</td>
<td>amount in micrograms</td>
</tr>
<tr>
<td>carotene alpha</td>
<td>amount in micrograms</td>
</tr>
<tr>
<td>lycopene</td>
<td>amount in micrograms</td>
</tr>
<tr>
<td>lutein + zeaxanthin</td>
<td>amount in micrograms</td>
</tr>
<tr>
<td>vitamin k</td>
<td>amount in micrograms</td>
</tr>
</tbody>
</table>

### Steps to Reproduce
- You will need to go to this website, <a href="https://tools.myfooddata.com/nutrition-facts-database-spreadsheet.php">Food Data</a> and open the file up in Google Sheets. The following punctuation needs to be removed before data can be read via Pandas, ():-,. Furthermore, the following columns should be dropped, Serving Weight 1-9 description g (the 1-9 is because there are 9 columns with this name).
- From the Google Sheet Readme, "all serving sizes are in 100 grams. Use the serving size conversion weights at the end of the file to convert values. For example to convert to an ounce (28.4g) multiply each value by 0.284".
- Download from Google Sheets as a CSV.
- Clone this repo and ensure wrangle.py and prepare.py are on your local machine.
- Verify *.csv is in the .gitignore to ensure the csv file is not pushed to GitHub.
- The technologies used in this project are Python 3.9.5, Pandas 1.3.5, MatPlotLib 3.5.0, Numpy 1.21.2 Seaborn 0.11.2, Scipy 1.7.3, and SkLearn 1.0.1. The notebook named report.ipynb should run.

### Plan
- Wrangle the data from the xlsx file.
- Visualizations and statistical tests.
- Regression and clustering machine learning using ENTER CHOSEN MODELS HERE.
- Fit on the training data and check for overfitting with the validation data.
- Pick the best model to test and move into production.
- Discuss some recommendations and next steps I would like to do with this project.
