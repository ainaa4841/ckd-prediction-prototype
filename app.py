import streamlit as st
import numpy as np
from predict import load_model, make_prediction

st.title("🩺 Chronic Kidney Disease Risk Predictor")

st.markdown("Enter your health data to check for CKD risk:")

age = st.number_input("Age", 0, 120)
female = st.selectbox("Sex", ["Male", "Female"]) == "Female"
bmi = st.number_input("BMI")
smoker = st.selectbox("Smoker", ["No", "Yes"]) == "Yes"
obese = st.selectbox("Obese", ["No", "Yes"]) == "Yes"
activity = st.selectbox("Activity Level", ["Sedentary (1/2)", "Active (3+)"]) == "Active (3+)"
fam_hyp = st.selectbox("Family History of Hypertension", ["No", "Yes"]) == "Yes"
fam_db = st.selectbox("Family History of Diabetes", ["No", "Yes"]) == "Yes"
sbp = st.number_input("Systolic Blood Pressure (SBP)")
dbp = st.number_input("Diastolic Blood Pressure (DBP)")
anemia = st.selectbox("Anemia", ["No", "Yes"]) == "Yes"
tchol = st.number_input("Total Cholesterol")
ldl = st.number_input("LDL")
hdl = st.number_input("HDL")

if st.button("Predict"):
    features = np.array([[
        age, int(female), bmi, int(smoker), int(obese), int(activity),
        int(fam_hyp), int(fam_db), sbp, dbp, int(anemia), tchol, ldl, hdl
    ]])

    result = predict_ckd(features)

    if result == 1:
        st.error("⚠️ Likely to have Chronic Kidney Disease. Please consult a doctor.")
    else:
        st.success("✅ Risk of CKD is low. Maintain a healthy lifestyle.")
