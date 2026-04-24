# 🎓 Student Performance Analysis & Pass Prediction

## 📌 Project Overview
This project analyzes student academic performance using data science techniques and builds a machine learning model to predict whether a student will pass or fail based on study habits, background factors, and previous grades.

The project includes:
- Exploratory Data Analysis (EDA)
- Data Visualization
- Feature Engineering
- Pass/Fail Prediction
- Model Evaluation
- Feature Importance Analysis

---

## 📂 Dataset
Two datasets were used:

- `mat2.csv` → Math student performance
- `por2.csv` → Portuguese student performance

Common features include:
- Study Time
- Failures
- Family Support
- Internet Access
- Absences
- Previous Grades (`G1`, `G2`)
- Final Grade (`G3`)

---

## 🎯 Problem Statement
Schools and educators want to understand what factors most influence student success.

This project answers:
1. Does study time improve marks?
2. Do male and female students perform differently?
3. How do failures and absences affect results?
4. Can we predict pass/fail outcomes using machine learning?

---

## 🛠️ Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook / Google Colab

---

## 📊 Exploratory Data Analysis
The following analyses were performed:

### ✅ Marks Distribution
- Histogram of final grades
- Boxplot for outlier detection

### ✅ Marks vs Study Hours
- Study time compared with final grades

### ✅ Gender Analysis
- Average marks by gender
- Performance comparison

### ✅ Family Support Impact
- Family support vs marks

### ✅ Internet Access Impact
- Internet availability vs performance

### ✅ Failures Analysis
- Past failures vs final grades

### ✅ Correlation Heatmap
- Relationships between numeric variables

---

## 🤖 Machine Learning Model

### Target Variable
- **Pass = 1** if `G3 >= 10`
- **Fail = 0** if `G3 < 10`

### Models Used
- Logistic Regression
- Random Forest Classifier

### Evaluation Metrics
- Accuracy Score
- Confusion Matrix
- Classification Report

---

## 📈 Key Insights
- Students with higher study time tend to score better.
- Previous grades (`G1`, `G2`) strongly predict final results.
- More failures and absences often reduce performance.
- Family support can positively impact grades.

---

## 📁 Project Structure
```bash
Day-5-Student-Performance/
│── Student_Performance_Analysis.ipynb
│── mat2.csv
│── por2.csv
│── README.md
│── images/
```

---

## 🚀 How to Run
1. Clone this repository
2. Open the notebook in Jupyter or Colab
3. Upload datasets (`mat2.csv`, `por2.csv`)
4. Run all cells step by step

---

## 📌 Future Improvements
- Hyperparameter tuning
- Deployment with Streamlit
- Power BI Dashboard
- Compare multiple ML models
- Student risk alert system

---

## 🙌 Author
**Hitarth Kansara**  

If you like this project, give it a ⭐ on GitHub!
