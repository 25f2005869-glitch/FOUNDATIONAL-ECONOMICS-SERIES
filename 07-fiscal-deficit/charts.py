# ==========================================
# Author : Saloni Tiwari
# Project : Fiscal Deficit Analytics
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
    "data/fiscal_deficit_data.csv"
)

# ------------------------------------------
# Fiscal Deficit Trend
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["FiscalDeficit"],
    marker="o"
)

plt.title(
    "Fiscal Deficit Trend"
)

plt.xlabel(
    "Year"
)

plt.ylabel(
    "Fiscal Deficit"
)

plt.grid(True)

plt.savefig(
    "charts/fiscal_deficit_trend.png"
)

plt.close()

# ------------------------------------------
# Revenue vs Expenditure
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["GovernmentRevenue"],
    marker="o",
    label="Revenue"
)

plt.plot(
    df["Year"],
    df["GovernmentExpenditure"],
    marker="s",
    label="Expenditure"
)

plt.title(
    "Revenue vs Expenditure"
)

plt.xlabel(
    "Year"
)

plt.ylabel(
    "Amount"
)

plt.legend()

plt.grid(True)

plt.savefig(
    "charts/revenue_vs_expenditure.png"
)

plt.close()

# ------------------------------------------
# Fiscal Deficit vs GDP
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["FiscalDeficit"],
    marker="o",
    label="Fiscal Deficit"
)

plt.plot(
    df["Year"],
    df["GDP"],
    marker="s",
    label="GDP"
)

plt.title(
    "Fiscal Deficit vs GDP"
)

plt.xlabel(
    "Year"
)

plt.ylabel(
    "Value"
)

plt.legend()

plt.grid(True)

plt.savefig(
    "charts/fiscal_deficit_vs_gdp.png"
)

plt.close()

# ------------------------------------------
# Public Debt Growth
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["PublicDebt"],
    marker="o"
)

plt.title(
    "Public Debt Growth"
)

plt.xlabel(
    "Year"
)

plt.ylabel(
    "Public Debt"
)

plt.grid(True)

plt.savefig(
    "charts/public_debt_growth.png"
)

plt.close()

# ------------------------------------------
# Borrowing Analysis
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.bar(
    df["Year"],
    df["Borrowing"]
)

plt.title(
    "Borrowing Analysis"
)

plt.xlabel(
    "Year"
)

plt.ylabel(
    "Borrowing"
)

plt.savefig(
    "charts/borrowing_analysis.png"
)

plt.close()

print(
    "\nAll Fiscal Deficit Charts Generated Successfully.\n"
)