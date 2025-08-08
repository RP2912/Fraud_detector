import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fraud_detection_app.app1.predict import predict_transaction
from fraud_detection_app.app1.schema import TransactionData

# Give 5 numerical features
sample_input = TransactionData(features=[0.2, -0.1, 0.4, 1.1, 3.5])
result = predict_transaction(sample_input)
print(result)
