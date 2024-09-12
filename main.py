from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

"""STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========')

except Exception as e:
    logger.exception(e)
    raise e
"""

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
