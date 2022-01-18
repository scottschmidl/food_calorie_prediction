# Food Calorie Prediction Project
This repo contains my food calorie regression project with Codeup.

## About

### Goal
The goal of this project is
This data is sourced from the USDA Food Data Central.

### Description


### Initial Questions
1)
2)
3)
4)

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
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### Steps to Reproduce
- You will need to go to this website, <a href="https://tools.myfooddata.com/nutrition-facts-database-spreadsheet.php">My Food Data</a> and open the file up in Google Sheets. The following punctuation needs to be removed before data can be read via Pandas, ():-,. Furthermore, the following columns should be dropped, Serving Weight 1-9 description g (the 1-9 is because there are 9 columns with this name).
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