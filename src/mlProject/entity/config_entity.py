from dataclasses import dataclass
from pathlib import Path


# these are the variable we mentioned in config.yaml under data_ingestion
# now here we are returning the each variable data type
@dataclass(frozen =True) #frozen = True helps in not allowing to add any other variable names in this class
class DataIngestionConfig:
    root_dir: Path #artifacts/data_ingestion is the directory as value we mentioned in config.yaml
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen= True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema:dict


@dataclass(frozen = True)
class DataTransformationConfig:
    root_dir : Path
    data_path: Path