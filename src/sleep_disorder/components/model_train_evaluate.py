import pickle

import pandas as pd
from catboost import CatBoostClassifier
from sklearn.ensemble import (
    AdaBoostClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier,
)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

from sleep_disorder.entity import ModelBuildEvaluateConfig
from sleep_disorder.logging import logger
from sleep_disorder.utils.common import create_directories


def get_results(name, accuracy, recall, precision, f1):
    results = pd.DataFrame()
    results['Name'] = name
    results['Accuracy'] = accuracy
    results['Recall'] = recall
    results['Precision'] = precision
    results['F1_score'] = f1

    return results


class ModelBuildEvaluate:
    def __init__(self, config: ModelBuildEvaluateConfig) -> None:
        self.config = config

        create_directories([self.config.root_dir, self.config.model_dir])

    def train_model(self):
        models = {
            "LogisticRegression": LogisticRegression(),
            "DecisionTreeClassifier": DecisionTreeClassifier(),
            "RandomForestClassifier": RandomForestClassifier(),
            "GradientBoostingClassifier": GradientBoostingClassifier(),
            "AdaBoostClassifier": AdaBoostClassifier(),
            "SVC": SVC(),
            "XGBClassifier": XGBClassifier(),
            "CatBoostClassifier": CatBoostClassifier(verbose=False),
        }

        train_data = pd.read_csv(self.config.train_data_file)

        X_train = train_data.drop(columns="Sleep Disorder")
        y_train = train_data["Sleep Disorder"]

        trained_models = {}

        name = []
        accuracy = []
        recall = []
        precision = []
        f1 = []

        for model_name in models.keys():
            model = models[model_name]
            model.fit(X_train, y_train)
            pred = model.predict(X_train)
            print(f"Train data {model_name} Classification Report:\n{classification_report(y_train, pred)}\n\n\n")
            name.append(model_name)
            accuracy.append(accuracy_score(y_train, pred))
            recall.append(recall_score(y_train, pred, average="macro"))
            precision.append(precision_score(y_train, pred, average="macro"))
            f1.append(f1_score(y_train, pred, average="macro"))
            trained_models[model_name] = model

        results = get_results(name, accuracy, recall, precision, f1)

        return trained_models, results

    def test_model(self, train_models):
        test_data = pd.read_csv(self.config.test_data_file)

        X_test = test_data.drop(columns="Sleep Disorder")
        y_test = test_data["Sleep Disorder"]

        name = []
        accuracy = []
        recall = []
        precision = []
        f1 = []

        print("\n\n\n\n\nTest Results:")

        for model_name in train_models.keys():
            model = train_models[model_name]
            model.fit(X_test, y_test)
            pred = model.predict(X_test)
            print(f"Test data {model_name} Classification Report:\n{classification_report(y_test, pred)}\n\n\n")
            name.append(model_name)
            accuracy.append(accuracy_score(y_test, pred))
            recall.append(recall_score(y_test, pred, average="macro"))
            precision.append(precision_score(y_test, pred, average="macro"))
            f1.append(f1_score(y_test, pred, average="macro"))

        results = get_results(name, accuracy, recall, precision, f1)

        best_model_name = list(results.sort_values('Accuracy', ascending=False)["Name"])[0]

        best_model = train_models[best_model_name]

        return best_model, results

    def save_model(self, model):
        with open(self.config.model_file, "wb") as model_pkl:
            pickle.dump(model, model_pkl)
            logger.info(f"Best model saved to path: {self.config.model_file}")

    def save_test_results(self, test_results):
        with open(self.config.model_results_file, "w") as f:
            f.write(test_results)
            logger.info(f"All model results saved to path: {self.config.model_file}")
