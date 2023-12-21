from sleep_disorder.components.data_transform import DataTransform
from sleep_disorder.config.configuration import ConfigurationManager


class DataTransformPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_transform_config = config.get_data_transform_config()
        data_transform = DataTransform(config=data_transform_config)
        df = data_transform.get_local_data()
        processor, train, test = data_transform.get_data_transform(df=df)
        data_transform.dump_preprocessor(processor=processor)
        data_transform.save_train_test_file(train=train, test=test)
