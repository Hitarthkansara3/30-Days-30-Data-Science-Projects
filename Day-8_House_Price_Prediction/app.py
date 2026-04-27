import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("house_price_model.pkl", "rb"))

st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

st.title("🏠 House Price Prediction App")
st.write("Fill house details and predict price")

# Numeric Inputs
area = st.number_input("Area (sq ft)", 500, 20000, 2000)
bedrooms = st.slider("Bedrooms", 1, 10, 3)
bathrooms = st.slider("Bathrooms", 1, 10, 2)
stories = st.slider("Stories", 1, 5, 2)
parking = st.slider("Parking", 0, 5, 1)

# Binary Inputs
mainroad = st.selectbox("Main Road Access", ["yes", "no"])
guestroom = st.selectbox("Guest Room", ["yes", "no"])
basement = st.selectbox("Basement", ["yes", "no"])
hotwaterheating = st.selectbox("Hot Water Heating", ["yes", "no"])
airconditioning = st.selectbox("Air Conditioning", ["yes", "no"])
prefarea = st.selectbox("Preferred Area", ["yes", "no"])

# Furnishing
furnishing = st.selectbox(
    "Furnishing Status",
    ["furnished", "semi-furnished", "unfurnished"]
)

# Predict Button
if st.button("Predict Price"):

    data = {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "stories": stories,
        "parking": parking,

        "mainroad_yes": 1 if mainroad == "yes" else 0,
        "guestroom_yes": 1 if guestroom == "yes" else 0,
        "basement_yes": 1 if basement == "yes" else 0,
        "hotwaterheating_yes": 1 if hotwaterheating == "yes" else 0,
        "airconditioning_yes": 1 if airconditioning == "yes" else 0,
        "prefarea_yes": 1 if prefarea == "yes" else 0,

        "furnishingstatus_semi-furnished": 1 if furnishing == "semi-furnished" else 0,
        "furnishingstatus_unfurnished": 1 if furnishing == "unfurnished" else 0,
    }

    input_df = pd.DataFrame([data])

    prediction = model.predict(input_df)[0]

    st.success(f"🏷️ Estimated House Price: ₹ {prediction:,.0f}")