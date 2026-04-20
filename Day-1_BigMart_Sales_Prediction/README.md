# BigMart Sales Prediction 📊

## Overview
A machine learning project that predicts product sales for BigMart outlets using data preprocessing, exploratory data analysis, feature engineering, multiple regression models, and stacking ensemble learning.

## Problem Statement
Retail businesses need accurate sales forecasts to optimize inventory, promotions, and revenue. This project predicts `Item_Outlet_Sales` using product and outlet attributes.

## Dataset
- File: `bigmart.csv`
- Typical features:
  - Item_Weight
  - Item_Fat_Content
  - Item_Visibility
  - Item_Type
  - Item_MRP
  - Outlet_Size
  - Outlet_Location_Type
  - Outlet_Type
- Target:
  - `Item_Outlet_Sales`

## Workflow
1. Load Dataset
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Encoding
6. Train/Test Split
7. Model Training
8. Evaluation
9. Stacking Ensemble
10. Model Saving

## Models Used
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor
- LightGBM Regressor
- Stacking Regressor

## Evaluation Metrics
- R2 Score
- RMSE
- MAE

## Results
Stacking and boosting models generally perform best for this dataset.

## Project Structure
```text
BigMart-Sales-Prediction/
│── bigmart.csv
│── BigMart_Sales_Prediction.ipynb
│── bigmart_sales_model.pkl
│── requirements.txt
│── README.md
│── presentation/
│   └── BigMart_Presentation.pptx
```

## Installation
```bash
pip install -r requirements.txt
```

## Run
Open the notebook and run all cells:
```bash
jupyter notebook
```

## Future Improvements
- Hyperparameter tuning
- Streamlit deployment
- Advanced feature selection
- Real-time prediction API

## Author
Hitarth Kansara
