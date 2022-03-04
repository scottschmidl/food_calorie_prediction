from split_get_scale import SplitGetScale
from prepare import Prepare
from sklearn.cluster import KMeans, DBSCAN
from sklearn.linear_model import LinearRegression, LassoCV, RidgeCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import seaborn as sns

class Models:
    """
    performs Regression and Clustering
    """

    nutrition_facts = Prepare().get_food_prep()

    sgs = SplitGetScale()
    train, validate, test = sgs.split(nutrition_facts)
    (X_train, y_train), (X_validate, y_validate), (X_test, y_test) = sgs.get_Xy(train, validate, test, target_col="calories", cols_drop=["calories", "food_group"])

    X_train_scaled, X_validate_scaled, X_test_scaled = sgs.scale(X_train, X_validate, X_test)

    def set_baseline(self):
        """set_baseline calculates baseline RMSE
        """

        from pandas import DataFrame

        act_pred_error = DataFrame({"actual": self.y_train})
        act_pred_error["baseline_prediction"] = self.y_train.mean()

        baseline_rmse = round(mean_squared_error(act_pred_error["actual"], act_pred_error["baseline_prediction"], squared=False), 2)

        print(f"Baseline RMSE: {baseline_rmse} calories")

    def linear_modelsTV(self):
        """linear_modelsTV fits and predicts on train and validate
        """

        # fit the model
        lasso = LassoCV(random_state=123, max_iter=1800).fit(self.X_train_scaled, self.y_train)
        ridge = RidgeCV().fit(self.X_train_scaled, self.y_train)
        rfr = RandomForestRegressor(n_estimators=10, max_depth=25, warm_start=True, random_state=123, n_jobs=-1).fit(self.X_train_scaled, self.y_train)
        lr = LinearRegression().fit(self.X_train_scaled, self.y_train)

        # predict on X_train_scaled
        lass_pred_train = lasso.predict(self.X_train_scaled)
        ridge_pred_train = ridge.predict(self.X_train_scaled)
        rfr_pred_train = rfr.predict(self.X_train_scaled)
        lr_pred_train = lr.predict(self.X_train_scaled)

        # predict on X_validate_scaled
        lass_pred_val = lasso.predict(self.X_validate_scaled)
        ridge_pred_val = ridge.predict(self.X_validate_scaled)
        rfr_pred_val = rfr.predict(self.X_validate_scaled)
        lr_pred_val = lr.predict(self.X_validate_scaled)

        # print train RMSE
        print(f"TRAIN\nLassoCV Train RMSE: {round(mean_squared_error(self.y_train, lass_pred_train, squared=False), 2)} calories\nRidgeCV Train RMSE: {round(mean_squared_error(self.y_train, ridge_pred_train, squared=False), 2)} calories\nRandom Forest Regressor Train RMSE: {round(mean_squared_error(self.y_train, rfr_pred_train, squared=False), 2)} calories\nLinear Regressor Train RMSE: {round(mean_squared_error(self.y_train, lr_pred_train, squared=False), 2)} calories")

        # print validate RMSE
        print(f"VALIDATE\nLassoCV Validation RMSE: {round(mean_squared_error(self.y_validate, lass_pred_val, squared=False), 2)} calories\nRidgeCV Validation RMSE: {round(mean_squared_error(self.y_validate, ridge_pred_val, squared=False), 2)} calories\nRandom Forest Regressor Validation RMSE: {round(mean_squared_error(self.y_validate, rfr_pred_val, squared=False), 2)} calories\nLinear Regressor Validation RMSE: {round(mean_squared_error(self.y_validate, lr_pred_val, squared=False), 2)} calories")

    def clustering(self):
        """clustering performs clustering, statistical tests, and regression

        Returns:
            tuple: a tuple of dataframes
        """

        features = ["vitamin_a", "vitamin_c", "vitamin_b12", "vitamin_d", "vitamin_e_alphatocopherol", "thiamin_b1", "riboflavin_b2", "niacin_b3", "vitamin_b6", "folate_b9", "vitamin_k"]

        clusters_train = self.X_train_scaled[features]
        clusters_validate = self.X_validate_scaled[features]
        clusters_test = self.X_test_scaled[features]

        # creating the object
        kmeans = KMeans(n_clusters=8, max_iter=500)

        # fitting the object
        kmeans.fit(clusters_train)

        # predict on train
        y_kmeans_train = kmeans.predict(clusters_train)
        self.X_train_scaled['feat_clusters'] = y_kmeans_train

        #predict on validate
        y_kmeans_validate = kmeans.predict(clusters_validate)
        self.X_validate_scaled['feat_clusters'] = y_kmeans_validate

        #predict on test
        y_kmeans_test = kmeans.predict(clusters_test)
        self.X_test_scaled['feat_clusters'] = y_kmeans_test

        # create plot of clusters and means
        sns.barplot(x=self.X_train_scaled["feat_clusters"], y=self.y_train)

        # run stat tests on cluster
        X_train_scaled_copy = self.X_train_scaled[["feat_clusters"]]
        X_train_scaled_copy["calories"] = self.y_train

        # create series for ANOVA test
        feat_cluster_0 = X_train_scaled_copy["calories"][X_train_scaled_copy["feat_clusters"] == 0]
        feat_cluster_1 = X_train_scaled_copy["calories"][X_train_scaled_copy["feat_clusters"] == 1]
        feat_cluster_2 = X_train_scaled_copy["calories"][X_train_scaled_copy["feat_clusters"] == 2]
        feat_cluster_3 = X_train_scaled_copy["calories"][X_train_scaled_copy["feat_clusters"] == 3]
        feat_cluster_4 = X_train_scaled_copy["calories"][X_train_scaled_copy["feat_clusters"] == 4]
        feat_cluster_5 = X_train_scaled_copy["calories"][X_train_scaled_copy["feat_clusters"] == 5]
        feat_cluster_6 = X_train_scaled_copy["calories"][X_train_scaled_copy["feat_clusters"] == 6]
        feat_cluster_7 = X_train_scaled_copy["calories"][X_train_scaled_copy["feat_clusters"] == 7]

        # import ANOVA test
        from scipy.stats import f_oneway

        # perform ANOVA test
        f, p = f_oneway(feat_cluster_0, feat_cluster_1, feat_cluster_2, feat_cluster_3, feat_cluster_4, feat_cluster_5, feat_cluster_6, feat_cluster_7)
        print(f"ANOVA F-Statistic: {round(f, 2)}, P-Value: {round(p, 2)}")

        return self.X_train_scaled, self.X_validate_scaled, self.X_test_scaled

    def cluster_modeling(self, X_train_scaled=None, X_validate_scaled=None, X_test_scaled=None, best_model=None):
        """cluster_modeling performed regression with clusters

        Args:
            X_train_scaled (pandas dataframe, optional): scaled training data. Defaults to None.
            X_validate_scaled (pandas dataframe, optional): scaled validate data. Defaults to None.
            X_test_scaled (pandas dataframe, optional): sclaed test data. Defaults to None.
            best_model (fit object, optional): the best model after fitting, predicting, and checking accuracy. Defaults to None.

        Returns:
            fit object: the algorithm to be used for testing
        """

        if not best_model:

            # fit the model
            lasso = LassoCV(random_state=123, max_iter=1800).fit(X_train_scaled, self.y_train)
            ridge = RidgeCV().fit(X_train_scaled, self.y_train)
            rfr = RandomForestRegressor(n_estimators=10, max_depth=25, min_samples_split=2, min_samples_leaf=1, bootstrap=True, warm_start=True, random_state=123, n_jobs=-1).fit(X_train_scaled, self.y_train)
            lr = LinearRegression().fit(X_train_scaled, self.y_train)

            # predict on X_train_scaled
            lass_pred_train = lasso.predict(X_train_scaled)
            ridge_pred_train = ridge.predict(X_train_scaled)
            rfr_pred_train = rfr.predict(X_train_scaled)
            lr_pred_train = lr.predict(X_train_scaled)

            # predict on X_train_scaled
            lass_pred_val = lasso.predict(X_validate_scaled)
            ridge_pred_val = ridge.predict(X_validate_scaled)
            rfr_pred_val = rfr.predict(X_validate_scaled)
            lr_pred_val = lr.predict(X_validate_scaled)

            # print train RMSE
            print(f"TRAIN\nLassoCV Train RMSE: {round(mean_squared_error(self.y_train, lass_pred_train, squared=False), 2)} calories\nRidgeCV Train RMSE: {round(mean_squared_error(self.y_train, ridge_pred_train, squared=False), 2)} calories\nRandom Forest Regressor Train RMSE: {round(mean_squared_error(self.y_train, rfr_pred_train, squared=False), 2)} calories\nLinear Regressor Train RMSE: {round(mean_squared_error(self.y_train, lr_pred_train, squared=False), 2)} calories")

            # print validate RMSE
            print(f"VALIDATE\nLassoCV Validation RMSE: {round(mean_squared_error(self.y_validate, lass_pred_val, squared=False), 2)} calories\nRidgeCV Validation RMSE: {round(mean_squared_error(self.y_validate, ridge_pred_val, squared=False), 2)} calories\nRandom Forest Regressor Validation RMSE: {round(mean_squared_error(self.y_validate, rfr_pred_val, squared=False), 2)} calories\nLinear Regressor Validation RMSE: {round(mean_squared_error(self.y_validate, lr_pred_val, squared=False), 2)} calories")

            return lr

        else:

            best_model_pred_test = best_model.predict(X_test_scaled)

            # print test RMSE
            print(f"TEST\nLinear Regressor Test RMSE: {round(mean_squared_error(self.y_test, best_model_pred_test, squared=False), 2)} calories")