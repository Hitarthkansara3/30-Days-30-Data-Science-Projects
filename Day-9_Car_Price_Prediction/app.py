# app.py
# Safe Streamlit App
# Automatically trains model if .pkl not found or broken

import os
import joblib
import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 Car Price Prediction App")
st.write("Predict used car selling price using Machine Learning")

MODEL_FILE = "car_price_model.pkl"
DATA_FILE = "cardekho_dataset.csv"

# -----------------------------
# Safe Model Loader / Trainer
# -----------------------------
@st.cache_resource
def load_or_train_model():
    # Try loading old model
    if os.path.exists(MODEL_FILE):
        try:
            model = joblib.load(MODEL_FILE)
            return model, "Loaded saved model successfully ✅"
        except:
            pass

    # Train new model if load fails
    df = pd.read_csv(DATA_FILE)

    # Remove unwanted column if present
    if "Unnamed: 0" in df.columns:
        df.drop("Unnamed: 0", axis=1, inplace=True)

    # Target column
    target_col = "selling_price"

    X = df.drop(target_col, axis=1)
    y = df[target_col]

    # Detect categorical columns
    cat_cols = X.select_dtypes(include="object").columns.tolist()

    # Preprocessing
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
        ],
        remainder="passthrough"
    )

    # Model pipeline
    model = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(
            n_estimators=300,
            random_state=42,
            n_jobs=-1
        ))
    ])

    # Train/Test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train
    model.fit(X_train, y_train)

    # Evaluate
    preds = model.predict(X_test)
    score = r2_score(y_test, preds)

    # Save fresh model
    joblib.dump(model, MODEL_FILE)

    return model, f"New model trained & saved ✅ | R² Score: {score:.2f}"

# -----------------------------
# Load Model
# -----------------------------
model, msg = load_or_train_model()
st.success(msg)

# -----------------------------
# Load Dataset for Dropdowns
# -----------------------------
df = pd.read_csv(DATA_FILE)

if "Unnamed: 0" in df.columns:
    df.drop("Unnamed: 0", axis=1, inplace=True)

# -----------------------------
# Dynamic Inputs
# -----------------------------
st.subheader("Enter Car Details")

inputs = {}

for col in df.columns:
    if col == "selling_price":
        continue

    if df[col].dtype == "object":
        options = sorted(df[col].dropna().unique().tolist())
        inputs[col] = st.selectbox(col, options)

    else:
        min_val = float(df[col].min())
        max_val = float(df[col].max())
        mean_val = float(df[col].mean())

        if df[col].dtype == "int64":
            inputs[col] = st.number_input(
                col,
                min_value=int(min_val),
                max_value=int(max_val),
                value=int(mean_val)
            )
        else:
            inputs[col] = st.number_input(
                col,
                min_value=min_val,
                max_value=max_val,
                value=mean_val
            )

# -----------------------------
# Predict Button
# -----------------------------
if st.button("🔮 Predict Price"):
    input_df = pd.DataFrame([inputs])
    prediction = model.predict(input_df)[0]

    st.balloons()
    st.success(f"💰 Estimated Selling Price: ₹ {prediction:,.2f}")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Built with Streamlit + Scikit-learn")