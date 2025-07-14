# CKD Risk Prediction App

A web-based app using XGBoost to predict Chronic Kidney Disease (CKD) risk based on medical inputs.

## Features
- Streamlit frontend
- Google Sheets integration for data logging
- XGBoost backend model
- Real-time predictions

## Setup Instructions

1. Clone the repo
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Add your Google service credentials to `.streamlit/secrets.toml`
4. Add your trained model to `model/xgb_model.pkl`
5. Run:
```bash
streamlit run app.py
```