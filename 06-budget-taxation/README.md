# 💰 Budget & Taxation Analytics

## 📖 Project Overview

Government budgets and taxation policies play a crucial role in economic development, public welfare, infrastructure creation, and fiscal stability.

This project analyzes government revenue, expenditure, direct taxes, indirect taxes, fiscal balance, and GDP trends using Data Analytics, Statistics, SQL, Machine Learning, Data Visualization, and an Interactive Streamlit Dashboard.

The objective is to transform public finance concepts into practical analytics applications using Python and modern data analysis techniques.

---

# 🎯 Objectives

- Analyze government revenue trends
- Study government expenditure patterns
- Compare direct and indirect taxes
- Examine fiscal balance movements
- Understand public finance indicators
- Perform statistical analysis
- Apply SQL analytics
- Build machine learning prediction models
- Develop interactive dashboards

---

# 📚 Source of Data

The dataset used in this project is an educational dataset created for learning and analytical purposes based on publicly available public finance concepts and trends.

## Reference Sources

- Union Budget of India
- Ministry of Finance
- Economic Survey of India
- Reserve Bank of India (RBI)
- RBI Database on Indian Economy (DBIE)
- World Bank Open Data
- International Monetary Fund (IMF)
- Investopedia Public Finance Resources

## Dataset Nature

- Educational Dataset
- Publicly Inspired Economic Indicators
- Learning Purpose Only
- Not Official Government Statistics

---

# 🛠 Technologies Used

## Programming

- Python

## Data Analysis

- Pandas
- NumPy

## Visualization

- Matplotlib
- Plotly

## Machine Learning

- Scikit-Learn
- Random Forest Regressor

## Dashboard Development

- Streamlit

## Database Analytics

- SQL

---

# 📂 Project Structure

```text
06-budget-taxation/
│
├── data/
│   └── budget_taxation_data.csv
│
├── charts/
│   ├── government_revenue.png
│   ├── government_expenditure.png
│   ├── direct_vs_indirect_tax.png
│   ├── fiscal_balance_trend.png
│   ├── tax_revenue_growth.png
│   ├── feature_importance.png
│   ├── ml_prediction.png
│   └── dashboard_preview.png
│
├── sql/
│   └── budget_taxation_queries.sql
│
├── analysis.py
├── charts.py
├── ml_model.py
├── dashboard.py
├── requirements.txt
└── README.md
```

---

# 📊 Dataset Description

The dataset contains yearly public finance indicators.

| Column | Description |
|----------|-------------|
| Year | Observation Year |
| GovernmentRevenue | Total Government Revenue |
| GovernmentExpenditure | Total Government Expenditure |
| DirectTax | Direct Tax Collection |
| IndirectTax | Indirect Tax Collection |
| FiscalBalance | Budget Surplus / Deficit |
| GDP | Gross Domestic Product |

---

# 📈 Economic Concepts Covered

## Government Budget

A government budget is an annual financial statement showing expected revenue and expenditure.

### Components

- Revenue Receipts
- Capital Receipts
- Revenue Expenditure
- Capital Expenditure

---

## Taxation

Taxes are compulsory payments imposed by governments to finance public expenditure.

### Direct Taxes

Examples:

- Income Tax
- Corporate Tax

Characteristics:

- Paid directly by taxpayers
- Progressive in nature

---

### Indirect Taxes

Examples:

- GST
- Excise Duty
- Customs Duty

Characteristics:

- Collected through goods and services
- Shared across consumers

---

## Fiscal Balance

Fiscal Balance = Revenue − Expenditure

### Positive Balance

Budget Surplus

### Negative Balance

Fiscal Deficit

---

# 📉 Statistical Analysis

The project performs:

- Descriptive Statistics
- Revenue Analysis
- Expenditure Analysis
- Tax Collection Analysis
- Fiscal Balance Analysis
- Growth Rate Analysis
- Correlation Analysis

### Example Metrics

- Average Revenue
- Average Expenditure
- Average Direct Tax
- Average Indirect Tax
- Revenue Growth Rate
- Expenditure Growth Rate
- Correlation Matrix

---

# 📊 Data Visualizations

The project automatically generates the following charts.

---

## 1. Government Revenue Trend

File:

```text
government_revenue.png
```

Visualizes revenue growth over time.

---

## 2. Government Expenditure Trend

File:

```text
government_expenditure.png
```

Analyzes public spending patterns.

---

## 3. Direct vs Indirect Tax

File:

```text
direct_vs_indirect_tax.png
```

Compares tax collection sources.

---

## 4. Fiscal Balance Trend

File:

```text
fiscal_balance_trend.png
```

Shows budget surplus or deficit movement.

---

## 5. Tax Revenue Growth

File:

```text
tax_revenue_growth.png
```

Tracks total tax collection growth.

---

## 6. Feature Importance

File:

```text
feature_importance.png
```

Displays influential variables used by the machine learning model.

---

## 7. Machine Learning Prediction

File:

```text
ml_prediction.png
```

Compares actual and predicted revenue values.

---

