# ==========================================
# Author : Saloni Tiwari
# Project : Money & Currency Analytics
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
    page_title="Money & Currency Analytics",
    layout="wide"
)

# ------------------------------------------
# Title
# ------------------------------------------

st.title(
    "💰 Money & Currency Analytics"
)

st.markdown(
    """
This dashboard explores the evolution of money,
currency circulation, digital payments, inflation,
money supply, SQL analytics, and machine learning
predictions.
"""
)

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv(
    "data/money_currency_data.csv"
)

# ------------------------------------------
# Dataset
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

with col1:
    st.metric(
        "Avg Inflation",
        round(
            df["InflationRate"].mean(),
            2
        )
    )

with col2:
    st.metric(
        "Avg Money Supply",
        round(
            df["MoneySupply"].mean(),
            2
        )
    )

with col3:
    st.metric(
        "Avg Currency",
        round(
            df["CurrencyInCirculation"].mean(),
            2
        )
    )

# ------------------------------------------
# Currency Circulation
# ------------------------------------------

st.subheader(
    "💵 Currency Circulation"
)

fig1 = px.line(
    df,
    x="Year",
    y="CurrencyInCirculation",
    markers=True
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ------------------------------------------
# Digital Payments
# ------------------------------------------

st.subheader(
    "📱 Digital Payments Growth"
)

fig2 = px.bar(
    df,
    x="Year",
    y="DigitalPayments"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ------------------------------------------
# Inflation vs Money Supply
# ------------------------------------------

st.subheader(
    "📈 Inflation vs Money Supply"
)

fig3 = px.line(
    df,
    x="Year",
    y=[
        "InflationRate",
        "MoneySupply"
    ]
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ------------------------------------------
# Correlation Matrix Table
# ------------------------------------------

st.subheader(
    "🔗 Correlation Matrix"
)

corr = df[
    [
        "CurrencyInCirculation",
        "DigitalPayments",
        "InflationRate",
        "MoneySupply"
    ]
].corr()

st.dataframe(
    corr,
    use_container_width=True
)

# ------------------------------------------
# ML Results
# ------------------------------------------

st.subheader(
    "🤖 Machine Learning Outputs"
)

st.image(
    "charts/feature_importance.png",
    caption="Feature Importance"
)

st.image(
    "charts/ml_prediction.png",
    caption="Actual vs Predicted"
)

# ------------------------------------------
# SQL Queries
# ------------------------------------------

st.subheader(
    "🗄 SQL Query Explorer"
)

with open(
    "sql/money_currency_queries.sql",
    "r"
) as f:

    sql_code = f.read()

st.code(
    sql_code,
    language="sql"
)

# ------------------------------------------
# Key Insights
# ------------------------------------------

st.subheader(
    "📚 Economics Insights"
)

st.success(
    """
• Currency circulation increased steadily.

• Digital payments grew rapidly.

• Money supply expanded over time.

• Inflation remained relatively stable.

• Machine learning can predict future
  currency circulation using economic indicators.
"""
)

# ------------------------------------------
# Conclusion
# ------------------------------------------

st.subheader(
    "✅ Conclusion"
)

st.info(
    """
Money evolved from barter systems to
modern digital payments.

Currency circulation, inflation,
and money supply remain key indicators
for understanding economic activity.
"""
)