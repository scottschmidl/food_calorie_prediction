from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

class SplitGetScale:

    def split(self, df: pd.DataFrame) -> tuple:

        train, test = train_test_split(df, test_size=.15, random_state=123)
        train, validate = train_test_split(train, test_size=.2, random_state=123)

        return train, validate, test

    def get_Xy(self, train: pd.DataFrame, validate: pd.DataFrame, test: pd.DataFrame,
                    target_col: str, cols_dummy=None, cols_drop=None) -> tuple:

        if cols_drop:
            X_train = train.drop(cols_drop, axis=1)
            X_validate = validate.drop(cols_drop, axis=1)
            X_test = test.drop(cols_drop, axis=1)

        if cols_dummy:
            X_train = pd.get_dummies(X_train, columns=cols_dummy, drop_first=True)
            X_validate = pd.get_dummies(X_val, columns=cols_dummy, drop_first=True)
            X_test = pd.get_dummies(X_test, columns=cols_dummy, drop_first=True)

        y_train = train[target_col]
        y_validate = validate[target_col]
        y_test = test[target_col]

        return (X_train, y_train), (X_validate, y_validate), (X_test, y_test)

    def scale(self, X_train: pd.DataFrame, X_validate: pd.DataFrame, X_test: pd.DataFrame) -> tuple:

        scale = StandardScaler()
        scale.fit(X_train)

        X_train_scaled = pd.DataFrame(data=scale.transform(X_train), columns=X_train.columns, index=X_train.index)
        X_validate_scaled = pd.DataFrame(data=scale.transform(X_validate), columns=X_train.columns, index=X_validate.index)
        X_test_scaled = pd.DataFrame(data=scale.transform(X_test), columns=X_train.columns, index=X_test.index)

        return X_train_scaled, X_validate_scaled, X_test_scaled