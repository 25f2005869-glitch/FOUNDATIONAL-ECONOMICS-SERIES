# ==========================================
# Author : Saloni Tiwari
# Project : Budget & Taxation Analytics
# File : dashboard.py
# Description : Streamlit Dashboard
# ==========================================

import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------------------------
# Page Config
# ------------------------------------------

st.set_page_config(
    page_title="Budget & Taxation Analytics",
    layout="wide"
)

# ------------------------------------------
# Title
# ------------------------------------------

st.title(
    "💰 Budget & Taxation Analytics Dashboard"
)

st.markdown("""
Analyze government revenue,
government expenditure,
tax collections,
fiscal balance,
and machine learning predictions.
""")

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv(
    "data/budget_taxation_data.csv"
)

# ------------------------------------------
# Dataset Explorer
# ------------------------------------------

st.subheader(
    "📋 Dataset Explorer"
)

st.dataframe(
    df,
    use_container_width=True
)

# ------------------------------------------
# Statistical Summary
# ------------------------------------------

st.subheader(
    "📊 Statistical Summary"
)

st.dataframe(
    df.describe(),
    use_container_width=True
)

# ------------------------------------------
# KPI Metrics
# ------------------------------------------

st.subheader(
    "📌 Key Metrics"
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Avg Revenue",
    round(
        df["GovernmentRevenue"].mean(),
        2
    )
)

col2.metric(
    "Avg Expenditure",
    round(
        df["GovernmentExpenditure"].mean(),
        2
    )
)

col3.metric(
    "Avg Fiscal Balance",
    round(
        df["FiscalBalance"].mean(),
        2
    )
)

# ------------------------------------------
# Revenue Trend
# ------------------------------------------

st.subheader(
    "📈 Government Revenue Trend"
)

fig1 = px.line(
    df,
    x="Year",
    y="GovernmentRevenue",
    markers=True
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ------------------------------------------
# Expenditure Trend
# ------------------------------------------

st.subheader(
    "🏛 Government Expenditure Trend"
)

fig2 = px.line(
    df,
    x="Year",
    y="GovernmentExpenditure",
    markers=True
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ------------------------------------------
# Direct vs Indirect Tax
# ------------------------------------------

st.subheader(
    "💵 Direct vs Indirect Tax"
)

fig3 = px.line(
    df,
    x="Year",
    y=[
        "DirectTax",
        "IndirectTax"
    ]
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ------------------------------------------
# Fiscal Balance
# ------------------------------------------

st.subheader(
    "📉 Fiscal Balance Trend"
)

fig4 = px.bar(
    df,
    x="Year",
    y="FiscalBalance"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# ------------------------------------------
# Correlation Matrix
# ------------------------------------------

st.subheader(
    "🔗 Correlation Matrix"
)

corr = df[
    [
        "GovernmentRevenue",
        "GovernmentExpenditure",
        "DirectTax",
        "IndirectTax",
        "FiscalBalance",
        "GDP"
    ]
].corr()

st.dataframe(
    corr,
    use_container_width=True
)

# ------------------------------------------
# Machine Learning Results
# ------------------------------------------

st.subheader(
    "🤖 Machine Learning Results"
)

st.image(
    "charts/feature_importance.png",
    caption="Feature Importance"
)

st.image(
    "charts/ml_prediction.png",
    caption="Actual vs Predicted Revenue"
)

# ------------------------------------------
# SQL Query Explorer
# ------------------------------------------

st.subheader(
    "🗄 SQL Query Explorer"
)

with open(
    "sql/budget_taxation_queries.sql",
    "r",
    encoding="utf-8"
) as f:

    sql_code = f.read()

st.code(
    sql_code,
    language="sql"
)

# ------------------------------------------
# Economic Insights
# ------------------------------------------

st.subheader(
    "📚 Economic Insights"
)

st.success("""
• Government revenue funds public services.

• Direct taxes are collected from income and profits.

• Indirect taxes are collected on goods and services.

• Fiscal deficits occur when expenditure exceeds revenue.

• Sustainable taxation supports economic growth.
""")

# ------------------------------------------
# Conclusion
# ------------------------------------------

st.subheader(
    "✅ Conclusion"
)

st.info("""
Government budgets influence economic growth,
public welfare, infrastructure development,
and fiscal sustainability.

Understanding taxation and expenditure patterns
helps evaluate public finance management.
""")