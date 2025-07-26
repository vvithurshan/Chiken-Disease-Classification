from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier import logger
from cnnClassifier.pipeline.state_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifier.pipeline.state_04_evaluation import EvalutionPipeline


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


STATE_NAME = "Training"

try:
    logger.info(f">>>>>> Stage {STATE_NAME} Started <<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>> Stage {STATE_NAME} Completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Evaluation Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<<")
    obj = EvalutionPipeline()
    obj.main()
    logger.info(f">>>> Stage {STAGE_NAME} Completed <<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e