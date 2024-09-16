from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_training import ModelTrainerTrainingPipeline
from mlProject.pipeline.stage_05_model_evalution import ModelEvaluationTrainingPipeline



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========')

except Exception as e:
    logger.exception(e)
    raise e


#checking if data validation is working good
STAGE_NAME = " Data validation " 
try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x')

except Exception as e:
    logger.exception(e)
    raise e


#checking if data transformation is working

STAGE_NAME = "Data Transformation"
try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x')

except Exception as e:
    logger.exception(e)
    raise e

# chekcing if model trianer is working good
STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   model_train = ModelTrainerTrainingPipeline()
   model_train.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Model evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelEvaluationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e