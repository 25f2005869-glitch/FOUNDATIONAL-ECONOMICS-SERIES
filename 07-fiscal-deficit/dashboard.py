# ==========================================
# Author : Saloni Tiwari
# Project : Fiscal Deficit Analytics
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
    page_title="Fiscal Deficit Analytics",
    layout="wide"
)

# ------------------------------------------
# Title
# ------------------------------------------

st.title(
    "📉 Fiscal Deficit Analytics Dashboard"
)

st.markdown("""
Analyze fiscal deficit, public debt,
government borrowing, revenue,
expenditure and machine learning predictions.
""")

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv(
    "data/fiscal_deficit_data.csv"
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
    "Avg Fiscal Deficit",
    round(df["FiscalDeficit"].mean(),2)
)

col2.metric(
    "Avg Public Debt",
    round(df["PublicDebt"].mean(),2)
)

col3.metric(
    "Avg Borrowing",
    round(df["Borrowing"].mean(),2)
)

# ------------------------------------------
# Fiscal Deficit Trend
# ------------------------------------------

st.subheader(
    "📉 Fiscal Deficit Trend"
)

fig1 = px.line(
    df,
    x="Year",
    y="FiscalDeficit",
    markers=True
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ------------------------------------------
# Revenue vs Expenditure
# ------------------------------------------

st.subheader(
    "💰 Revenue vs Expenditure"
)

fig2 = px.line(
    df,
    x="Year",
    y=[
        "GovernmentRevenue",
        "GovernmentExpenditure"
    ]
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ------------------------------------------
# Public Debt
# ------------------------------------------

st.subheader(
    "💳 Public Debt Growth"
)

fig3 = px.line(
    df,
    x="Year",
    y="PublicDebt",
    markers=True
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ------------------------------------------
# Borrowing Analysis
# ------------------------------------------

st.subheader(
    "🏦 Borrowing Analysis"
)

fig4 = px.bar(
    df,
    x="Year",
    y="Borrowing"
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
        "FiscalDeficit",
        "PublicDebt",
        "Borrowing",
        "GDP"
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
    "🤖 Machine Learning Results"
)

st.image(
    "charts/feature_importance.png",
    caption="Feature Importance"
)

st.image(
    "charts/ml_prediction.png",
    caption="Actual vs Predicted Fiscal Deficit"
)

# ------------------------------------------
# SQL Query Explorer
# ------------------------------------------

st.subheader(
    "🗄 SQL Query Explorer"
)

with open(
    "sql/fiscal_deficit_queries.sql",
    "r",
    encoding="utf-8"
) as f:

    sql_code = f.read()

st.code(
    sql_code,
    language="sql"
)

# ------------------------------------------
# Insights
# ------------------------------------------

st.subheader(
    "📚 Economic Insights"
)

st.success("""
• Fiscal deficit occurs when expenditure exceeds revenue.

• Persistent deficits increase public debt.

• Borrowing finances government spending.

• GDP growth improves fiscal sustainability.

• Responsible fiscal management supports stability.
""")

# ------------------------------------------
# Conclusion
# ------------------------------------------

st.subheader(
    "✅ Conclusion"
)

st.info("""
Fiscal deficits affect debt levels,
interest obligations, economic stability,
and future government spending capacity.

Monitoring deficits is essential for
sustainable economic growth.
""")