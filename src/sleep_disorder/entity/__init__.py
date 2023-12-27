from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path


@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: Path
    ALL_REQUIRED_FILES: str


@dataclass
class DataTransformConfig:
    root_dir: Path
    preprocessor_dir: Path
    preprocessor_file: Path
    train_data_file: Path
    test_data_file: Path


@dataclass
class ModelBuildEvaluateConfig:
    root_dir: Path
    model_dir: Path
    model_file: Path
    train_data_file: Path
    test_data_file: Path
    model_results_file: Path


@dataclass
class PredictionConfig:
    model_file: Path
    preprocessor_file: Path
