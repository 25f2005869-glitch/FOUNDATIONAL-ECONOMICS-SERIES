# ==========================================
# Author : Saloni Tiwari
# Project : GDP & Development Analytics
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
    page_title="GDP & Development Analytics",
    layout="wide"
)

# ------------------------------------------
# Title
# ------------------------------------------

st.title(
    "📊 GDP & Development Analytics Dashboard"
)

st.markdown("""
Analyze GDP growth, per capita income,
sectoral contribution, HDI and
machine learning predictions.
""")

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv(
    "data/gdp_development_data.csv"
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
    "Average GDP",
    round(
        df["GDP"].mean(),
        2
    )
)

col2.metric(
    "Average HDI",
    round(
        df["HDI"].mean(),
        3
    )
)

col3.metric(
    "Average Income",
    round(
        df["PerCapitaIncome"].mean(),
        2
    )
)

# ------------------------------------------
# GDP Trend
# ------------------------------------------

st.subheader(
    "📈 GDP Growth Trend"
)

fig1 = px.line(
    df,
    x="Year",
    y="GDP",
    markers=True
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ------------------------------------------
# Per Capita Income
# ------------------------------------------

st.subheader(
    "💰 Per Capita Income"
)

fig2 = px.line(
    df,
    x="Year",
    y="PerCapitaIncome",
    markers=True
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ------------------------------------------
# Sector Contribution
# ------------------------------------------

st.subheader(
    "🏭 Sectoral Contribution"
)

fig3 = px.line(
    df,
    x="Year",
    y=[
        "Agriculture",
        "Industry",
        "Services"
    ]
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ------------------------------------------
# HDI Analysis
# ------------------------------------------

st.subheader(
    "🌍 HDI vs GDP"
)

fig4 = px.scatter(
    df,
    x="GDP",
    y="HDI"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# ------------------------------------------
# Growth Rate
# ------------------------------------------

st.subheader(
    "📉 Economic Growth Rate"
)

fig5 = px.bar(
    df,
    x="Year",
    y="GrowthRate"
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
        "GDP",
        "PerCapitaIncome",
        "Agriculture",
        "Industry",
        "Services",
        "HDI",
        "GrowthRate"
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
    caption="Actual vs Predicted GDP"
)

# ------------------------------------------
# SQL Query Explorer
# ------------------------------------------

st.subheader(
    "🗄 SQL Query Explorer"
)

with open(
    "sql/gdp_development_queries.sql",
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
    "📚 Development Insights"
)

st.success("""
• GDP measures economic output.

• Per capita income reflects living standards.

• Agriculture, industry and services drive growth.

• HDI captures broader human development.

• Sustainable growth improves quality of life.
""")

# ------------------------------------------
# Conclusion
# ------------------------------------------

st.subheader(
    "✅ Conclusion"
)

st.info("""
GDP and development indicators help
evaluate economic performance,
living standards and long-term growth.

Understanding these indicators provides
valuable insights into national progress.
""")