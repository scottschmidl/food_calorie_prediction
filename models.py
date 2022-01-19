from split_get_scale import SplitGetScale
from prepare import Prepare
from sklearn.cluster import KMeans, DBSCAN
from sklearn.linear_model import LinearRegression, LassoCV, RidgeCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

class Models:

    nutrition_facts = Prepare().get_food_prep()

    sgs = SplitGetScale()
    train, validate, test = sgs.split(nutrition_facts)
    (X_train, y_train), (X_validate, y_validate), (X_test, y_test) = sgs.get_Xy(train, validate, test, target_col="calories", cols_drop=["calories"])

    def fit_supervised(self, X_train, y_train):
        pass

    def fit_unsupervised(self, X_train, y_train):
        pass

    def get_metric(self, y_train, y_pred):
        return mean_squared_error(y_train, y_pred)