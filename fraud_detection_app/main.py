from fastapi import FastAPI
from app.schema import TransactionData
from app.predict import predict_fraud

app=FastAPI()

@app.get('/')
def read_root():
    return {"message": "Welcome to the Fraud Detection API"}

@app.post("/predict")
def predict(data: TransactionData):
    result = predict_fraud(data.features)
    return {'prediction':result}