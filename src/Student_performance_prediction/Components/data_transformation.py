import pandas as pd
import numpy as np
from src.Student_performance_prediction.logger import logging
from src.Student_performance_prediction.exception import CustomException
from src.Student_performance_prediction.utils.utils import save_obj
import os, sys
from pathlib import Path
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from dataclasses import dataclass

@dataclass
class DataTransformerConfig:

    preprocessor_obj_path : str = os.path.join(Path(os.getcwd()).resolve().parents[2],"artifacts", "preprocessor.pkl")


class DataTransformation:

    def __init__(self):

        self.data_transform_config = DataTransformerConfig()

    def get_data_transformation(self):

        try:
            logging.info("Data transformation started here")

            categorical_features = ['gender',
                                    'race/ethnicity',
                                    'parental level of education',
                                    'lunch',
                                    'test preparation course']
            numerical_features = ['reading score', 'writing score']


            logging.info("Pipeline started here")


            numerical_pipeline = Pipeline(
                steps = [
                    ("Imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )

            categorical_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("onehotencoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False))
                ]
             )

            logging.info("Pipeline created for numerical & categorical features")

            preprocessor = ColumnTransformer(
                [
                    ("numerical_pipeline", numerical_pipeline, numerical_features),
                    ("categorical_pipeline", categorical_pipeline, categorical_features)
                ]
            )

            return preprocessor

        except Exception as e:
            logging.info("Error occured in data transformation file in get_data_transformation method")
            raise CustomException(e, sys)


    def initiate_data_transformation(self, train_data, test_data):  

        try:
            train_data = pd.read_csv(train_data)
            test_data = pd.read_csv(test_data)

            logging.info("train & test data read successfully")

            preprocessing_obj = self.get_data_transformation()

            target_column = 'math score'

            final_train_df = train_data.drop(target_column, axis = 1)
            target_train_df = train_data[target_column]

            final_test_df = test_data.drop(target_column, axis = 1)
            target_test_df = test_data[target_column]

            train_data_after_preprocess = preprocessing_obj.fit_transform(final_train_df)
            test_data_after_preprocess = preprocessing_obj.transform(final_test_df)

            logging.info("Successfully applied preprocessor object on train & test dataset")

            train_arr = np.c_[train_data_after_preprocess, np.array(target_train_df)]
            test_arr = np.c_[test_data_after_preprocess, np.array(target_test_df)]

            save_obj(
                filepath = self.data_transform_config.preprocessor_obj_path,
                obj=preprocessing_obj
            )

            logging.info("preprocessing pickle object created")

            return(
                train_arr, test_arr,self.data_transform_config.preprocessor_obj_path
            )

        except Exception as e:
            logging.info("Error occured in data transformation file in initiate_data_transformation method")
            raise CustomException(e, sys)

