
import pandas as pd
import numpy as mp
from src.Student_performance_prediction.logger import logging
from src.Student_performance_prediction.exception import CustomException

from sklearn.model_selection import train_test_split
import os, sys
from pathlib import Path 
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:

    raw_data_path : str = os.path.join(Path(os.getcwd()).resolve().parents[2],"artifacts", "raw_data.csv")
    train_data_path :str = os.path.join(Path(os.getcwd()).resolve().parents[2],"artifacts", "train.csv")
    test_data_path :str = os.path.join(Path(os.getcwd()).resolve().parents[2],"artifacts", "test.csv")

class DataIngestion:

    def __init__(self): 
        
        self.ingestion_config = DataIngestionConfig()

    def initiate_ingestion(self):
        try:
            logging.info("The data ingestion will start here")

            data = pd.read_csv(os.path.join(Path(os.getcwd()).resolve().parents[2], "notebooks", "data", "student.csv"))
            print(data.head())

            logging.info("The data read successfully")

            os.makedirs(os.path.join(Path(os.getcwd()).resolve().parents[2], "artifacts"), exist_ok = True)

            data.to_csv(os.path.join(Path(os.getcwd()).resolve().parents[2], self.ingestion_config.raw_data_path), index=False)
            logging.info("Saved the raw data in artifacts folder")

            train_data, test_data = train_test_split(data, test_size=0.3)
            logging.info("train test split completed")

            train_data.to_csv(os.path.join(Path(os.getcwd()).resolve().parents[2],self.ingestion_config.train_data_path), index=False)
            test_data.to_csv(os.path.join(Path(os.getcwd()).resolve().parents[2],self.ingestion_config.test_data_path), index=False)

            logging.info("Saved the train & test data in artifacts folder")
            logging.info("The data ingestion part is completed here")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info("Error occured in data ingestion")
            raise CustomException(e, sys)

