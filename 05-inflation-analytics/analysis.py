# ==========================================
# Author : Saloni Tiwari
# Project : Inflation Analytics
# File : analysis.py
# Description : Statistical Analysis
# ==========================================

import pandas as pd

df = pd.read_csv("data/inflation_data.csv")

print("\n========== INFLATION ANALYSIS ==========\n")

print("Average Inflation Rate:")
print(round(df["InflationRate"].mean(),2))

print("\nAverage CPI:")
print(round(df["CPI"].mean(),2))

print("\nAverage WPI:")
print(round(df["WPI"].mean(),2))

print("\nAverage Income:")
print(round(df["AverageIncome"].mean(),2))

growth = (
    (
        df["InflationRate"].iloc[-1]
        -
        df["InflationRate"].iloc[0]
    )
    /
    df["InflationRate"].iloc[0]
) * 100

print("\nInflation Growth Rate (%):")
print(round(growth,2))

print("\nCorrelation Matrix:\n")

print(
    df[
        [
            "CPI",
            "WPI",
            "InflationRate",
            "AverageIncome",
            "PurchasingPower"
        ]
    ].corr()
)

print("\n========== ANALYSIS COMPLETED ==========\n")