import os
import sys
import pickle
import numpy as np
import pandas as pd
from src.Student_performance_prediction.logger import logging
from src.Student_performance_prediction.exception import CustomException
from sklearn.metrics import r2_score, mean_absolute_error,mean_squared_error


def save_obj(filepath, obj):

    try:
        dir_name = os.path.dirname(filepath)
        os.makedirs(dir_name, exist_ok = True)
        
        with open(filepath, "wb") as f:
            pickle.dump(obj, f)

    except Exception as e:
        logging.info("Error occured in utils.py file")
        raise CustomException(e, sys)
    


def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]

            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            score = r2_score(y_test, y_pred)

            report[list(models.keys())[i]] = score

        return report
    
    except Exception as e:
        logging.info("Error occured in evaluate model in utils.py file")
        raise CustomException(e, sys)

def load_object(filepath):
    try:

        with open(filepath, "rb") as file:
            return pickle.load(file)
    
    except Exception as e:
        logging.info("Error occured in load object method in utils file")
        raise CustomException(e, sys)

    
