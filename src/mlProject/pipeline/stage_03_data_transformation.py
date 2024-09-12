from mlProject import logger
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation

STAGE_NAME = " Data Transformation"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config = data_transformation_config)
        data_transformation.train_test_split()

if __name__ == "__main__":
    try:
        logger.info(f">>>>> {STAGE_NAME} stage started <<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>{STAGE_NAME} stage completed <<<<<")
    except Exception as e:
        raise e
