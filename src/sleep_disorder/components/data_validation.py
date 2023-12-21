import os

from sleep_disorder.entity import DataValidationConfig
from sleep_disorder.logging import logger
from sleep_disorder.utils.common import create_directories, get_size


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

        create_directories([self.config.root_dir])

    def get_data_validation(self):
        try:
            local_data_dir = os.path.join("artifacts", "data_ingestion")
            all_files = os.listdir(local_data_dir)

            validation_status = None

            if sorted(all_files) != sorted(self.config.ALL_REQUIRED_FILES):
                validation_status = False
                with open(self.config.STATUS_FILE, "w") as f:
                    f.write(f"VALIDATION STATUS: {validation_status}")
                    logger.info(f"Check if 'Data Ingestion Stage'  is completed!")

            else:
                validation_status = True
                with open(self.config.STATUS_FILE, "w") as f:
                    f.write(f"VALIDATION STATUS: {validation_status}")
                    logger.info(f"'Data Validation' successful.")

        except Exception as e:
            raise e
