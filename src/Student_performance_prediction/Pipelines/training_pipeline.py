from src.Student_performance_prediction.Components.data_ingestion import DataIngestion
import os, sys

from src.Student_performance_prediction.logger import logging
from src.Student_performance_prediction.exception import CustomException
import pandas as pd


ingest_obj = DataIngestion()

train_path, test_path = ingest_obj.initiate_ingestion()