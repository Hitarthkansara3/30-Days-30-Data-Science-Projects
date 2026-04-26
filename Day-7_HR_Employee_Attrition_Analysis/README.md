# Day 7 — HR Employee Attrition Analysis

## 📌 Project Overview
Employee attrition is a major challenge for organizations because losing skilled employees increases hiring costs, reduces productivity, and impacts team performance. This project analyzes HR employee data to identify the key reasons employees leave and builds a machine learning model to predict attrition risk.

## 🎯 Objectives
- Understand why employees leave the company
- Analyze the impact of salary on attrition
- Compare attrition across departments
- Study overtime, job satisfaction, and work-life balance
- Build a predictive model for employee attrition

## 📂 Dataset
**IBM HR Analytics Employee Attrition & Performance Dataset**

File used: `WA_Fn-UseC_-HR-Employee-Attrition.csv`

Key features:
- Attrition
- MonthlyIncome
- Department
- JobRole
- OverTime
- Age
- YearsAtCompany
- JobSatisfaction
- WorkLifeBalance

## 🛠️ Tech Stack
- Python
- Google Colab / Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## 📊 Analysis Performed
### 1. Data Exploration
- Dataset shape
- Data types
- Missing values
- Statistical summary

### 2. Exploratory Data Analysis
- Attrition count and percentage
- Salary vs Attrition
- Department-wise attrition
- Overtime impact
- Job satisfaction trends
- Work-life balance trends
- Age distribution
- Years at company vs attrition
- Correlation heatmap

### 3. Machine Learning
- Label Encoding
- Train-Test Split
- Logistic Regression / Random Forest
- Model Evaluation
- Confusion Matrix

## 📈 Key Insights
- Employees working overtime are more likely to leave.
- Lower income groups show higher attrition.
- Some departments experience higher turnover.
- Low job satisfaction is linked to resignations.
- Predictive models can help HR take early action.

## 🤖 Sample Results
- Classification Accuracy depends on model and preprocessing.
- Random Forest often performs better than baseline Logistic Regression.

## 📁 Project Structure
```text
Day-7-HR-Employee-Attrition-Analysis/
│── HR_Employee_Attrition_Analysis.ipynb
│── WA_Fn-UseC_-HR-Employee-Attrition.csv
│── README.md
```

## ▶️ How to Run
1. Clone this repository
2. Open the notebook in Google Colab or Jupyter
3. Upload the dataset CSV file
4. Run all cells in order
5. Review insights and model results

## 🚀 Future Improvements
- Hyperparameter tuning
- XGBoost / LightGBM models
- Interactive dashboard in Power BI / Tableau
- Employee retention recommendation system
- Deployment with Flask / Streamlit

## 👨‍💻 Author
Created as part of **30 Days 30 Data Science Projects** challenge.

## ⭐ If You Like This Project
Give it a star on GitHub and share your feedback!
