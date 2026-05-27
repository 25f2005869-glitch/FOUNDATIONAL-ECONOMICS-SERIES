# ==========================================
# Author : Saloni Tiwari
# Project : Trade & Forex Analytics
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
    page_title="Trade & Forex Analytics",
    layout="wide"
)

# ------------------------------------------
# Title
# ------------------------------------------

st.title(
    "🌍 Trade & Forex Analytics Dashboard"
)

st.markdown("""
Analyze exports, imports,
trade balance, exchange rates,
forex reserves and machine learning predictions.
""")

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv(
    "data/trade_forex_data.csv"
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
    "Avg Exports",
    round(
        df["Exports"].mean(),
        2
    )
)

col2.metric(
    "Avg Imports",
    round(
        df["Imports"].mean(),
        2
    )
)

col3.metric(
    "Avg Forex Reserves",
    round(
        df["ForexReserves"].mean(),
        2
    )
)

# ------------------------------------------
# Exports Growth
# ------------------------------------------

st.subheader(
    "📈 Exports Growth"
)

fig1 = px.line(
    df,
    x="Year",
    y="Exports",
    markers=True
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ------------------------------------------
# Imports Growth
# ------------------------------------------

st.subheader(
    "📉 Imports Growth"
)

fig2 = px.line(
    df,
    x="Year",
    y="Imports",
    markers=True
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ------------------------------------------
# Trade Balance Trend
# ------------------------------------------

st.subheader(
    "🌍 Trade Balance Trend"
)

fig3 = px.bar(
    df,
    x="Year",
    y="TradeBalance"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ------------------------------------------
# Exchange Rate Analysis
# ------------------------------------------

st.subheader(
    "💱 Exchange Rate Analysis"
)

fig4 = px.line(
    df,
    x="Year",
    y="ExchangeRate",
    markers=True
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# ------------------------------------------
# Forex Reserves Growth
# ------------------------------------------

st.subheader(
    "💰 Forex Reserves Growth"
)

fig5 = px.line(
    df,
    x="Year",
    y="ForexReserves",
    markers=True
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
        "Exports",
        "Imports",
        "TradeBalance",
        "ExchangeRate",
        "ForexReserves",
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
    caption="Actual vs Predicted Exports"
)

# ------------------------------------------
# SQL Query Explorer
# ------------------------------------------

st.subheader(
    "🗄 SQL Query Explorer"
)

with open(
    "sql/trade_forex_queries.sql",
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
    "📚 Trade & Forex Insights"
)

st.success("""
• Exports generate foreign exchange earnings.

• Imports satisfy domestic demand.

• Trade deficit occurs when imports exceed exports.

• Exchange rates affect international competitiveness.

• Forex reserves support currency stability.
""")

# ------------------------------------------
# Conclusion
# ------------------------------------------

st.subheader(
    "✅ Conclusion"
)

st.info("""
International trade and foreign exchange
markets play a crucial role in economic growth,
currency stability and global competitiveness.

Understanding these indicators helps analyze
external sector performance effectively.
""")