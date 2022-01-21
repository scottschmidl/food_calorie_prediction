from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report
from split_get_scale import SplitGetScale
from prepare import Prepare
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import accuracy_score

class ClassificationModels:

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

        print(f"Baseline Accuracy Score: {round(baseline_acc, 2)}%")

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
            print(f"TRAIN\nRandom Forest Classifier Train Accuracy: {round(accuracy_score(self.y_train, rfc_pred_train), 2)}%\nAda Boost Classifier Train Accuracy: {round(accuracy_score(self.y_train, ada_pred_train), 2)}%\nSupport Vector Classifier Train Accuracy: {round(accuracy_score(self.y_train, svc_pred_train), 2)}%")

            # print validate accuracy
            print(f"\nVALIDATE\nRandom Forest Classifier Validation Accuracy: {round(accuracy_score(self.y_validate, rfc_pred_val), 2)}%\nAda Boost Classifier Validation Accuracy: {round(accuracy_score(self.y_validate, ada_pred_val), 2)}%\nSupport Vector Classifier Validation Accuracy: {round(accuracy_score(self.y_validate, svc_pred_val), 2)}%")

            return rfc

        else:
            print("TEST\nFinal Best Model Found Using Random Forest Classifier! Performing Predictions on X_test_scaled.")

            rfc_pred_test = best_model.predict(self.X_test_scaled)

            print(f"Calculating Accuracy...\nRandom Forest Classifier Test Accuracy: {round(accuracy_score(self.y_test, rfc_pred_test), 2)}")