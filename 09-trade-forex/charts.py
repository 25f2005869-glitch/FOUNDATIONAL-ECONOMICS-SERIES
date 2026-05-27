# ==========================================
# Author : Saloni Tiwari
# Project : Trade & Forex Analytics
# File : charts.py
# Description : Data Visualizations
# ==========================================

import os
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------
# Create Charts Folder
# ------------------------------------------

os.makedirs(
    "charts",
    exist_ok=True
)

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv(
    "data/trade_forex_data.csv"
)

# ------------------------------------------
# Exports Growth
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["Exports"],
    marker="o"
)

plt.title(
    "Exports Growth"
)

plt.xlabel("Year")

plt.ylabel("Exports")

plt.grid(True)

plt.savefig(
    "charts/exports_growth.png"
)

plt.close()

# ------------------------------------------
# Imports Growth
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["Imports"],
    marker="o"
)

plt.title(
    "Imports Growth"
)

plt.xlabel("Year")

plt.ylabel("Imports")

plt.grid(True)

plt.savefig(
    "charts/imports_growth.png"
)

plt.close()

# ------------------------------------------
# Trade Balance Trend
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.bar(
    df["Year"],
    df["TradeBalance"]
)

plt.title(
    "Trade Balance Trend"
)

plt.xlabel("Year")

plt.ylabel("Trade Balance")

plt.savefig(
    "charts/trade_balance_trend.png"
)

plt.close()

# ------------------------------------------
# Exchange Rate Analysis
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["ExchangeRate"],
    marker="o"
)

plt.title(
    "Exchange Rate Analysis"
)

plt.xlabel("Year")

plt.ylabel("INR per USD")

plt.grid(True)

plt.savefig(
    "charts/exchange_rate_analysis.png"
)

plt.close()

# ------------------------------------------
# Forex Reserves Growth
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["ForexReserves"],
    marker="o"
)

plt.title(
    "Forex Reserves Growth"
)

plt.xlabel("Year")

plt.ylabel("Forex Reserves")

plt.grid(True)

plt.savefig(
    "charts/forex_reserves_growth.png"
)

plt.close()

print(
    "\nAll Trade & Forex Charts Generated Successfully.\n"
)