from src.Student_performance_prediction.Components.data_ingestion import DataIngestion
from src.Student_performance_prediction.Components.data_transformation import DataTransformation
from src.Student_performance_prediction.Components.model_trainer import ModelTrainer
# import os, sys

# from src.Student_performance_prediction.logger import logging
# from src.Student_performance_prediction.exception import CustomException
# import pandas as pd


ingest_obj = DataIngestion()
train_path, test_path = ingest_obj.initiate_ingestion()

data_transform = DataTransformation()
training_data, testing_data = data_transform.initiate_data_transformation(train_path, test_path)

model_trainer = ModelTrainer()
model_trainer.initiate_model_training(training_data, testing_data)
