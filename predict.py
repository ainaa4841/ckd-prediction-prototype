import pickle
import numpy as np

def load_model():
    with open("model/xgb_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

def make_prediction(model, input_array):
    prediction = model.predict(input_array)
    return int(prediction[0])
