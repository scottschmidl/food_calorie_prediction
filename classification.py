from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report
from split_get_scale import SplitGetScale
from prepare import Prepare
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import accuracy_score

class Models:

    nutrition_facts = Prepare().get_food_prep()

    sgs = SplitGetScale()
    train, validate, test = sgs.split(nutrition_facts)
    (X_train, y_train), (X_validate, y_validate), (X_test, y_test) = sgs.get_Xy(train, validate, test, target_col="food_group", cols_drop=["food_group"])

    X_train_scaled, X_validate_scaled, X_test_scaled = sgs.scale(X_train, X_validate, X_test)

    def classification_baseline(self):

        from pandas import DataFrame

        act_pred_error = DataFrame({"actual": self.y_train})
        act_pred_error["baseline_prediction"] = self.y_train.value_counts().index[0]

        baseline_acc = accuracy_score(act_pred_error["actual"], act_pred_error["baseline_prediction"])

        print(f"Baseline Accuracy Score:{round(baseline_acc, 2)}")

    def classification_models(self, best_model=None):

        if not best_model:

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

            # print train accuracy
            print(f"TRAIN\nRandom Forest Classifier Train Accuracy: {accuracy_score(self.y_train, rfc_pred_train)}%\nAda Boost Classifier Train Accuracy: {accuracy_score(self.y_train, ada_pred_train)}%\nSupport Vector Classifier Train Accuracy: {accuracy_score(self.y_train, svc_pred_train)}%")

            # print validate accuracy
            print(f"VALIDATE\nRandom Forest Classifier Validation Accuracy: {accuracy_score(self.y_validate, rfc_pred_val)}%\nAda Boost Classifier Validation Accuracy: {accuracy_score(self.y_validate, ada_pred_val)}%\nSupport Vector Classifier Validation Accuracy: {accuracy_score(self.y_validate, svc_pred_val)}%")

            return rfc

        else:
            print("Final Best Model Found! Performing Predictions On X_test_scaled.")

            best_model_pred_test = best_model.predict(self.X_test_scaled)

            print("Calculating Accuracy...")

            print(f"Random Forest Classifier Test Accuracy: {accuracy_score(self.y_test, best_model_pred_test)}")

def main():

    Models().classification_baseline()
    rfc = Models().classification_models()
    Models().classification_models(best_model=rfc)

if __name__ == "__main__":
    main()