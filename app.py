import streamlit as st
import numpy as np
from predict import load_model, load_scaler, make_prediction

st.set_page_config(page_title="Chronic Kidney Disease Prediction", layout="centered")
st.title("🩺 Chronic Kidney Disease Prediction")

st.markdown("Please enter the following medical information:")

# Input fields
age = st.number_input("Enter Age", 0, 120)
female = st.selectbox("Gender (Male/Female)", ["Male", "Female"]) == "Female"
bmi = st.number_input("Enter BMI", 10, 80)
smoker = st.selectbox("Smoker (Choose Yes/No)", ["No", "Yes"]) == "Yes"
obese = st.selectbox("Obese (Choose Yes/No)", ["No", "Yes"]) == "Yes"
activity = st.selectbox("Activity Level", ["Sedentary (1/2)", "Active (3+)"]) == "Active (3+)"
fam_htn = st.selectbox("Family History of Hypertension (Choose Yes/No)", ["No", "Yes"]) == "Yes"
fam_dm = st.selectbox("Family History of Diabetes (Choose Yes/No)", ["No", "Yes"]) == "Yes"
sbp = st.number_input("Systolic Blood Pressure (mmHG)", 60, 300)
dbp = st.number_input("Diastolic Blood Pressure (mmHG)",30, 200)
anemia = st.selectbox("Anemia (Choose Yes/No)", ["No", "Yes"]) == "Yes"
total_chol = st.number_input("Total Cholesterol (mg/dL)", 100, 1000)
ldl = st.number_input("Low-Density Lipoprotein (mg/dL)", 30, 600)
hdl = st.number_input("High-Density Lipoprotein (mg/dL)", 20, 200)

if st.button("🔍 Predict"):
    if any([
        age < 0 or age > 120,
        bmi < 10 or bmi > 80,
        sbp < 60 or sbp > 300,
        dbp < 30 or dbp > 200,
        total_chol < 100 or total_chol > 1000,
        ldl < 30 or ldl > 600,
        hdl < 20 or hdl > 200
    ]):
        st.warning("⚠️ Please re-enter valid data.")
    else:
        model = load_model()
        scaler = load_scaler()

        input_data = np.array([[ 
            age,
            1 if female else 0,
            bmi,
            1 if smoker else 0,
            1 if obese else 0,
            1 if activity else 0,
            1 if fam_htn else 0,
            1 if fam_dm else 0,
            sbp,
            dbp,
            1 if anemia else 0,
            total_chol,
            ldl,
            hdl
        ]])

        prediction = make_prediction(model, scaler, input_data)

        if prediction == 1:
            st.error("🚨 Likely to have Chronic Kidney Disease. Please consult a doctor for future treatment.")
        else:
            st.success("✅ Risk of Chronic Kidney Disease is low. Maintain a healthy lifestyle.")
