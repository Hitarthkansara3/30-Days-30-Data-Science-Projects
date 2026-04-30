import streamlit as st
import pandas as pd
import joblib
import os
import traceback
import streamlit as st
st.title("Customer Churn App 🔥")
st.write("Frontend working")

# -----------------------------------
# Page Config
# -----------------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📉",
    layout="wide"
)

# -----------------------------------
# CSS
# -----------------------------------
st.markdown("""
<style>
.stButton>button{
    width:100%;
    background:linear-gradient(90deg,#00c6ff,#0072ff);
    color:white;
    border:none;
    border-radius:10px;
    height:3em;
    font-size:18px;
    font-weight:bold;
}
.result-box{
    padding:20px;
    border-radius:12px;
    text-align:center;
    font-size:24px;
    font-weight:bold;
    margin-top:20px;
}
</style>
""", unsafe_allow_html=True)

MODEL_PATH = "customer_churn_model.pkl"

# -----------------------------------
# Safe Model Loader
# -----------------------------------
@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        st.error("❌ customer_churn_model.pkl not found in project folder.")
        st.stop()

    try:
        model = joblib.load(MODEL_PATH)
        return model

    except Exception as e:
        st.error("❌ Failed to load model.")
        st.code(str(e))

        st.warning("""
Possible Reasons:
1. Model saved with different sklearn version  
2. Corrupted .pkl file  
3. Wrong file path  
4. Incompatible libraries
""")
        st.stop()

model = load_model()

# -----------------------------------
# Title
# -----------------------------------
st.title("📉 Customer Churn Prediction")
st.write("Predict customer churn using your trained ML model.")

# -----------------------------------
# Inputs
# -----------------------------------
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
    ["Electronic check", "Mailed check",
     "Bank transfer (automatic)", "Credit card (automatic)"]
)

monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
total = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)

# -----------------------------------
# Prediction
# -----------------------------------
if st.button("🔍 Predict Churn"):

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
        pred = model.predict(input_df)[0]

        if hasattr(model, "predict_proba"):
            prob = model.predict_proba(input_df)[0][1]
        else:
            prob = 0.0

        if pred == 1:
            st.markdown(f"""
            <div class="result-box" style="background:#ff4b4b;">
            ⚠️ Customer is Likely to Churn<br>
            Probability: {prob:.2%}
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown(f"""
            <div class="result-box" style="background:#00c853;">
            ✅ Customer Will Stay<br>
            Churn Probability: {prob:.2%}
            </div>
            """, unsafe_allow_html=True)

    except Exception as e:
        st.error("❌ Prediction Failed")
        st.code(str(e))

# -----------------------------------
# Footer
# -----------------------------------
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")