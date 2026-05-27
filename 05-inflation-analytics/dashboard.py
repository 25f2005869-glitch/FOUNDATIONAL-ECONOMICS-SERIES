# ==========================================
# Author : Saloni Tiwari
# Project : Inflation Analytics
# File : dashboard.py
# Description : Streamlit Dashboard
# ==========================================

import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------------------------
# Page Settings
# ------------------------------------------

st.set_page_config(
    page_title="Inflation Analytics",
    layout="wide"
)

# ------------------------------------------
# Title
# ------------------------------------------

st.title("📈 Inflation Analytics Dashboard")

st.markdown("""
Analyze inflation trends, CPI, WPI,
purchasing power, income growth,
machine learning predictions,
and economic insights.
""")

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv(
    "data/inflation_data.csv"
)

# ------------------------------------------
# Dataset Explorer
# ------------------------------------------

st.subheader("📋 Dataset Explorer")

st.dataframe(
    df,
    use_container_width=True
)

# ------------------------------------------
# Statistical Summary
# ------------------------------------------

st.subheader("📊 Statistical Summary")

st.dataframe(
    df.describe(),
    use_container_width=True
)

# ------------------------------------------
# KPI Metrics
# ------------------------------------------

st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Inflation",
    round(df["InflationRate"].mean(),2)
)

col2.metric(
    "Average CPI",
    round(df["CPI"].mean(),2)
)

col3.metric(
    "Average WPI",
    round(df["WPI"].mean(),2)
)

# ------------------------------------------
# Inflation Trend
# ------------------------------------------

st.subheader("📈 Inflation Trend")

fig1 = px.line(
    df,
    x="Year",
    y="InflationRate",
    markers=True
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ------------------------------------------
# CPI vs WPI
# ------------------------------------------

st.subheader("📊 CPI vs WPI")

fig2 = px.line(
    df,
    x="Year",
    y=["CPI","WPI"]
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ------------------------------------------
# Purchasing Power
# ------------------------------------------

st.subheader("💰 Purchasing Power")

fig3 = px.bar(
    df,
    x="Year",
    y="PurchasingPower"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ------------------------------------------
# Inflation vs Income
# ------------------------------------------

st.subheader("💵 Inflation vs Income")

fig4 = px.scatter(
    df,
    x="AverageIncome",
    y="InflationRate"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# ------------------------------------------
# Correlation Matrix
# ------------------------------------------

st.subheader("🔗 Correlation Matrix")

corr = df[
    [
        "CPI",
        "WPI",
        "InflationRate",
        "AverageIncome",
        "PurchasingPower"
    ]
].corr()

st.dataframe(
    corr,
    use_container_width=True
)

# ------------------------------------------
# Machine Learning Results
# ------------------------------------------

st.subheader("🤖 Machine Learning Results")

st.image(
    "charts/feature_importance.png",
    caption="Feature Importance"
)

st.image(
    "charts/ml_prediction.png",
    caption="Actual vs Predicted Inflation"
)

# ------------------------------------------
# SQL Query Explorer
# ------------------------------------------

st.subheader("🗄 SQL Query Explorer")

with open(
    "sql/inflation_queries.sql",
    "r"
) as f:

    sql_code = f.read()

st.code(
    sql_code,
    language="sql"
)

# ------------------------------------------
# Economic Insights
# ------------------------------------------

st.subheader("📚 Economic Insights")

st.success("""
• Rising inflation reduces purchasing power.

• CPI measures consumer price changes.

• WPI measures wholesale price changes.

• Income growth can offset inflation impact.

• Long-term inflation influences economic planning.
""")

# ------------------------------------------
# Conclusion
# ------------------------------------------

st.subheader("✅ Conclusion")

st.info("""
Inflation affects prices, income,
purchasing power, savings, and
overall economic stability.

Monitoring inflation helps governments,
businesses, and citizens make better
economic decisions.
""")