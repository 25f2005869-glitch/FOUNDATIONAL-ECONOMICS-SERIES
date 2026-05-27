# ==========================================
# Author : Saloni Tiwari
# Project : Inflation Analytics
# File : charts.py
# Description : Data Visualizations
# ==========================================

import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/inflation_data.csv")

# Inflation Trend

plt.figure(figsize=(8,5))
plt.plot(df["Year"], df["InflationRate"], marker="o")
plt.title("Inflation Trend")
plt.xlabel("Year")
plt.ylabel("Inflation Rate")
plt.grid(True)
plt.savefig("charts/inflation_trend.png")
plt.close()

# CPI vs WPI

plt.figure(figsize=(8,5))
plt.plot(df["Year"], df["CPI"], marker="o", label="CPI")
plt.plot(df["Year"], df["WPI"], marker="o", label="WPI")
plt.legend()
plt.title("CPI vs WPI")
plt.savefig("charts/cpi_vs_wpi.png")
plt.close()

# Purchasing Power

plt.figure(figsize=(8,5))
plt.bar(df["Year"], df["PurchasingPower"])
plt.title("Purchasing Power")
plt.savefig("charts/purchasing_power.png")
plt.close()

# Inflation vs Income

plt.figure(figsize=(8,5))
plt.scatter(df["AverageIncome"], df["InflationRate"])
plt.title("Inflation vs Income")
plt.xlabel("Income")
plt.ylabel("Inflation")
plt.savefig("charts/inflation_vs_income.png")
plt.close()

# Growth Rate

plt.figure(figsize=(8,5))
plt.plot(df["Year"], df["InflationRate"].pct_change()*100)
plt.title("Inflation Growth Rate")
plt.savefig("charts/inflation_growth_rate.png")
plt.close()

print("Charts Generated Successfully")