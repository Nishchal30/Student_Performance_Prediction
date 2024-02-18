import os, sys
from pathlib import Path
import pandas as pd

from src.Student_performance_prediction.logger import logging
from src.Student_performance_prediction.exception import CustomException
from src.Student_performance_prediction.utils.utils import load_object


class PredictPipeline:

    def __init__(self) -> None:
        pass

    def predict(self, features):
        try:
            preprocessor_path = os.path.join(Path(os.getcwd()), "artifacts", "preprocessor.pkl")
            model_path = os.path.join(Path(os.getcwd()), "artifacts", "model_trainer.pkl")

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            scaled_data = preprocessor.transform(features)
            prediction = model.predict(scaled_data)

            return prediction
        
        except Exception as e:
            logging.info("Error occured in prediction pipeline file")
            raise CustomException (e,sys)
        


class CustomData:

    def __init__(self, 
                 gender:str,
                 race_ethinicity:str,
                 parental_level_of_education:str,
                 lunch:str,
                 test_preparation_course:str,
                 reading_score:float,
                 writing_score:float
    ):
        
        self.gender = gender
        self.race_ethinicity = race_ethinicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score
    

    def get_data_as_df(self):

        try:
            custom_data_input_dict = {
                "gender":[self.gender],
                "race_ethinicity":[self.race_ethinicity],
                "parental_level_of_education":[self.parental_level_of_education],
                "lunch":[self.lunch],
                "test_preparation_course":[self.test_preparation_course],
                "reading_score":[self.reading_score],
                "writing_score":[self.writing_score]
            }

            data = pd.DataFrame(custom_data_input_dict)
            logging.info("The dataframe has been created")
            return data
        
        except Exception as e:
            logging.info("The error occured in get_data_as_df method in prediction pipeline file")
            raise CustomException(e, sys)