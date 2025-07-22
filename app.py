import streamlit as st
import numpy as np
from predict import load_model, make_prediction

st.set_page_config(page_title="Chronic Kidney Disease Prediction", layout="centered")
st.title("🩺 Chronic Kidney Disease Risk Predictor")

st.markdown("Please enter the following medical information:")

# Input fields
age = st.number_input("Age", 0, 120)
female = st.selectbox("Sex", ["Male", "Female"]) == "Female"
bmi = st.number_input("BMI")
smoker = st.selectbox("Smoker", ["No", "Yes"]) == "Yes"
obese = st.selectbox("Obese", ["No", "Yes"]) == "Yes"
activity = st.selectbox("Activity Level", ["Sedentary (1/2)", "Active (3+)"]) == "Active (3+)"
fam_htn = st.selectbox("Family History of Hypertension", ["No", "Yes"]) == "Yes"
fam_dm = st.selectbox("Family History of Diabetes", ["No", "Yes"]) == "Yes"
sbp = st.number_input("Systolic Blood Pressure (SBP)")
dbp = st.number_input("Diastolic Blood Pressure (DBP)")
anemia = st.selectbox("Anemia", ["No", "Yes"]) == "Yes"
total_chol = st.number_input("Total Cholesterol")
ldl = st.number_input("LDL")
hdl = st.number_input("HDL")

# Predict button
if st.button("🔍 Predict"):
    model = load_model()

    input_data = np.array([[ 
        age,
        int(female),
        bmi,
        int(smoker),
        int(obese),
        int(activity),
        int(fam_htn),
        int(fam_dm),
        sbp,
        dbp,
        int(anemia),
        total_chol,
        ldl,
        hdl
    ]])

    prediction = make_prediction(model, input_data)

    if prediction == 1:
        st.error("🚨 Likely to have Chronic Kidney Disease. Please consult a doctor.")
    else:
        st.success("✅ Low risk of Chronic Kidney Disease. Keep maintaining a healthy lifestyle!")
