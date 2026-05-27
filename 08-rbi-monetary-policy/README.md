# 🏦 RBI & Monetary Policy Analytics

## 📖 Project Overview

Monetary Policy is one of the most important tools used by the Reserve Bank of India (RBI) to control inflation, regulate liquidity, stabilize financial markets, and support economic growth.

This project analyzes Repo Rate, Reverse Repo Rate, Cash Reserve Ratio (CRR), Statutory Liquidity Ratio (SLR), Inflation Rate, and Money Supply using Data Analytics, Statistics, SQL, Machine Learning, Data Visualization, and an Interactive Streamlit Dashboard.

The objective is to transform RBI monetary policy concepts into practical analytics applications using Python and modern data science tools.

---

# 🎯 Objectives

- Analyze Repo Rate trends
- Study Reverse Repo Rate movements
- Compare CRR and SLR changes
- Examine inflation and monetary policy relationships
- Evaluate money supply growth
- Perform statistical analysis
- Apply SQL analytics
- Build machine learning prediction models
- Develop interactive dashboards

---

# 📚 Source of Data

The dataset used in this project is an educational dataset created for learning and analytical purposes based on publicly available monetary policy concepts and trends.

## Reference Sources

- Reserve Bank of India (RBI)
- RBI Database on Indian Economy (DBIE)
- Monetary Policy Committee (MPC) Reports
- Economic Survey of India
- Ministry of Finance
- World Bank Open Data
- International Monetary Fund (IMF)
- Investopedia Monetary Economics Resources

## Dataset Nature

- Educational Dataset
- Publicly Inspired Economic Indicators
- Learning Purpose Only
- Not Official RBI Statistics

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
08-rbi-monetary-policy/
│
├── data/
│   └── rbi_monetary_policy_data.csv
│
├── charts/
│   ├── repo_rate_trend.png
│   ├── reverse_repo_rate.png
│   ├── crr_slr_analysis.png
│   ├── inflation_vs_repo_rate.png
│   ├── money_supply_growth.png
│   ├── feature_importance.png
│   ├── ml_prediction.png
│   └── dashboard_preview.png
│
├── sql/
│   └── rbi_monetary_policy_queries.sql
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

The dataset contains yearly monetary policy indicators.

| Column | Description |
|----------|-------------|
| Year | Observation Year |
| RepoRate | RBI Lending Rate |
| ReverseRepoRate | RBI Borrowing Rate |
| CRR | Cash Reserve Ratio |
| SLR | Statutory Liquidity Ratio |
| InflationRate | Annual Inflation Rate (%) |
| MoneySupply | Total Money Supply Index |

---

# 📈 Economic Concepts Covered

## Repo Rate

Repo Rate is the interest rate at which the RBI lends money to commercial banks.

### Effects

- Higher Repo Rate → Lower Borrowing
- Lower Repo Rate → Higher Borrowing
- Controls Inflation
- Influences Economic Growth

---

## Reverse Repo Rate

Reverse Repo Rate is the interest rate at which RBI borrows money from commercial banks.

### Purpose

- Absorb Excess Liquidity
- Control Inflation
- Stabilize Money Markets

---

## Cash Reserve Ratio (CRR)

CRR is the percentage of deposits banks must keep with RBI as reserves.

### Importance

- Controls Liquidity
- Regulates Credit Creation
- Maintains Financial Stability

---

## Statutory Liquidity Ratio (SLR)

SLR is the percentage of deposits banks must maintain in approved securities.

### Importance

- Ensures Bank Liquidity
- Promotes Financial Stability
- Supports Government Borrowing

---

## Money Supply

Money Supply represents the total amount of money circulating in the economy.

### Components

- Currency
- Bank Deposits
- Liquid Financial Assets

---

# 📉 Statistical Analysis

The project performs:

- Descriptive Statistics
- Repo Rate Analysis
- Reverse Repo Analysis
- CRR Analysis
- SLR Analysis
- Inflation Analysis
- Money Supply Growth Analysis
- Correlation Analysis

### Example Metrics

- Average Repo Rate
- Average Reverse Repo Rate
- Average CRR
- Average SLR
- Average Inflation Rate
- Money Supply Growth
- Correlation Matrix

---

# 📊 Data Visualizations

The project automatically generates the following charts.

---

## 1. Repo Rate Trend

File:

```text
repo_rate_trend.png
```

