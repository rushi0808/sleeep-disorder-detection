from sleep_disorder.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from sleep_disorder.entity import (
    DataIngestionConfig,
    DataTransformConfig,
    DataValidationConfig,
    ModelBuildEvaluateConfig,
    PredictionConfig,
)
from sleep_disorder.utils.common import create_directories, read_yaml


class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
        )

        return data_validation_config

    def get_data_transform_config(self) -> DataTransformConfig:
        config = self.config.data_transform

        data_transform_config = DataTransformConfig(
            root_dir=config.root_dir,
            preprocessor_dir=config.preprocessor_dir,
            preprocessor_file=config.preprocessor_file,
            train_data_file=config.train_data_file,
            test_data_file=config.test_data_file,
        )

        return data_transform_config

    def get_model_build_evaluate_config(self) -> ModelBuildEvaluateConfig:
        config = self.config.model_build_evaluate

        model_build_evaluate_config = ModelBuildEvaluateConfig(
            root_dir=config.root_dir,
            model_dir=config.model_dir,
            model_file=config.model_file,
            train_data_file=config.train_data_file,
            test_data_file=config.test_data_file,
            model_results_file=config.model_results_file,
        )

        return model_build_evaluate_config

    def get_prediction_config(self) -> PredictionConfig:
        config = self.config.prediction

        prediction_config = PredictionConfig(model_file=config.model_file, preprocessor_file=config.preprocessor_file)

        return prediction_config
