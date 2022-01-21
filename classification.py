from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report
from split_get_scale import SplitGetScale
from prepare import Prepare
from sklearn.model_selection import RandomizedSearchCV

class Models:

    nutrition_facts = Prepare().get_food_prep()

    sgs = SplitGetScale()
    train, validate, test = sgs.split(nutrition_facts)
    (X_train, y_train), (X_validate, y_validate), (X_test, y_test) = sgs.get_Xy(train, validate, test, target_col="food_group", cols_drop=["food_group"])

    X_train_scaled, X_validate_scaled, X_test_scaled = sgs.scale(X_train, X_validate, X_test)

    def classification_baseline(self):

        from pandas import DataFrame
        from sklearn.metrics import accuracy_score

        act_pred_error = DataFrame({"actual": self.y_train})
        act_pred_error["baseline_prediction"] = self.y_train.value_counts().index[0]

        baseline_acc = accuracy_score(act_pred_error["actual"], act_pred_error["baseline_prediction"])

        print(f"Baseline Accuracy Score:{round(baseline_acc, 2)}")

    def classification_models(self):

        # fit the model
        rfc = RandomForestClassifier().fit(self.X_train_scaled, self.y_train)
        ada = AdaBoostClassifier().fit(self.X_train_scaled, self.y_train)
        svc = SVC().fit(self.X_train_scaled, self.y_train)

        # predict on X_train_scaled
        rfc_pred_train = rfc.predict(self.X_train_scaled)
        ada_pred_train = ada.predict(self.X_train_scaled)
        svc_pred_train = svc.predict(self.X_train_scaled)

        # predict on X_validate_scaled
        rfc_pred_val = rfc.predict(self.X_validate_scaled)
        ada_pred_val = ada.predict(self.X_validate_scaled)
        svc_pred_val = svc.predict(self.X_validate_scaled)

        # print train RMSE
        print(f" TRAIN\nRandom Forest Classifier Train Classification Report:\n{classification_report(self.y_train, rfc_pred_train)}\nAda Boost Classifier Train Classification Report:\n{classification_report(self.y_train, ada_pred_train)}\n Support Vector Classifier Train Classification Report:\n{classification_report(self.y_train, svc_pred_train)}\n")

        # print validate RMSE
        print(f"\nVALIDATE\nRandom Forest Classifier Validation Classification Report:\n{classification_report(self.y_validate, rfc_pred_val)}\nAda Boost Classifier Validation Classification Report:\n{classification_report(self.y_validate, ada_pred_val)}\n Support Vector Classifier Validation RMSE:\n{classification_report(self.y_validate, svc_pred_val)}")


def main():
    # Models().classification_models()
    Models().classification_baseline()

if __name__ == "__main__":
    main()