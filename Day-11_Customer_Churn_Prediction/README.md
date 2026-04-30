# Customer Churn Prediction 📉

## Overview
This project predicts whether a telecom customer is likely to churn (leave the company) or stay based on customer demographics, account information, subscribed services, and billing behavior.

Customer churn prediction helps businesses identify at-risk customers early and take proactive retention actions such as discounts, support improvements, or personalized offers.

---

## Problem Statement
Customer acquisition is expensive, and losing existing customers directly impacts revenue.  
The goal of this project is to build a Machine Learning classification model that predicts:

- **0 = Customer Will Stay**
- **1 = Customer Will Churn**

Using this model, businesses can reduce churn and improve customer retention strategies.

---

## Features Used
- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure Months
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

---

## Dataset
**Dataset Name:** IBM Telco Customer Churn Dataset  
**File Used:** `Telco_customer_churn.xlsx`

This dataset contains telecom customer records including services, billing, and churn labels.

---

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- OpenPyXL

---

## Model Information
This project uses a trained classification model saved as:

`customer_churn_model.pkl`

The `.pkl` file stores the trained machine learning pipeline so predictions can be made instantly without retraining every time.

---

## What is Pickle / PKL File?
A `.pkl` (pickle) file is a serialized version of a trained machine learning model.

### Why Use It?
- Saves trained model
- Loads instantly
- No need to train again
- Used for deployment in apps

---

## How to Download / Generate PKL Model
If `customer_churn_model.pkl` is missing:

1. Open terminal in project folder
2. Run training script:

```bash
python day_11_customer_churn_prediction.py
```

3. After running, the PKL file will be created automatically.

---

## What is Streamlit?
Streamlit is a Python framework used to convert data science and machine learning scripts into interactive web applications.

### Why Streamlit?
- Easy to use
- Fast deployment
- Beautiful UI components
- Perfect for ML projects
- No frontend coding required

---

## How to Run This Project

### 1. Clone Repository
```bash
git clone <your-repository-link>
cd Day-11_Customer_Churn_Prediction
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Run App
```bash
streamlit run app.py
```

---

## Project Files
```text
Day-11_Customer_Churn_Prediction/
│── app.py
│── customer_churn_model.pkl
│── day_11_customer_churn_prediction.py
│── Telco_customer_churn.xlsx
│── requirements.txt
│── README.md
```

---

## App Prediction Output
The app takes customer details as input and predicts:

- ✅ Customer Will Stay
- ⚠️ Customer is Likely to Churn

It also shows churn probability (if supported by model).

---

## Business Use Cases
- Reduce customer loss
- Increase revenue
- Improve retention campaigns
- Identify unhappy customers
- Offer personalized plans

---

## Resume Description
Developed a Customer Churn Prediction system using Machine Learning and Streamlit to identify customers likely to leave a telecom service based on behavioral and billing data.

---

## Future Improvements
- Hyperparameter tuning
- Advanced models (XGBoost, LightGBM)
- Explainable AI (SHAP)
- Cloud deployment
- Real-time database integration

---

## Author
**Hitarth Kansara**

---

## License
This project is for educational and portfolio purposes.
