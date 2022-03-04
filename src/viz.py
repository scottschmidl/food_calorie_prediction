from prepare import Prepare
import seaborn as sns
import matplotlib.pyplot as plt
from split_get_scale import SplitGetScale

class Viz:
    """ creates visualizations
    """

    nutrition_facts = Prepare().get_food_prep()

    sgs = SplitGetScale()
    train, _, _ = sgs.split(nutrition_facts)

    def histo_gram(self, col="calories"):
        """histo_gram creates a histogram

        Args:
            col (str, optional): columns to plot as a histogram. Defaults to "calories".
        """

        plt.figure(figsize=(10, 6))
        sns.histplot(self.train[col])

    def bar_plot(self, x: str, y="calories"):
        """bar_plot plots a bar plot

        Args:
            x (str): column to use for x
            y (str, optional): column to use for y. Defaults to "calories".
        """

        plt.figure(figsize=(12, 8))
        plt.xticks(rotation=65)
        sns.barplot(x=x, y=y,  data=self.train)

    def scatter_plot(self, x: str, y="calories"):
        """scatter_plot plots a scatter plot

        Args:
            x (str): column to use for x
            y (str, optional): column to use for y. Defaults to "calories".
        """

        plt.figure(figsize=(12, 7))
        sns.scatterplot(x=x, y=y, data=self.train)