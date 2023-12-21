from sleep_disorder.logging import logger
from sleep_disorder.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from sleep_disorder.pipeline.stage_02_data_validation import DataValidationPipeline
from sleep_disorder.pipeline.stage_03_data_transform import DataTransformPipeline
from sleep_disorder.pipeline.stage_04_model_train_evaluate import (
    ModelBuildEvaluatePipeline,
)

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f"----->{STAGE_NAME} started<-----")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f"----->{STAGE_NAME} completed<-----\n\nX====================X")
except Exception as e:
    raise e


STAGE_NAME = "Data Validation"
try:
    logger.info(f"----->{STAGE_NAME} started<-----")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f"----->{STAGE_NAME} completed<-----\n\nX====================X")
except Exception as e:
    raise e

STAGE_NAME = "Data Transform"
try:
    logger.info(f"----->{STAGE_NAME} started<-----")
    data_transform = DataTransformPipeline()
    data_transform.main()
    logger.info(f"----->{STAGE_NAME} completed<-----\n\nX====================X")
except Exception as e:
    raise e

STAGE_NAME = "Model Train Test"
try:
    logger.info(f"----->{STAGE_NAME} started<-----")
    model_build_evaluate = ModelBuildEvaluatePipeline()
    model_build_evaluate.main()
    logger.info(f"----->{STAGE_NAME} completed<-----\n\nX====================X")
except Exception as e:
    raise e
