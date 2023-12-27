import os
import pickle

import numpy as np
import pandas as pd

from sleep_disorder.constants import (
    FLOAT_COL_NAME,
    INT_COL_NAME,
    NUM_COL_NAME,
    OBJECT_COL_NAME,
)
from sleep_disorder.entity import PredictionConfig


class UserPrediction:
    def __init__(self, config: PredictionConfig):
        self.config = config

    def get_model_and_preprocessor(self):
        with open(self.config.model_file, "rb") as model_pkl:
            model = pickle.load(model_pkl)

        with open(self.config.preprocessor_file, "rb") as processor_pkl:
            preprocessor = pickle.load(processor_pkl)

        return model, preprocessor

    def predict_for_user(self, model, preprocessor, user_input: list) -> str:
        # Creating user data dict
        user_data_dict = {}

        for key, value in user_input:
            user_data_dict[key] = [value]

        # Creating DataFrame from dict created
        user_df = pd.DataFrame(user_data_dict)

        # Converting Numeric values from str to int32 formate
        user_df[INT_COL_NAME] = user_df[INT_COL_NAME].astype("int32")

        # Converting Sleep Duration to float
        user_df[FLOAT_COL_NAME] = user_df[FLOAT_COL_NAME].astype("float32")

        # Converting blood pressure to BP ration
        user_df["BP Ratio"] = round(user_df["Systolic blood pressure"] / user_df["Diastolic blood pressure"], 2)

        # Dropping the unused columns for prediction
        user_df = user_df.drop(columns=["Systolic blood pressure", "Diastolic blood pressure"])

        # applying preprocessor on Category columns to convert from str to number
        X_cate = preprocessor.transform(user_df[OBJECT_COL_NAME])

        # creating DataFrame of output from preprocessor
        X_cate = pd.DataFrame(X_cate.toarray(), columns=preprocessor.get_feature_names_out())

        # concatenating both numeric and Category columns in one DataFrame
        X = pd.concat([user_df[NUM_COL_NAME], X_cate], axis=1)

        # User input prediction
        prediction = model.predict(X)

        # returning user prediction
        if prediction[0] == 1:
            return "Its is good to know you don't have sleep disorder. It's still recommended to visit doctor if you have any symptoms."

        elif prediction[0] == 0:
            return "The model has predicted Insomnia as per you'r inputs it is recommended to visit a doctor."

        elif prediction[0] == 2:
            return "The model has predicted Apnea as per you'r inputs it is recommended to visit a doctor."
