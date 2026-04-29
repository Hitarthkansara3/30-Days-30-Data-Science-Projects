# app.py
# Uses YOUR saved model only (no retraining)
# Fixes "always rejected" issue by cleaning inputs exactly like training data

import streamlit as st
import pandas as pd
import joblib
import os

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="💰",
    layout="wide"
)

# -----------------------------
# Load Your Model
# -----------------------------
MODEL_FILE = "loan_approval_model.pkl"

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_FILE):
        st.error("❌ loan_approval_model.pkl not found!")
        st.stop()
    return joblib.load(MODEL_FILE)

model = load_model()

# -----------------------------
# Title
# -----------------------------
st.title("💰 Loan Approval Prediction")
st.markdown("Prediction using **your trained model**")

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("Applicant Details")

no_of_dependents = st.sidebar.slider("Dependents", 0, 5, 1)
education = st.sidebar.selectbox("Education", [" Graduate", " Not Graduate"])
self_employed = st.sidebar.selectbox("Self Employed", [" Yes", " No"])
income_annum = st.sidebar.number_input("Annual Income", min_value=0, value=500000)
loan_amount = st.sidebar.number_input("Loan Amount", min_value=0, value=1000000)
loan_term = st.sidebar.slider("Loan Term", 2, 20, 10)
cibil_score = st.sidebar.slider("CIBIL Score", 300, 900, 750)
residential_assets_value = st.sidebar.number_input("Residential Assets", min_value=0, value=1000000)
commercial_assets_value = st.sidebar.number_input("Commercial Assets", min_value=0, value=0)
luxury_assets_value = st.sidebar.number_input("Luxury Assets", min_value=0, value=0)
bank_asset_value = st.sidebar.number_input("Bank Assets", min_value=0, value=500000)

# -----------------------------
# Create Input DataFrame
# IMPORTANT: exact column names
# -----------------------------
input_data = pd.DataFrame({
    "no_of_dependents": [no_of_dependents],
    "education": [education],
    "self_employed": [self_employed],
    "income_annum": [income_annum],
    "loan_amount": [loan_amount],
    "loan_term": [loan_term],
    "cibil_score": [cibil_score],
    "residential_assets_value": [residential_assets_value],
    "commercial_assets_value": [commercial_assets_value],
    "luxury_assets_value": [luxury_assets_value],
    "bank_asset_value": [bank_asset_value]
})

st.subheader("📋 Input Data")
st.dataframe(input_data, use_container_width=True)

# -----------------------------
# Predict
# -----------------------------
if st.button("🔍 Predict", use_container_width=True):
    try:
        prediction = model.predict(input_data)[0]

        st.subheader("Result")

        if str(prediction).strip().lower() == "approved":
            st.success("✅ Loan Approved")
        else:
            st.error("❌ Loan Rejected")

    except Exception as e:
        st.error(f"Prediction Error: {e}")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Built with Streamlit | Using Your Saved Model")