Tracks RBI policy rate changes over time.

---

## 2. Reverse Repo Rate Analysis

File:

```text
reverse_repo_rate.png
```

Analyzes liquidity absorption trends.

---

## 3. CRR vs SLR Analysis

File:

```text
crr_slr_analysis.png
```

Compares reserve requirement policies.

---

## 4. Inflation vs Repo Rate

File:

```text
inflation_vs_repo_rate.png
```

Examines monetary policy effectiveness.

---

## 5. Money Supply Growth

File:

```text
money_supply_growth.png
```

Tracks expansion of money supply.

---

## 6. Feature Importance

File:

```text
feature_importance.png
```

Displays important variables influencing inflation predictions.

---

## 7. Machine Learning Prediction

File:

```text
ml_prediction.png
```

Compares actual and predicted inflation values.

---

# 🤖 Machine Learning Model

The project uses Machine Learning to predict future inflation rates.

## Algorithm

Random Forest Regressor

## Features

- Repo Rate
- Reverse Repo Rate
- CRR
- SLR
- Money Supply

## Target

- Inflation Rate

## Outputs

- R² Score
- Future Inflation Prediction
- Feature Importance
- Actual vs Predicted Comparison

### Example Prediction Output

```text
========== ML RESULTS ==========

R2 Score: 0.92

Predicted Inflation Rate

2025 : 5.70

2026 : 5.45

========== MODEL COMPLETED ==========
```

---

# 🗄 SQL Analytics

The project includes SQL queries for monetary policy analysis.

### Example Queries

```sql
SELECT AVG(RepoRate)
FROM rbi_monetary_policy_data;
```

```sql
SELECT AVG(ReverseRepoRate)
FROM rbi_monetary_policy_data;
```

```sql
SELECT AVG(CRR)
FROM rbi_monetary_policy_data;
```

```sql
SELECT AVG(SLR)
FROM rbi_monetary_policy_data;
```

```sql
SELECT AVG(InflationRate)
FROM rbi_monetary_policy_data;
```

### SQL Insights

- Repo Rate Analysis
- Reverse Repo Analysis
- CRR Analysis
- SLR Analysis
- Inflation Tracking
- Money Supply Growth
- Policy Rankings
- Monetary Summary Reports

---

# 📷 Project Outputs

## Terminal Output

Running:

```bash
python analysis.py
```

Example:

```text
========== RBI MONETARY POLICY ANALYSIS ==========

Average Repo Rate:
5.91

Average Reverse Repo Rate:
5.28

Average Inflation Rate:
5.67

Money Supply Growth:
170.00

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
repo_rate_trend.png
reverse_repo_rate.png
crr_slr_analysis.png
inflation_vs_repo_rate.png
money_supply_growth.png
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
Future Inflation Prediction
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
- Repo Rate Analysis
- Reverse Repo Analysis
- CRR vs SLR Analysis
- Inflation vs Repo Rate Analysis
- Money Supply Growth
- Correlation Matrix
- Machine Learning Results
- SQL Query Explorer
- Monetary Policy Insights

Dashboard Screenshot:

```text
charts/dashboard_preview.png
```

---

# 🌐 Dashboard Features

### 📋 Dataset Explorer

Explore complete RBI monetary policy data.

### 📊 Statistical Summary

View descriptive statistics instantly.

### 🏦 Repo Rate Analysis

Track monetary policy stance.

### 💵 Reverse Repo Analysis

Analyze liquidity absorption.

### 📈 CRR vs SLR Analysis

Compare reserve requirements.

### 📉 Inflation Analysis

Study inflation control mechanisms.

### 💰 Money Supply Analysis

Monitor monetary expansion.

### 🤖 Machine Learning Results

Explore future inflation forecasts.

### 🗄 SQL Query Explorer

Review monetary policy SQL queries.

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

- RBI Functions
- Monetary Policy Framework
- Repo Rate Mechanism
- Reverse Repo Operations
- CRR and SLR Concepts
- Inflation Management
- Money Supply Control
- Statistical Analysis
- SQL Analytics
- Machine Learning Prediction
- Dashboard Development

---

# 🌍 Real-World Applications

This project can be applied in:

- Monetary Policy Research
- Banking Studies
- Economic Analysis
- Financial Market Research
- Academic Learning
- Data Analytics Training
- Dashboard Development
- Policy Evaluation

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