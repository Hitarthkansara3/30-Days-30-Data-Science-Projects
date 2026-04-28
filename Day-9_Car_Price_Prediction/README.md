# 🚗 Day 9 — Car Price Prediction

A professional Machine Learning project that predicts the selling price of used cars using the CarDekho dataset. The project includes data preprocessing, model training, evaluation, and an interactive Streamlit web app.

---

## 📌 Project Overview

Used car prices depend on many factors such as brand, year, fuel type, kilometers driven, transmission, engine capacity, and ownership history. This project builds a regression model to estimate the selling price accurately.

### ✅ Key Highlights

* End-to-end ML pipeline
* Automatic preprocessing with `ColumnTransformer`
* Random Forest Regressor model
* 90%+ R² score (dataset dependent)
* Streamlit web app for live predictions
* Safe auto-train / auto-load model workflow

---

## 🧠 Problem Statement

Buying and selling used cars often involves uncertain pricing. Sellers may overprice and buyers may underpay. The goal is to build a machine learning model that predicts a fair selling price based on car specifications.

---

## 📂 Project Structure

```bash
Day_9_Car_Price_Prediction/
│── cardekho_dataset.csv
│── day_9_car_price_prediction.py
│── car_price_model.pkl
│── app.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit
* Matplotlib / Seaborn

---

## 📊 Features Used

Depending on dataset columns:

* Year
  n- Present Price / Selling Price
* Kilometers Driven
* Fuel Type
* Seller Type
* Transmission
* Owner Count
* Mileage
* Engine
* Max Power
* Seats
* Brand / Model (if available)

---

## 🤖 Model Used

### Random Forest Regressor

Why Random Forest?

* Handles non-linear relationships
* Works well on mixed data types
* Robust and accurate
* Less overfitting than a single tree

---

## 📈 Evaluation Metrics

This is a **Regression** project, so we use:

* **R² Score**
* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)

---

## 🌐 Streamlit Web App

The app allows users to enter car details and get instant predicted selling price.

### App Screenshot

<img width="778" height="408" alt="image" src="https://github.com/user-attachments/assets/6a262ec2-4355-4e4b-bd67-3e41965f5d01" />


<img width="778" height="415" alt="image" src="https://github.com/user-attachments/assets/94882317-d80e-4f4b-a81a-86e16337257a" />



---

## ▶️ How to Run Locally

### 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd Day_9_Car_Price_Prediction
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

## 📦 requirements.txt

```txt
streamlit
pandas
numpy
scikit-learn
joblib
matplotlib
seaborn
```

---

## 🚀 Future Improvements

* XGBoost / CatBoost version
* Better UI design
* Price confidence range
* Car image support
* Cloud deployment
* API integration

---

## 👨‍💻 Author

**Hitarth Kansara**

---

## ⭐ If You Like This Project

Give this repository a star and share it with others.
