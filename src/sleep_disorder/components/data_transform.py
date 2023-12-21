import os
import pickle

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from sleep_disorder.entity import DataTransformConfig
from sleep_disorder.logging import logger
from sleep_disorder.utils.common import create_directories


class DataTransform:
    def __init__(self, config: DataTransformConfig):
        self.config = config

        create_directories([self.config.root_dir, self.config.preprocessor_dir])

    def get_local_data(self) -> pd.DataFrame:
        local_data_file = os.path.join("artifacts", "data_ingestion", "local_data.csv")

        df = pd.read_csv(local_data_file)

        return df

    def get_data_transform(self, df: pd.DataFrame):
        df = df.drop(columns='Person ID')
        df['Sleep Disorder'].fillna("No", inplace=True)
        df['BP Ratio'] = df['Blood Pressure'].apply(lambda x: round(float(x.split("/")[0]) / float(x.split("/")[1]), 2))
        X = df.drop(columns=['Sleep Disorder', 'Blood Pressure'])
        y = df['Sleep Disorder']
        cate_col = X.select_dtypes(include='object').columns
        num_col = X.select_dtypes(exclude='object').columns
        cate_pipe = Pipeline([("OneHotEncoder", OneHotEncoder())])

        preprocessor = ColumnTransformer([("cate", cate_pipe, cate_col)])

        X_cate = preprocessor.fit_transform(X[cate_col])
        X_cate = pd.DataFrame.sparse.from_spmatrix(X_cate, columns=preprocessor.get_feature_names_out())

        X = pd.concat([X[num_col], X_cate], axis=1)
        y = y.replace({"No": 0, "Sleep Apnea": 1, "Insomnia": 2})
        data = pd.concat([X, y], axis=1)
        train, test = train_test_split(data, test_size=0.3)

        return preprocessor, train, test

    def dump_preprocessor(self, processor):
        with open(self.config.preprocessor_file, "wb") as pkl_file:
            pickle.dump(processor, pkl_file)
            logger.info(f"Preprocessor Saved to path: {self.config.preprocessor_file}")

    def save_train_test_file(self, train: pd.DataFrame, test: pd.DataFrame):
        try:
            train.to_csv(self.config.train_data_file, index=False)
            logger.info(f"Train Data Saved to path: {self.config.train_data_file}")
            test.to_csv(self.config.test_data_file, index=False)
            logger.info(f"Test Data Saved to path: {self.config.train_data_file}")
        except Exception as e:
            raise e
