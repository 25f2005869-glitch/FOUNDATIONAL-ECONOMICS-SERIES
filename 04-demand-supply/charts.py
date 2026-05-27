# ==========================================
# Author : Saloni Tiwari
# Project : Demand & Supply Analytics
# File : charts.py
# Description : Visualizations
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
    "data/demand_supply_data.csv"
)

# ------------------------------------------
# Demand Curve
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Price"],
    df["Demand"],
    marker="o"
)

plt.title(
    "Demand Curve"
)

plt.xlabel("Price")

plt.ylabel("Demand")

plt.grid(True)

plt.savefig(
    "charts/demand_curve.png"
)

plt.close()

# ------------------------------------------
# Supply Curve
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Price"],
    df["Supply"],
    marker="o"
)

plt.title(
    "Supply Curve"
)

plt.xlabel("Price")

plt.ylabel("Supply")

plt.grid(True)

plt.savefig(
    "charts/supply_curve.png"
)

plt.close()

# ------------------------------------------
# Market Equilibrium
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Price"],
    df["Demand"],
    marker="o",
    label="Demand"
)

plt.plot(
    df["Price"],
    df["Supply"],
    marker="s",
    label="Supply"
)

plt.title(
    "Market Equilibrium"
)

plt.xlabel("Price")

plt.ylabel("Quantity")

plt.legend()

plt.grid(True)

plt.savefig(
    "charts/market_equilibrium.png"
)

plt.close()

# ------------------------------------------
# Price vs Quantity Trend
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["Price"],
    marker="o",
    label="Price"
)

plt.plot(
    df["Year"],
    df["Demand"],
    marker="s",
    label="Demand"
)

plt.plot(
    df["Year"],
    df["Supply"],
    marker="^",
    label="Supply"
)

plt.title(
    "Price Quantity Trend"
)

plt.xlabel("Year")

plt.ylabel("Value")

plt.legend()

plt.grid(True)

plt.savefig(
    "charts/price_quantity_trend.png"
)

plt.close()

# ------------------------------------------
# Elasticity Analysis
# ------------------------------------------

elasticity = (
    df["Demand"].pct_change()
    /
    df["Price"].pct_change()
)

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"][1:],
    elasticity[1:],
    marker="o"
)

plt.title(
    "Elasticity Analysis"
)

plt.xlabel("Year")

plt.ylabel("Elasticity")

plt.grid(True)

plt.savefig(
    "charts/elasticity_analysis.png"
)

plt.close()

print(
    "\nAll Demand & Supply Charts Generated Successfully.\n"
)