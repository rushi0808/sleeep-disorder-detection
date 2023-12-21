import os
import urllib.request as request
from pathlib import Path

from sleep_disorder.entity import DataIngestionConfig
from sleep_disorder.logging import logger
from sleep_disorder.utils.common import create_directories, get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

        create_directories([self.config.root_dir])

    def get_data(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                filename, headers = request.urlretrieve(self.config.source_URL, self.config.local_data_file)
                logger.info(f"File {filename} downloaded with following information:\n{headers}")
            else:
                logger.info(
                    f"File {self.config.local_data_file} already exists with size {get_size(Path(self.config.local_data_file))}"
                )
        except Exception as e:
            raise e
