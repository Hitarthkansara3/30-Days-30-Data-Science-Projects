# 💰 Loan Approval Prediction using Machine Learning

A professional end-to-end **Machine Learning + Streamlit** project that predicts whether a loan application will be **Approved** or **Rejected** based on applicant details such as income, CIBIL score, assets, loan amount, education, and employment status.

---

# 📌 Project Overview

Banks receive thousands of loan applications. Manually reviewing each application takes time and may lead to inconsistent decisions.

This project uses **Machine Learning** to automate the prediction process by learning patterns from historical data and instantly predicting the loan status.

### ✅ Main Goal

Build an intelligent model that can predict:

* **Approved**
* **Rejected**

---

# 🚀 Live Features

✅ User-friendly Streamlit web app
✅ Real-time prediction
✅ Uses trained `.pkl` model
✅ Automatic preprocessing pipeline
✅ Clean UI design
✅ Ready for deployment

---

# 🧠 What is Streamlit?

**Streamlit** is a Python framework used to build interactive web applications for Data Science and Machine Learning projects using only Python code.

### Why Streamlit?

* No HTML/CSS required
* Fast and beginner-friendly
* Easy deployment
* Interactive inputs like sliders, buttons, forms
* Perfect for portfolio projects

### Example:

You train a model in Jupyter Notebook, then use Streamlit to turn it into a real website.

---

# 📂 Project Structure

```bash
Loan_Approval_Prediction/
│── app.py
│── loan_approval_dataset.csv
│── loan_approval_model.pkl
│── Loan_Approval_Prediction.ipynb
│── requirements.txt
│── README.md
```

---

# 📊 Dataset Information

The dataset contains applicant details such as:

* Number of Dependents
* Education
* Self Employed
* Annual Income
* Loan Amount
* Loan Term
* CIBIL Score
* Residential Assets Value
* Commercial Assets Value
* Luxury Assets Value
* Bank Asset Value
* Loan Status (Target)

---

# ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit
* Matplotlib
* Seaborn

---

# 🤖 Machine Learning Workflow

### 1️⃣ Data Cleaning

* Remove extra spaces
* Handle column names
* Check missing values

### 2️⃣ Feature Engineering

* Encode categorical values
* Scale numeric features

### 3️⃣ Model Training

Used models like:

* Logistic Regression
* Random Forest ✅
* Gradient Boosting

### 4️⃣ Evaluation

Measured using:

* Accuracy Score
* Confusion Matrix
* Classification Report

### 5️⃣ Deployment

Deployed using Streamlit app.

---

# 🎯 Model Accuracy

✅ Achieved **90%+ Accuracy** using optimized Random Forest model.

> Actual accuracy may vary depending on train/test split and random state.

---

# 💾 How to Download / Generate Pickle Model (.pkl)

The `.pkl` file stores your trained machine learning model so the Streamlit app can use it without retraining every time.

## Method 1: Generate from Notebook

Run the final training cell:

```python
import joblib
joblib.dump(final_model, "loan_approval_model.pkl")
```

This creates:

```bash
loan_approval_model.pkl
```

## Method 2: If File Not in GitHub

Some `.pkl` files are too large for GitHub or excluded intentionally.

In that case:

1. Open the notebook
2. Run all cells
3. Execute the save-model cell above
4. The `.pkl` file will be created automatically

---

# ▶️ How to Run This Project

## Step 1: Clone Repository

```bash
git clone <your-repo-link>
cd Loan_Approval_Prediction
```

## Step 2: Install Requirements

```bash
pip install -r requirements.txt
```

## Step 3: Run Streamlit App

```bash
streamlit run app.py
```

---

# 🖥️ App Preview

The Streamlit app allows users to enter:

* Income
* CIBIL Score
* Loan Amount
* Assets
* Education
* Employment Status

Then click **Predict** to get instant result.

---

# 📈 Future Improvements

* Hyperparameter tuning
* Better UI design
* Cloud deployment
* Explainable AI (SHAP)
* Loan risk scoring
* User login system

---

# 🙋‍♂️ Author

**Hitarth Kansara**
Data Science & Machine Learning Enthusiast

---

