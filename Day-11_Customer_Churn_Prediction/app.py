import streamlit as st
import pandas as pd
import joblib
import os

# -----------------------------------
# Page Config
# -----------------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📉",
    layout="wide"
)

# -----------------------------------
# Load Model
# -----------------------------------
MODEL_PATH = "customer_churn_model.pkl"

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        st.error("❌ customer_churn_model.pkl file not found.")
        st.stop()

    try:
        return joblib.load(MODEL_PATH)
    except Exception as e:
        st.error("❌ Failed to load model.")
        st.code(str(e))
        st.stop()

model = load_model()

# -----------------------------------
# Title
# -----------------------------------
st.title("📉 Customer Churn Prediction")
st.write("Predict whether a telecom customer will **churn or stay**.")

# -----------------------------------
# Input Form
# -----------------------------------
with st.form("prediction_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        senior = st.selectbox("Senior Citizen", [0, 1])
        partner = st.selectbox("Partner", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["Yes", "No"])
        tenure = st.slider("Tenure Months", 0, 72, 12)

    with col2:
        phone = st.selectbox("Phone Service", ["Yes", "No"])
        multiple = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
        internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
        online_sec = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
        online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])

    with col3:
        device = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
        tech = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
        tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
        movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
        contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])

    paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=70.0)
    total = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=1000.0)

    submitted = st.form_submit_button("🔍 Predict")

# -----------------------------------
# Prediction
# -----------------------------------
if submitted:
    input_df = pd.DataFrame([{
        "Gender": gender,
        "Senior Citizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "Tenure Months": tenure,
        "Phone Service": phone,
        "Multiple Lines": multiple,
        "Internet Service": internet,
        "Online Security": online_sec,
        "Online Backup": online_backup,
        "Device Protection": device,
        "Tech Support": tech,
        "Streaming TV": tv,
        "Streaming Movies": movies,
        "Contract": contract,
        "Paperless Billing": paperless,
        "Payment Method": payment,
        "Monthly Charges": monthly,
        "Total Charges": total
    }])

    try:
        prediction = model.predict(input_df)[0]

        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(input_df)[0][1]
        else:
            probability = 0.0

        st.subheader("Prediction Result")

        if prediction == 1:
            st.error(f"⚠️ Customer is Likely to Churn")
            st.write(f"Churn Probability: **{probability:.2%}**")
        else:
            st.success("✅ Customer Will Stay")
            st.write(f"Churn Probability: **{probability:.2%}**")

    except Exception as e:
        st.error("❌ Prediction failed.")
        st.code(str(e))

# -----------------------------------
# Footer
# -----------------------------------
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")