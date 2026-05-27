# ==========================================
# Author : Saloni Tiwari
# Project : Demand & Supply Analytics
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
    page_title="Demand & Supply Analytics",
    layout="wide"
)

# ------------------------------------------
# Title
# ------------------------------------------

st.title("📈 Demand & Supply Analytics Dashboard")

st.markdown("""
Analyze demand, supply, market equilibrium,
elasticity, and machine learning predictions.
""")

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv(
    "data/demand_supply_data.csv"
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
    "Average Demand",
    round(df["Demand"].mean(),2)
)

col2.metric(
    "Average Supply",
    round(df["Supply"].mean(),2)
)

col3.metric(
    "Average Price",
    round(df["Price"].mean(),2)
)

# ------------------------------------------
# Demand Trend
# ------------------------------------------

st.subheader("📈 Demand Trend")

fig1 = px.line(
    df,
    x="Year",
    y="Demand",
    markers=True
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ------------------------------------------
# Supply Trend
# ------------------------------------------

st.subheader("📊 Supply Trend")

fig2 = px.line(
    df,
    x="Year",
    y="Supply",
    markers=True
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ------------------------------------------
# Price Trend
# ------------------------------------------

st.subheader("💰 Price Trend")

fig3 = px.line(
    df,
    x="Year",
    y="Price",
    markers=True
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ------------------------------------------
# Market Equilibrium
# ------------------------------------------

st.subheader("⚖ Market Equilibrium")

fig4 = px.line(
    df,
    x="Price",
    y=["Demand","Supply"]
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
        "Price",
        "Demand",
        "Supply",
        "IncomeLevel",
        "Population"
    ]
].corr()

st.dataframe(
    corr,
    use_container_width=True
)

# ------------------------------------------
# Machine Learning
# ------------------------------------------

st.subheader("🤖 Machine Learning Results")

st.image(
    "charts/feature_importance.png",
    caption="Feature Importance"
)

st.image(
    "charts/ml_prediction.png",
    caption="Actual vs Predicted Demand"
)

# ------------------------------------------
# SQL Query Explorer
# ------------------------------------------

st.subheader("🗄 SQL Query Explorer")

with open(
    "sql/demand_supply_queries.sql",
    "r"
) as f:

    sql_code = f.read()

st.code(
    sql_code,
    language="sql"
)

# ------------------------------------------
# Insights
# ------------------------------------------

st.subheader("📚 Economic Insights")

st.success("""
• Demand decreases as price increases.

• Supply increases as price increases.

• Market equilibrium balances buyers and sellers.

• Income growth influences demand.

• Population growth increases market demand.
""")

# ------------------------------------------
# Conclusion
# ------------------------------------------

st.subheader("✅ Conclusion")

st.info("""
Demand and Supply are fundamental economic forces
that determine prices and quantities in markets.

Understanding equilibrium helps explain market behavior.
""")