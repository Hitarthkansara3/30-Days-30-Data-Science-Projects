# 🏠 House Price Prediction App

A professional Machine Learning project that predicts house prices based on property features such as area, bedrooms, bathrooms, parking, furnishing status, and amenities.

Built using **Python, Scikit-learn, Pandas, and Streamlit**.

---


## 📸 Project Screenshot

<img width="753" height="414" alt="image" src="https://github.com/user-attachments/assets/3e6d7d14-a064-48d1-b250-3aa6b207078e" />

<img width="751" height="423" alt="image" src="https://github.com/user-attachments/assets/bd39f989-34a8-42da-bc86-2221f9df5fdd" />



## 🎯 Features

- Predict house prices instantly
- Clean and interactive Streamlit UI
- Supports multiple property inputs
- Machine Learning regression model
- Real-world dataset based project
- Ready for deployment

---

## 🧠 Machine Learning Workflow

1. Data Collection  
2. Data Cleaning  
3. Exploratory Data Analysis (EDA)  
4. Feature Engineering  
5. One-Hot Encoding  
6. Model Training  
7. Model Evaluation  
8. Model Saving (`.pkl`)  
9. Streamlit Web App Deployment  

---

## 📊 Input Parameters

- Area (sq ft)
- Bedrooms
- Bathrooms
- Stories
- Parking
- Main Road Access
- Guest Room
- Basement
- Hot Water Heating
- Air Conditioning
- Preferred Area
- Furnishing Status

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Pickle

---

## 📂 Project Structure

```bash
Day-8_House_Price_Prediction/
│── app.py
│── house_price_model.pkl
│── Housing.csv
│── house_price_prediction.py
│── requirements.txt
│── README.md

## ⚠️ Model File Notice

The `house_price_model.pkl` file is not included in this repository because the file size exceeds GitHub's upload limit.

You can generate the model file locally by running the training script:

```bash
python house_price_prediction.py
```

After running the script, the file `house_price_model.pkl` will be created automatically.

---

## ▶️ Steps to Recreate the Model

```bash
git clone https://github.com/your-username/Day-8_House_Price_Prediction.git
cd Day-8_House_Price_Prediction
pip install -r requirements.txt
python house_price_prediction.py
streamlit run app.py
```

---

## 📌 Why This Is Needed

GitHub has file size limits for uploads, so large model files are often excluded from repositories. Recreating the model locally ensures the project still runs correctly.
