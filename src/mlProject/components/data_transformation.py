import os
from pathlib import Path
import pandas as pd
from mlProject import logger
from sklearn.model_selection import train_test_split
from mlProject.utils.common import *
from mlProject.config.configuration import ConfigurationManager
from mlProject.entity.config_entity import  DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index = False)

        logger.info("splitted the data into traina and test data sets")

        print(train.shape)
        print(test.shape)