# ==========================================
# Author : Saloni Tiwari
# Project : RBI & Monetary Policy Analytics
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
    "data/rbi_monetary_policy_data.csv"
)

# ------------------------------------------
# Repo Rate Trend
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["RepoRate"],
    marker="o"
)

plt.title(
    "Repo Rate Trend"
)

plt.xlabel("Year")

plt.ylabel("Repo Rate (%)")

plt.grid(True)

plt.savefig(
    "charts/repo_rate_trend.png"
)

plt.close()

# ------------------------------------------
# Reverse Repo Rate
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["ReverseRepoRate"],
    marker="o",
    color="green"
)

plt.title(
    "Reverse Repo Rate Analysis"
)

plt.xlabel("Year")

plt.ylabel(
    "Reverse Repo Rate (%)"
)

plt.grid(True)

plt.savefig(
    "charts/reverse_repo_rate.png"
)

plt.close()

# ------------------------------------------
# CRR vs SLR
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["CRR"],
    marker="o",
    label="CRR"
)

plt.plot(
    df["Year"],
    df["SLR"],
    marker="s",
    label="SLR"
)

plt.title(
    "CRR vs SLR Analysis"
)

plt.xlabel("Year")

plt.ylabel("Rate (%)")

plt.legend()

plt.grid(True)

plt.savefig(
    "charts/crr_slr_analysis.png"
)

plt.close()

# ------------------------------------------
# Inflation vs Repo Rate
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["InflationRate"],
    marker="o",
    label="Inflation"
)

plt.plot(
    df["Year"],
    df["RepoRate"],
    marker="s",
    label="Repo Rate"
)

plt.title(
    "Inflation vs Repo Rate"
)

plt.xlabel("Year")

plt.ylabel("Percentage")

plt.legend()

plt.grid(True)

plt.savefig(
    "charts/inflation_vs_repo_rate.png"
)

plt.close()

# ------------------------------------------
# Money Supply Growth
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.bar(
    df["Year"],
    df["MoneySupply"]
)

plt.title(
    "Money Supply Growth"
)

plt.xlabel("Year")

plt.ylabel("Money Supply")

plt.savefig(
    "charts/money_supply_growth.png"
)

plt.close()

print(
    "\nAll RBI Monetary Policy Charts Generated Successfully.\n"
)