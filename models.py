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
    (X_train, y_train), (X_validate, y_validate), (X_test, y_test) = sgs.get_Xy(self.train, self.validate, self.test, target_col="calories", cols_drop=["calories", "food_group"])

    X_train_scaled, X_val_scaled, X_test_scaled = sgs.scale(self.X_train, self.X_validate, self.X_test)

    def linear_model(self, X_train, y_train):
        pass

    def clustering(self, X_train, y_train):
        pass

    def get_metric(self, y_train, y_pred):
        return   mean_squared_error(y_train, y_pred)