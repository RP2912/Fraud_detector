import joblib
import numpy as np
import logging
from datetime import datetime

# load the model
model=joblib.load('model/fraud_model.pkl')
# set logger
logging.basicConfig(
    filename='logs/predictions.log',
    level=logging.INFO,
)
def predict_fraud(features: list[float],source:str ='unknown') -> int:
    prediction=model.predict([features])[0]
    log_entry =f"{datetime.now()} - Source: {source}, Features: {features}, Prediction: {prediction}"

    logging.info(log_entry)
    return int(prediction)