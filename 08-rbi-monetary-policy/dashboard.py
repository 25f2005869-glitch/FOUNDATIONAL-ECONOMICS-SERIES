# ==========================================
# Author : Saloni Tiwari
# Project : RBI & Monetary Policy Analytics
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
    page_title="RBI & Monetary Policy Analytics",
    layout="wide"
)

# ------------------------------------------
# Title
# ------------------------------------------

st.title(
    "🏦 RBI & Monetary Policy Analytics Dashboard"
)

st.markdown("""
Analyze Repo Rate, Reverse Repo Rate,
CRR, SLR, Inflation, Money Supply,
and Machine Learning predictions.
""")

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv(
    "data/rbi_monetary_policy_data.csv"
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
    "Avg Repo Rate",
    round(
        df["RepoRate"].mean(),
        2
    )
)

col2.metric(
    "Avg Inflation",
    round(
        df["InflationRate"].mean(),
        2
    )
)

col3.metric(
    "Money Supply",
    int(
        df["MoneySupply"].iloc[-1]
    )
)

# ------------------------------------------
# Repo Rate Trend
# ------------------------------------------

st.subheader(
    "🏦 Repo Rate Trend"
)

fig1 = px.line(
    df,
    x="Year",
    y="RepoRate",
    markers=True
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ------------------------------------------
# Reverse Repo Trend
# ------------------------------------------

st.subheader(
    "💵 Reverse Repo Rate"
)

fig2 = px.line(
    df,
    x="Year",
    y="ReverseRepoRate",
    markers=True
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ------------------------------------------
# CRR vs SLR
# ------------------------------------------

st.subheader(
    "📈 CRR vs SLR Analysis"
)

fig3 = px.line(
    df,
    x="Year",
    y=[
        "CRR",
        "SLR"
    ]
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ------------------------------------------
# Inflation vs Repo Rate
# ------------------------------------------

st.subheader(
    "📉 Inflation vs Repo Rate"
)

fig4 = px.line(
    df,
    x="Year",
    y=[
        "InflationRate",
        "RepoRate"
    ]
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# ------------------------------------------
# Money Supply Growth
# ------------------------------------------

st.subheader(
    "💰 Money Supply Growth"
)

fig5 = px.bar(
    df,
    x="Year",
    y="MoneySupply"
)

st.plotly_chart(
    fig5,
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
        "RepoRate",
        "ReverseRepoRate",
        "CRR",
        "SLR",
        "InflationRate",
        "MoneySupply"
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
    caption="Actual vs Predicted Inflation"
)

# ------------------------------------------
# SQL Query Explorer
# ------------------------------------------

st.subheader(
    "🗄 SQL Query Explorer"
)

with open(
    "sql/rbi_monetary_policy_queries.sql",
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
    "📚 Monetary Policy Insights"
)

st.success("""
• Repo Rate controls borrowing costs.

• Reverse Repo absorbs excess liquidity.

• CRR regulates bank reserves.

• SLR ensures banking stability.

• Monetary policy helps control inflation.
""")

# ------------------------------------------
# Conclusion
# ------------------------------------------

st.subheader(
    "✅ Conclusion"
)

st.info("""
The RBI uses monetary policy tools
such as Repo Rate, Reverse Repo Rate,
CRR and SLR to manage inflation,
liquidity and economic stability.

Understanding these indicators helps
analyze the functioning of modern
financial systems.
""")