# 📊 GDP & Development Analytics

## 📖 Project Overview

Gross Domestic Product (GDP) and development indicators are among the most important measures of a nation's economic performance and quality of life.

This project analyzes GDP growth, Per Capita Income, Human Development Index (HDI), Sectoral Contribution (Agriculture, Industry, Services), and Economic Growth Rates using Data Analytics, Statistics, SQL, Machine Learning, Data Visualization, and an Interactive Streamlit Dashboard.

The objective is to transform economic growth and development concepts into practical analytics applications using Python and modern data science tools.

---

# 🎯 Objectives

- Analyze GDP growth trends
- Study Per Capita Income growth
- Evaluate Human Development Index (HDI)
- Examine sectoral contributions
- Analyze economic growth rates
- Perform statistical analysis
- Apply SQL analytics
- Build machine learning prediction models
- Develop interactive dashboards

---

# 📚 Source of Data

The dataset used in this project is an educational dataset created for learning and analytical purposes based on publicly available economic development concepts and trends.

## Reference Sources

- World Bank Open Data
- International Monetary Fund (IMF)
- United Nations Development Programme (UNDP)
- Reserve Bank of India (RBI)
- Ministry of Statistics & Programme Implementation (MOSPI)
- Economic Survey of India
- OECD Statistics
- Investopedia Economic Growth Resources

## Dataset Nature

- Educational Dataset
- Publicly Inspired Economic Indicators
- Learning Purpose Only
- Not Official Statistics

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
10-gdp-development/
│
├── data/
│   └── gdp_development_data.csv
│
├── charts/
│   ├── gdp_growth_trend.png
│   ├── per_capita_income.png
│   ├── sectoral_contribution.png
│   ├── hdi_vs_gdp.png
│   ├── economic_growth_rate.png
│   ├── feature_importance.png
│   ├── ml_prediction.png
│   └── dashboard_preview.png
│
├── sql/
│   └── gdp_development_queries.sql
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

The dataset contains yearly economic development indicators.

| Column | Description |
|----------|-------------|
| Year | Observation Year |
| GDP | Gross Domestic Product |
| PerCapitaIncome | Income Per Person |
| Agriculture | Agriculture Sector Share (%) |
| Industry | Industry Sector Share (%) |
| Services | Services Sector Share (%) |
| HDI | Human Development Index |
| GrowthRate | Annual Economic Growth Rate (%) |

---

# 📈 Economic Concepts Covered

## Gross Domestic Product (GDP)

GDP represents the total value of goods and services produced within a country during a specific period.

### Importance

- Measures Economic Performance
- Indicates National Output
- Supports Policy Decisions
- Reflects Economic Growth

---

## Per Capita Income

Per Capita Income measures average income earned per person.

### Importance

- Living Standard Indicator
- Income Comparison Tool
- Development Measurement

---

## Human Development Index (HDI)

HDI measures development beyond income.

### Components

- Education
- Health
- Standard of Living

### Range

```text
0 → Low Development
1 → High Development
```

---

## Economic Growth Rate

Economic Growth Rate measures annual expansion of economic activity.

### Positive Growth

- More Production
- More Employment
- Higher Income

### Negative Growth

- Recession
- Lower Output
- Reduced Income

---

## Sectoral Contribution

The economy is generally divided into:

### Agriculture

Farming and related activities.

### Industry

Manufacturing and industrial production.

### Services

Banking, IT, Healthcare, Education, Tourism and other services.

---

# 📉 Statistical Analysis

The project performs:

- Descriptive Statistics
- GDP Analysis
- Per Capita Income Analysis
- HDI Analysis
- Growth Rate Analysis
- Sector Contribution Analysis
- Correlation Analysis

### Example Metrics

- Average GDP
- Average Per Capita Income
- Average HDI
- GDP Growth Rate
- Income Growth Rate
- Sector Averages
- Correlation Matrix

---

# 📊 Data Visualizations

The project automatically generates the following charts.

---

## 1. GDP Growth Trend

File:

```text
gdp_growth_trend.png
```

Tracks GDP growth over time.

---

