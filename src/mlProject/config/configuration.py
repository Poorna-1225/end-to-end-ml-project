from mlProject.constants import *
from mlProject.utils.common import *
from mlProject.entity.config_entity import DataIngestionConfig


"""
this is a configurationmanager class and this is used to configure all the values to 
data_ingestion, data_validation and other components too.

"""



CONFIG_FILE_PATH =Path('config/config.yaml')

class ConfigurationManager:
    def __init__(
        self):

        self.config = read_yaml(CONFIG_FILE_PATH)
        self.params = read_yaml(PARAMS_FILE_PATH)
        self.schema = read_yaml(SCHEMA_FILE_PATH)

        create_directories([self.config.artifacts_root])
        

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
