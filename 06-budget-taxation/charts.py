# ==========================================
# Author : Saloni Tiwari
# Project : Budget & Taxation Analytics
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
    "data/budget_taxation_data.csv"
)

# ------------------------------------------
# Government Revenue
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["GovernmentRevenue"],
    marker="o"
)

plt.title(
    "Government Revenue Trend"
)

plt.xlabel("Year")

plt.ylabel("Revenue")

plt.grid(True)

plt.savefig(
    "charts/government_revenue.png"
)

plt.close()

# ------------------------------------------
# Government Expenditure
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["GovernmentExpenditure"],
    marker="o"
)

plt.title(
    "Government Expenditure Trend"
)

plt.xlabel("Year")

plt.ylabel("Expenditure")

plt.grid(True)

plt.savefig(
    "charts/government_expenditure.png"
)

plt.close()

# ------------------------------------------
# Direct vs Indirect Tax
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["DirectTax"],
    marker="o",
    label="Direct Tax"
)

plt.plot(
    df["Year"],
    df["IndirectTax"],
    marker="s",
    label="Indirect Tax"
)

plt.title(
    "Direct vs Indirect Tax"
)

plt.xlabel("Year")

plt.ylabel("Tax Collection")

plt.legend()

plt.grid(True)

plt.savefig(
    "charts/direct_vs_indirect_tax.png"
)

plt.close()

# ------------------------------------------
# Fiscal Balance Trend
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.bar(
    df["Year"],
    df["FiscalBalance"]
)

plt.title(
    "Fiscal Balance Trend"
)

plt.xlabel("Year")

plt.ylabel("Fiscal Balance")

plt.savefig(
    "charts/fiscal_balance_trend.png"
)

plt.close()

# ------------------------------------------
# Tax Revenue Growth
# ------------------------------------------

tax_total = (
    df["DirectTax"]
    +
    df["IndirectTax"]
)

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    tax_total,
    marker="o"
)

plt.title(
    "Tax Revenue Growth"
)

plt.xlabel("Year")

plt.ylabel("Total Tax Revenue")

plt.grid(True)

plt.savefig(
    "charts/tax_revenue_growth.png"
)

plt.close()

print(
    "\nAll Budget & Taxation Charts Generated Successfully.\n"
)