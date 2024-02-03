import os, sys
import pandas as pd
import numpy as np
from pathlib import Path

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor

from src.Student_performance_prediction.logger import logging
from src.Student_performance_prediction.exception import CustomException
from src.Student_performance_prediction.utils.utils import save_obj, evaluate_model


class ModelTrainerConfig:
    model_trainer_config_file : str = os.path.join(Path(os.getcwd()).resolve().parents[2],"artifacts", "model_trainer.pkl")


class ModelTrainer:

    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self, train_data_path, test_data_path):
        try:
            logging.info("Model training will start here")

            train_data = pd.DataFrame(train_data_path)
            test_data = pd.DataFrame(test_data_path)

            logging.info("split dependent & independent variables from train & test data")

            X_train, y_train, X_test, y_test = (
                train_data.iloc[:,:-1],
                train_data.iloc[:,-1],
                test_data.iloc[:,:-1],
                test_data.iloc[:,-1]
            )

            models = {
                "LinearRegression": LinearRegression(),
                "RidgeRegression": Ridge(),
                "LassoRegression": Lasso(),
                "DecisionTreeRegressor": DecisionTreeRegressor(),
                "RandomForestRegressor" : RandomForestRegressor(),
                "AdaBoostRegressor" : AdaBoostRegressor(),
                "GradientBoostRegressor" : GradientBoostingRegressor()
            }

            model_report : dict = evaluate_model(X_train, y_train, X_test, y_test, models)

            print(model_report)
            print("\n==================================================================\n")
            logging.info(f"Model report: {model_report}")

            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]

            print(f"Best model found, model name: {best_model_name}, R2_score: {best_model_score}")
            print("\n==================================================================\n")
            logging.info(f"Best model found, model name: {best_model_name}, R2_score: {best_model_score}")

            save_obj(
                self.model_trainer_config.model_trainer_config_file,
                best_model
            )

            logging.info("model training is completed and pickle file has been saved")

        except Exception as e:
            logging.info("Error occured in model trainer file")
            raise CustomException (e, sys)
