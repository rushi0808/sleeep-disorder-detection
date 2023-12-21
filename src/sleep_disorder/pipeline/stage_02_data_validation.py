from sleep_disorder.components.data_validation import DataValidation
from sleep_disorder.config.configuration import ConfigurationManager


class DataValidationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.get_data_validation()
