# ==========================================
# Author : Saloni Tiwari
# Project : Banking Fundamentals Analytics
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
    page_title="Banking Fundamentals Analytics",
    layout="wide"
)

st.write("BANKING PROJECT LOADED")

# ------------------------------------------
# Title
# ------------------------------------------

st.title("🏦 Banking Fundamentals Analytics Dashboard")

st.markdown("""
Explore banking deposits, loans, interest rates,
credit creation, and machine learning predictions.
""")

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv(
    "data/banking_fundamentals_data.csv"
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

st.subheader("📌 Key Banking Metrics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Deposits",
    round(df["Deposits"].mean(),2)
)

col2.metric(
    "Average Loans",
    round(df["Loans"].mean(),2)
)

col3.metric(
    "Average Interest Rate",
    round(df["InterestRate"].mean(),2)
)

# ------------------------------------------
# Deposits Growth
# ------------------------------------------

st.subheader("💰 Deposits Growth")

fig1 = px.line(
    df,
    x="Year",
    y="Deposits",
    markers=True
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ------------------------------------------
# Loans Growth
# ------------------------------------------

st.subheader("💳 Loans Growth")

fig2 = px.line(
    df,
    x="Year",
    y="Loans",
    markers=True
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ------------------------------------------
# Credit Deposit Ratio
# ------------------------------------------

st.subheader("📈 Credit Deposit Ratio")

fig3 = px.bar(
    df,
    x="Year",
    y="CreditDepositRatio"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ------------------------------------------
# Interest Rate Analysis
# ------------------------------------------

st.subheader("🏦 Interest Rate Analysis")

fig4 = px.line(
    df,
    x="Year",
    y="InterestRate",
    markers=True
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# ------------------------------------------
# Banking Sector Growth
# ------------------------------------------

st.subheader("📊 Banking Sector Growth")

fig5 = px.bar(
    df,
    x="Year",
    y="BankingGrowth"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

# ------------------------------------------
# Correlation Matrix
# ------------------------------------------

st.subheader("🔗 Correlation Matrix")

corr = df[
    [
        "Deposits",
        "Loans",
        "InterestRate",
        "CreditDepositRatio",
        "BankingGrowth"
    ]
].corr()

st.dataframe(
    corr,
    use_container_width=True
)

# ------------------------------------------
# Machine Learning Outputs
# ------------------------------------------

st.subheader("🤖 Machine Learning Results")

st.image(
    "charts/feature_importance.png",
    caption="Feature Importance"
)

st.image(
    "charts/ml_prediction.png",
    caption="Actual vs Predicted Deposits"
)

# ------------------------------------------
# SQL Query Explorer
# ------------------------------------------

st.subheader("🗄 SQL Query Explorer")

with open(
    "sql/banking_queries.sql",
    "r"
) as f:

    sql_code = f.read()

st.code(
    sql_code,
    language="sql"
)

# ------------------------------------------
# Banking Insights
# ------------------------------------------

st.subheader("📚 Banking Insights")

st.success("""
• Deposits increased consistently over time.

• Loan disbursement expanded steadily.

• Credit Deposit Ratio improved.

• Interest rates gradually declined.

• Banking sector growth remained positive.

• Machine learning can estimate future deposits.
""")

# ------------------------------------------
# Conclusion
# ------------------------------------------

st.subheader("✅ Conclusion")

st.info("""
Banks mobilize savings and create credit
for economic development.

Deposits, loans, and interest rates remain
key indicators of banking sector health.
""")