import joblib
import gspread
from google.oauth2.service_account import Credentials
import datetime
import streamlit as st

# Load model
model = joblib.load("model/xgb_model.pkl")

# Google Sheets config
scope = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=scope
)
client = gspread.authorize(creds)
sheet = client.open("CKD_Log").sheet1

def predict_ckd(features):
    return int(model.predict(features)[0])

def log_to_gsheet(data_row, prediction):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_row = [now] + data_row + [prediction]
    sheet.append_row(full_row)