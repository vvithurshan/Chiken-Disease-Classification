from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.evaluation import Evaluation
from cnnClassifier import logger

STAGE_NAME = "Evaluation Stage"

class EvalutionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_validation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<<")
        obj = EvalutionPipeline()
        obj.main()
        logger.info(f">>>> Stage {STAGE_NAME} Completed <<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e

