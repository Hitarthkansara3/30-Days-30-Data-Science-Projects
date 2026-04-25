# 🛒 Amazon Product Data Analysis

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-blue?style=for-the-badge&logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge&logo=plotly)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-green?style=for-the-badge)
![TextBlob](https://img.shields.io/badge/TextBlob-Sentiment%20Analysis-red?style=for-the-badge)

---

# 📌 Project Overview

Amazon has millions of products across multiple categories.  
Understanding **pricing strategy, discounts, customer ratings, reviews, and product performance** is crucial for both sellers and buyers.

This project performs an end-to-end analysis of Amazon product data using **Python, Data Analysis, Visualization, and NLP (Sentiment Analysis)** to extract meaningful business insights.

---

# 🎯 Problem Statement

Customers often struggle to identify the best-value products, while businesses need data-driven insights to improve pricing and product strategies.

The goal of this project is to analyze Amazon product listings and answer:

- Which categories dominate the marketplace?
- How do discounts affect ratings?
- What products are most popular?
- What sentiment do customers express in reviews?
- Which products offer the best value?

---

# 📂 Dataset Information

- **Dataset Name:** Amazon Sales Dataset
- **Source:** Kaggle
- **Records:** 1,000+ Products
- **Features Include:**
  - Product Name
  - Category
  - Actual Price
  - Discounted Price
  - Discount Percentage
  - Rating
  - Rating Count
  - Review Content
  - Product Description

🔗 **Dataset Link:**  
https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- TextBlob
- Jupyter Notebook

---

# 📊 Project Workflow

## 1️⃣ Data Collection
Imported dataset from Kaggle.

## 2️⃣ Data Cleaning
- Removed ₹ symbol and commas
- Converted prices to numeric
- Converted percentages
- Handled missing values
- Removed duplicates

## 3️⃣ Exploratory Data Analysis (EDA)
Performed detailed analysis on:

- Product Categories
- Price Distribution
- Discounts
- Ratings
- Most Reviewed Products
- Top Rated Products
- Best Value Products

## 4️⃣ Sentiment Analysis
Used customer reviews to classify sentiment into:

- Positive 😊
- Neutral 😐
- Negative 😞

## 5️⃣ Business Insights
Generated practical recommendations for sellers and decision-makers.

---

# 📈 Key Visualizations

- Top Categories by Product Count
- Price Distribution Histogram
- Rating Distribution
- Discount vs Rating Scatter Plot
- Most Reviewed Products
- Correlation Heatmap
- Sentiment Analysis Chart

---

# 🔍 Key Insights

✅ Most products have ratings above 4.0 stars  
✅ Electronics categories dominate the marketplace  
✅ Higher discounts do not always guarantee better ratings  
✅ Positive sentiment dominates customer reviews  
✅ Affordable products can provide high value scores  

---

# 🤖 Sentiment Analysis Example

| Sentiment | Meaning |
|--------|---------|
| Positive | Happy customer reviews |
| Neutral | Mixed or average reviews |
| Negative | Poor customer experience |

---

# 📌 Future Improvements

- Build Product Recommendation System  
- Create Interactive Dashboard (Power BI / Tableau)  
- Predict Product Ratings using Machine Learning  
- Deploy as Web App using Streamlit  

---

# 📷 Project Output

This project demonstrates:

✔ Real-world EDA Skills  
✔ Data Cleaning Techniques  
✔ Business Thinking  
✔ NLP Sentiment Analysis  
✔ Data Visualization  
✔ Portfolio-Level Project Experience  

---

# 🚀 How to Run This Project

```bash
# Clone Repository
git clone https://github.com/Hitarthkansara3/30-Days-30-Data-Science-Projects/edit/main/Day-6_Amazon_Data_Analysis

# Open Folder
cd amazon-data-analysis

# Install Requirements
pip install -r requirements.txt

# Run Notebook
jupyter notebook
