# ==========================================
# Author : Saloni Tiwari
# Project : Demand & Supply Analytics
# File : analysis.py
# Description : Statistical Analysis
# ==========================================

import pandas as pd

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv(
    "data/demand_supply_data.csv"
)

print("\n========== DEMAND & SUPPLY ANALYSIS ==========\n")

print(df)

# ------------------------------------------
# Statistical Summary
# ------------------------------------------

print("\n========== DESCRIPTIVE STATISTICS ==========\n")

print(df.describe())

# ------------------------------------------
# Average Values
# ------------------------------------------

print("\nAverage Demand:")
print(round(df["Demand"].mean(),2))

print("\nAverage Supply:")
print(round(df["Supply"].mean(),2))

print("\nAverage Price:")
print(round(df["Price"].mean(),2))

# ------------------------------------------
# Maximum Values
# ------------------------------------------

print("\nMaximum Demand:")
print(df["Demand"].max())

print("\nMaximum Supply:")
print(df["Supply"].max())

# ------------------------------------------
# Demand Growth
# ------------------------------------------

demand_growth = (
    (
        df["Demand"].iloc[-1]
        -
        df["Demand"].iloc[0]
    )
    /
    df["Demand"].iloc[0]
) * 100

print("\nDemand Growth Rate (%):")
print(round(demand_growth,2))

# ------------------------------------------
# Supply Growth
# ------------------------------------------

supply_growth = (
    (
        df["Supply"].iloc[-1]
        -
        df["Supply"].iloc[0]
    )
    /
    df["Supply"].iloc[0]
) * 100

print("\nSupply Growth Rate (%):")
print(round(supply_growth,2))

# ------------------------------------------
# Market Gap
# ------------------------------------------

df["MarketGap"] = (
    df["Demand"]
    -
    df["Supply"]
)

print("\nAverage Market Gap:")
print(round(df["MarketGap"].mean(),2))

# ------------------------------------------
# Correlation Matrix
# ------------------------------------------

print("\nCorrelation Matrix:\n")

corr = df[
    [
        "Price",
        "Demand",
        "Supply",
        "IncomeLevel",
        "Population"
    ]
].corr()

print(corr)

# ------------------------------------------
# Best Demand Year
# ------------------------------------------

best_year = df.loc[
    df["Demand"].idxmax(),
    "Year"
]

print("\nHighest Demand Year:")
print(best_year)

print(
    "\n========== ANALYSIS COMPLETED ==========\n"
)