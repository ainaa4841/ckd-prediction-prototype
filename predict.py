import pickle
import numpy as np
import joblib

def load_model():
    with open("model/xgb_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

def load_scaler():
    scaler = joblib.load("model/scaler.pkl")
    return scaler

def make_prediction(model, scaler, input_array):
    scaled_input = scaler.transform(input_array)
    prediction = model.predict(scaled_input)
    return int(prediction[0])
