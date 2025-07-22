import streamlit as st
import numpy as np
from predict import load_model, make_prediction

st.set_page_config(page_title="Chronic Kidney Disease Prediction", layout="centered")
st.title("🩺 Chronic Kidney Disease Risk Predictor")

st.markdown("Please enter the following medical information:")

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
tchol = st.number_input("Total Cholesterol")
ldl = st.number_input("LDL")
hdl = st.number_input("HDL")

if st.button("🔍 Predict"):
    model = load_model()

    input_data = np.array([[ 
        age,
        1 if female == "Female" else 0,
        bmi,
        1 if smoker == "Yes" else 0,
        1 if obese == "Yes" else 0,
        1 if activity == "Yes" else 0,
        1 if fam_htn == "Yes" else 0,
        1 if fam_dm == "Yes" else 0,
        sbp,
        dbp,
        1 if anemia == "Yes" else 0,
        total_chol,
        ldl,
        hdl
    ]])

    prediction = make_prediction(model, input_data)

    if prediction == 1:
        st.error("🚨 Likely to have Chronic Kidney Disease. Please consult a doctor for future treatment.")
    else:
        st.success("✅ Risk of Chronic Kidney Disease is low. Maintain a healthy lifestyle.")
