from prepare import Prepare
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

class SplitGetScale:

    def split(self, df):

        train, test = train_test_split(df, test_size=.15, random_state=123)
        train, validate = train_test_split(train, test_size=.2, random_state=123)

        return train, validate, test

    def get_Xy(self, train, validate, test, cols_dummy=None, cols_drop=None):

        if cols_drop:
            X_train = train.drop(cols_drop, axis=1)
            X_val = validate.drop(cols_drop, axis=1)
            X_test = test.drop(cols_drop, axis=1)

        if cols_dummy:
            X_train = pd.get_dummies(X_train, columns=cols_dummy, drop_first=True)
            X_val = pd.get_dummies(X_val, columns=cols_dummy, drop_first=True)
            X_test = pd.get_dummies(X_test, columns=cols_dummy, drop_first=True)

        y_train = train["log_error"]
        y_val = validate["log_error"]
        y_test = test["log_error"]

        return (X_train, y_train), (X_val, y_val), (X_test, y_test)

    def scale(self, X_train, X_validate, X_test):

        scale = StandardScaler()
        scale.fit(X_train)

        X_train_scaled = pd.DataFrame(data=scale.transform(X_train), columns=X_train.columns)
        X_val_scaled = pd.DataFrame(data=scale.transform(X_validate), columns=X_train.columns)
        X_test_scaled = pd.DataFrame(data=scale.transform(X_test), columns=X_train.columns)

        return X_train_scaled, X_val_scaled, X_test_scaled, scale