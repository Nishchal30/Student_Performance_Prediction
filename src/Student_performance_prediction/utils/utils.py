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