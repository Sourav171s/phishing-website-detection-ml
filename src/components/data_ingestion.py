import sys #n Python, we import the sys module to interact with the Python interpreter and access system-specific parameters and functions.
import os
import numpy as np
import pandas as pd
from pymongo import MongoClient
#This is used to create, read, write, and extract .zip files
from zipfile import ZipFile
#If you want to work with file paths, including zip files, you're probably thinking of
from pathlib import Path
from src.constant import *
from src.exception import CustomException
from src.logger import logging
from src.data_access.phising_data import PhisingData
from src.utils.main_utils import MainUtils
from dataclasses import dataclass
from dotenv import load_dotenv
load_dotenv()

@dataclass
class DataIngestionConfig:
 #This sets the path for the data ingestion directory.
# It stores data ingestion files inside the 'artifact' folder, under a subfolder named 'data_ingestion'.
# The 'artifact_folder' path may include a timestamp to separate runs.
    data_ingestion_dir: str =os.path.join(artifact_folder,"data_ingestion")


class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.utils = MainUtils()

    def export_data_into_raw_data_dir(self) -> pd.DataFrame:
        '''
        Reads data from MongoDB and saves it into the raw data ingestion directory.
        '''
        try:
            logging.info("Exporting data from MongoDB")
            raw_batch_files_path = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(raw_batch_files_path, exist_ok=True)

            income_data = PhisingData(database_name=MONGO_DATABASE_NAME)
            logging.info(f"Saving exported data into feature store file path: {raw_batch_files_path}")
            
            for collection_name, dataset in income_data.export_collections_as_dataframe():
                logging.info(f"Shape of {collection_name}: {dataset.shape}")
                feature_store_file_path = os.path.join(raw_batch_files_path, collection_name + '.csv')
                print(f"feature_store_file_path-----{feature_store_file_path}")
                if dataset.empty:

                    print(f"Warning: Collection {collection_name} is empty!")
                else:

                    print(f"Saving data for {collection_name}, shape: {dataset.shape}")
                    print(dataset.head())  # <- Debug print

                dataset.to_csv(feature_store_file_path, index=False)
        
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_ingestion(self) -> Path:
        """
        Initiates the data ingestion process from MongoDB.
        """
        logging.info("Entered initiate_data_ingestion method of DataIngestion class")
        try:
            self.export_data_into_raw_data_dir()
            logging.info("Got the data from MongoDB")
            logging.info("Exited initiate_data_ingestion method of DataIngestion class")
            return self.data_ingestion_config.data_ingestion_dir
        except Exception as e:
            raise CustomException(e, sys) from e
