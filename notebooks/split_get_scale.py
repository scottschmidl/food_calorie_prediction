from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

class SplitGetScale:
    """
    split the data into train, validate, test, X and y, and scales
    """

    def split(self, df: pd.DataFrame) -> tuple:
        """split splits data into train, validate, test

        Args:
            df (pd.DataFrame): the dataframe to split

        Returns:
            tuple: the train, validate, and test dataframes
        """

        train, test = train_test_split(df, test_size=.15, random_state=123)
        train, validate = train_test_split(train, test_size=.2, random_state=123)

        return train, validate, test

    def get_Xy(self, train: pd.DataFrame, validate: pd.DataFrame, test: pd.DataFrame,
                    target_col: str, cols_dummy=None, cols_drop=None) -> tuple:
        """get_Xy splits train, validate, test into X, y

        Args:
            train (pd.DataFrame): training set
            validate (pd.DataFrame): validation set
            test (pd.DataFrame): testing set
            target_col (str): which column will be the target
            cols_dummy (list, optional): list of columns to dummy. Defaults to None.
            cols_drop (list, optional): list of columns to drop. Defaults to None.

        Returns:
            tuple: pandas dataframes ready for modeling
        """

        if cols_drop:
            X_train = train.drop(cols_drop, axis=1)
            X_validate = validate.drop(cols_drop, axis=1)
            X_test = test.drop(cols_drop, axis=1)

        if cols_dummy:
            X_train = pd.get_dummies(X_train, columns=cols_dummy, drop_first=True)
            X_validate = pd.get_dummies(X_validate, columns=cols_dummy, drop_first=True)
            X_test = pd.get_dummies(X_test, columns=cols_dummy, drop_first=True)

        y_train = train[target_col]
        y_validate = validate[target_col]
        y_test = test[target_col]

        return (X_train, y_train), (X_validate, y_validate), (X_test, y_test)

    def scale(self, X_train: pd.DataFrame, X_validate: pd.DataFrame, X_test: pd.DataFrame) -> tuple:
        """scale scales the data

        Args:
            X_train (pd.DataFrame): training data to scale
            X_validate (pd.DataFrame): validation data to scale
            X_test (pd.DataFrame): testing data to scaled

        Returns:
            tuple: scaled train, validate, and test
        """

        scale = StandardScaler()
        scale.fit(X_train)

        X_train_scaled = pd.DataFrame(data=scale.transform(X_train), columns=X_train.columns, index=X_train.index)
        X_validate_scaled = pd.DataFrame(data=scale.transform(X_validate), columns=X_train.columns, index=X_validate.index)
        X_test_scaled = pd.DataFrame(data=scale.transform(X_test), columns=X_train.columns, index=X_test.index)

        return X_train_scaled, X_validate_scaled, X_test_scaled