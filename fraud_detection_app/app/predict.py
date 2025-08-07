# import joblib
# import numpy as np
# import logging
# from datetime import datetime

# # load the model
# model=joblib.load('model/fraud_model.pkl')
# # set logger
# logging.basicConfig(
#     filename='logs/predictions.log',
#     level=logging.INFO,
# )
# def predict_fraud(features: list[float],source:str ='unknown') -> int:
#     prediction=model.predict([features])[0]
#     log_entry =f"{datetime.now()} - Source: {source}, Features: {features}, Prediction: {prediction}"

#     logging.info(log_entry)
#     return int(prediction)


import joblib
import numpy as np
import logging
from datetime import datetime
import os

# === Setup Absolute Log Path ===

# This gets the directory of this predict.py file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go up one level (to fraud_detection_app/)
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))

# Ensure logs folder exists
LOG_DIR = os.path.join(PROJECT_ROOT, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Full path to log file
LOG_FILE = os.path.join(LOG_DIR, "predictions.log")

# === Logging Config ===
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# === Load the model ===
MODEL_PATH = os.path.join(PROJECT_ROOT, "model", "fraud_model.pkl")
model = joblib.load(MODEL_PATH)

# === Prediction Function ===
def predict_fraud(features: list[float], source: str = 'unknown') -> int:
    prediction = model.predict([features])[0]
    log_entry = f"{datetime.now()} - Source: {source}, Features: {features}, Prediction: {prediction}"
    logging.info(log_entry)
    return int(prediction)
