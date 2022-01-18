from prepare import Prepare
import seaborn as sns
import matplotlib.pyplot as plt
from split_get_scale import SplitGetScale

class Viz:

    nutrition_facts = Prepare().get_food_prep()

    sgs = SplitGetScale()
    train, _, _ = sgs.split(nutrition_facts)

    def histo_gram(self, col="calories"):

        plt.figure(figsize=(10, 6))
        sns.histplot(self.train[col])

    def bar_plot(self, x: str, y="calories"):
        plt.figure(figsize=(12, 8))
        plt.xticks(rotation=65)
        sns.barplot(x=x, y=y,  data=self.train)

    def scatter_plot(self, x: str, y="calories"):

        plt.figure(figsize=(12, 7))
        sns.scatterplot(x=x, y=y, data=self.train)