import streamlit as st
import requests

st.title("💸 Fraud Detection App")

features = st.text_input("Enter 5 features (comma-separated):")

if st.button("Predict"):
    try:
        features_list = [float(x.strip()) for x in features.split(",")]
        response = requests.post(
            "http://localhost:8000/predict",  # change to AWS URL after deploy
            json={"features": features_list}
        )
        result = response.json()
        st.success(f"Prediction: {'FRAUD' if result['prediction'] else 'Not Fraud'}")
    except Exception as e:
        st.error(f"Error: {e}")