# 🤖 Machine Learning Model

The project uses Machine Learning to predict future government revenue.

## Algorithm

Random Forest Regressor

## Features

- Government Expenditure
- Direct Tax
- Indirect Tax
- GDP

## Target

- Government Revenue

## Outputs

- R² Score
- Revenue Prediction
- Feature Importance
- Actual vs Predicted Comparison

### Example Prediction Output

```text
========== ML RESULTS ==========

R2 Score: 0.95

Predicted Government Revenue

2025 : 2815

2026 : 3048

========== MODEL COMPLETED ==========
```

---

# 🗄 SQL Analytics

The project includes SQL queries for public finance analysis.

### Example Queries

```sql
SELECT *
FROM budget_taxation_data;
```

```sql
SELECT AVG(GovernmentRevenue)
FROM budget_taxation_data;
```

```sql
SELECT AVG(GovernmentExpenditure)
FROM budget_taxation_data;
```

```sql
SELECT AVG(DirectTax)
FROM budget_taxation_data;
```

```sql
SELECT AVG(IndirectTax)
FROM budget_taxation_data;
```

```sql
SELECT Year,
       FiscalBalance
FROM budget_taxation_data;
```

### SQL Insights

- Revenue Analysis
- Expenditure Analysis
- Tax Collection Analysis
- Fiscal Balance Tracking
- Revenue Ranking
- GDP Comparison
- Economic Summary Reports

---

# 📷 Project Outputs

## Terminal Output

Running:

```bash
python analysis.py
```

Example:

```text
========== BUDGET & TAXATION ANALYSIS ==========

Average Government Revenue:
1773.00

Average Government Expenditure:
1980.00

Average Direct Tax:
794.00

Average Indirect Tax:
979.00

Revenue Growth Rate:
116.67

Expenditure Growth Rate:
107.14

Correlation Matrix:
...

========== ANALYSIS COMPLETED ==========
```

---

## Generated Charts

Running:

```bash
python charts.py
```

Creates:

```text
government_revenue.png
government_expenditure.png
direct_vs_indirect_tax.png
fiscal_balance_trend.png
tax_revenue_growth.png
feature_importance.png
ml_prediction.png
```

---

## Machine Learning Output

Running:

```bash
python ml_model.py
```

Generates:

```text
Future Revenue Prediction
Feature Importance Analysis
Actual vs Predicted Visualization
R² Score Evaluation
```

---

## Dashboard Output

Running:

```bash
streamlit run dashboard.py
```

Launches an interactive dashboard featuring:

- Dataset Explorer
- Statistical Summary
- KPI Metrics
- Revenue Analysis
- Expenditure Analysis
- Direct vs Indirect Tax Analysis
- Fiscal Balance Analysis
- Correlation Matrix
- Machine Learning Results
- SQL Query Explorer
- Economic Insights

Dashboard Screenshot:

```text
charts/dashboard_preview.png
```

---

# 🌐 Dashboard Features

### 📋 Dataset Explorer

Explore complete budget and taxation data.

### 📊 Statistical Summary

View descriptive statistics instantly.

### 💰 Revenue Analysis

Analyze government revenue growth.

### 🏛 Expenditure Analysis

Study expenditure patterns and trends.

### 💵 Tax Analysis

Compare direct and indirect taxes.

### 📉 Fiscal Balance Analysis

Understand budget surplus and deficit movement.

### 🤖 Machine Learning Results

Explore future revenue forecasts.

### 🗄 SQL Query Explorer

Review public finance SQL queries.

---

# ▶ How To Run

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Statistical Analysis

```bash
python analysis.py
```

## Generate Charts

```bash
python charts.py
```

## Run Machine Learning

```bash
python ml_model.py
```

## Launch Dashboard

```bash
streamlit run dashboard.py
```

---

# 🎓 Learning Outcomes

After completing this project, learners will understand:

- Government Budget Structure
- Revenue and Expenditure Analysis
- Direct and Indirect Taxation
- Fiscal Balance Concepts
- Public Finance Analytics
- Statistical Analysis Techniques
- SQL Analytics
- Data Visualization
- Machine Learning Prediction
- Dashboard Development

---

# 🌍 Real-World Applications

This project can be applied in:

- Public Finance Research
- Economic Policy Analysis
- Government Budget Studies
- Academic Learning
- Data Analytics Training
- Dashboard Development
- Fiscal Planning Analysis

---

# 👩‍💻 Author

**Saloni Tiwari**

🎓 IIT Madras BS in Data Science

🎓 B.Sc Mathematics (Magadh University)

### Skills

- Python
- NumPy
- Pandas
- Matplotlib
- SQL
- Statistics
- Data Analytics
- Machine Learning (Learning)
- Data Structures & Algorithms (Learning)
- DBMS (Learning)

---

# ⭐ Project Status

✅ Completed

Part of the **Foundational Economics Series**, a collection of economics analytics projects built using Python, Statistics, SQL, Machine Learning, Data Visualization, and Interactive Dashboards.

---

## 🚀 Learning Economics Through Data Analytics