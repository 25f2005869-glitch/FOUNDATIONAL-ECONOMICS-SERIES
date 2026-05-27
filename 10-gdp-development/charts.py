# ==========================================
# Author : Saloni Tiwari
# Project : GDP & Development Analytics
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
    "data/gdp_development_data.csv"
)

# ------------------------------------------
# GDP Growth Trend
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["GDP"],
    marker="o"
)

plt.title(
    "GDP Growth Trend"
)

plt.xlabel("Year")

plt.ylabel("GDP")

plt.grid(True)

plt.savefig(
    "charts/gdp_growth_trend.png"
)

plt.close()

# ------------------------------------------
# Per Capita Income
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["PerCapitaIncome"],
    marker="o"
)

plt.title(
    "Per Capita Income Growth"
)

plt.xlabel("Year")

plt.ylabel("Income")

plt.grid(True)

plt.savefig(
    "charts/per_capita_income.png"
)

plt.close()

# ------------------------------------------
# Sectoral Contribution
# ------------------------------------------

plt.figure(figsize=(10,6))

plt.plot(
    df["Year"],
    df["Agriculture"],
    marker="o",
    label="Agriculture"
)

plt.plot(
    df["Year"],
    df["Industry"],
    marker="s",
    label="Industry"
)

plt.plot(
    df["Year"],
    df["Services"],
    marker="^",
    label="Services"
)

plt.title(
    "Sectoral Contribution"
)

plt.xlabel("Year")

plt.ylabel("Percentage Share")

plt.legend()

plt.grid(True)

plt.savefig(
    "charts/sectoral_contribution.png"
)

plt.close()

# ------------------------------------------
# HDI vs GDP
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.scatter(
    df["GDP"],
    df["HDI"]
)

plt.title(
    "HDI vs GDP"
)

plt.xlabel("GDP")

plt.ylabel("HDI")

plt.grid(True)

plt.savefig(
    "charts/hdi_vs_gdp.png"
)

plt.close()

# ------------------------------------------
# Economic Growth Rate
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.bar(
    df["Year"],
    df["GrowthRate"]
)

plt.title(
    "Economic Growth Rate"
)

plt.xlabel("Year")

plt.ylabel("Growth Rate (%)")

plt.savefig(
    "charts/economic_growth_rate.png"
)

plt.close()

print(
    "\nAll GDP & Development Charts Generated Successfully.\n"
)