from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.state_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e


STATE_NAME = "Prepare base model"


try:
    logger.info(f">>>>>> Stage {STATE_NAME} Started <<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>> Stage {STATE_NAME} Completed <<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e