## 2. Per Capita Income

File:

```text
per_capita_income.png
```

Shows income growth per person.

---

## 3. Sectoral Contribution

File:

```text
sectoral_contribution.png
```

Compares Agriculture, Industry and Services sectors.

---

## 4. HDI vs GDP

File:

```text
hdi_vs_gdp.png
```

Analyzes relationship between development and economic output.

---

## 5. Economic Growth Rate

File:

```text
economic_growth_rate.png
```

Shows annual economic growth performance.

---

## 6. Feature Importance

File:

```text
feature_importance.png
```

Displays important variables used by the machine learning model.

---

## 7. Machine Learning Prediction

File:

```text
ml_prediction.png
```

Compares actual and predicted GDP values.

---

# 🤖 Machine Learning Model

The project uses Machine Learning to predict future GDP.

## Algorithm

Random Forest Regressor

## Features

- Per Capita Income
- Agriculture
- Industry
- Services
- HDI
- Growth Rate

## Target

- GDP

## Outputs

- R² Score
- Future GDP Prediction
- Feature Importance
- Actual vs Predicted Comparison

### Example Prediction Output

```text
========== ML RESULTS ==========

R2 Score: 0.96

Predicted GDP

2025 : 21050

2026 : 22780

========== MODEL COMPLETED ==========
```

---

# 🗄 SQL Analytics

The project includes SQL queries for development analytics.

### Example Queries

```sql
SELECT AVG(GDP)
FROM gdp_development_data;
```

```sql
SELECT AVG(PerCapitaIncome)
FROM gdp_development_data;
```

```sql
SELECT AVG(HDI)
FROM gdp_development_data;
```

```sql
SELECT MAX(GDP)
FROM gdp_development_data;
```

```sql
SELECT Year, GDP
FROM gdp_development_data;
```

### SQL Insights

- GDP Analysis
- Income Analysis
- HDI Analysis
- Growth Rate Analysis
- Sector Contribution Analysis
- Development Rankings
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
========== GDP & DEVELOPMENT ANALYSIS ==========

Average GDP:
14580

Average Per Capita Income:
104800

Average HDI:
0.666

GDP Growth Rate:
95.00

Per Capita Income Growth:
100.00

Highest GDP Year:
2024

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
gdp_growth_trend.png
per_capita_income.png
sectoral_contribution.png
hdi_vs_gdp.png
economic_growth_rate.png
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
Future GDP Prediction
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
- GDP Analysis
- Per Capita Income Analysis
- Sectoral Contribution Analysis
- HDI Analysis
- Growth Rate Analysis
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

Explore complete development data.

### 📊 Statistical Summary

View descriptive statistics instantly.

### 📈 GDP Analysis

Track economic output growth.

### 💰 Income Analysis

Monitor per capita income growth.

### 🏭 Sector Analysis

Understand sectoral transformation.

### 🌍 HDI Analysis

Evaluate human development progress.

### 📉 Growth Rate Analysis

Measure annual economic performance.

### 🤖 Machine Learning Results

Explore future GDP forecasts.

### 🗄 SQL Query Explorer

Review development analytics SQL queries.

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

- GDP Measurement
- Economic Growth Analysis
- Per Capita Income Analysis
- Human Development Index (HDI)
- Sectoral Transformation
- Statistical Analysis
- SQL Analytics
- Data Visualization
- Machine Learning Prediction
- Dashboard Development

---

# 🌍 Real-World Applications

This project can be applied in:

- Economic Research
- Development Studies
- Policy Evaluation
- Academic Learning
- Data Analytics Training
- Economic Forecasting
- Dashboard Development
- Public Policy Analysis

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

Part of the **Foundational Economics Series (10 Projects)**

### Series Projects

1. Barter System
2. Money & Currency
3. Banking Fundamentals
4. Demand & Supply
5. Inflation Analytics
6. Budget & Taxation
7. Fiscal Deficit Analytics
8. RBI & Monetary Policy Analytics
9. Trade & Forex Analytics
10. GDP & Development Analytics

---

## 🚀 Learning Economics Through Data Analytics