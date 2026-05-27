# ==========================================
# Author : Saloni Tiwari
# Project : Banking Fundamentals Analytics
# File : charts.py
# Description : Banking Visualizations
# ==========================================

import os
import pandas as pd
import matplotlib.pyplot as plt

# Create Charts Folder
os.makedirs(
    "charts",
    exist_ok=True
)

# Load Dataset
df = pd.read_csv(
    "data/banking_fundamentals_data.csv"
)

# ------------------------------------------
# Deposits Growth
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["Deposits"],
    marker="o"
)

plt.title("Deposits Growth")
plt.xlabel("Year")
plt.ylabel("Deposits")

plt.grid(True)

plt.savefig(
    "charts/deposits_growth.png"
)

plt.close()

# ------------------------------------------
# Loans Growth
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["Loans"],
    marker="o"
)

plt.title("Loans Growth")
plt.xlabel("Year")
plt.ylabel("Loans")

plt.grid(True)

plt.savefig(
    "charts/loans_growth.png"
)

plt.close()

# ------------------------------------------
# Credit Deposit Ratio
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.bar(
    df["Year"],
    df["CreditDepositRatio"]
)

plt.title(
    "Credit Deposit Ratio"
)

plt.xlabel("Year")
plt.ylabel("CD Ratio")

plt.savefig(
    "charts/credit_deposit_ratio.png"
)

plt.close()

# ------------------------------------------
# Interest Rate Analysis
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["InterestRate"],
    marker="o"
)

plt.title(
    "Interest Rate Analysis"
)

plt.xlabel("Year")
plt.ylabel("Interest Rate")

plt.grid(True)

plt.savefig(
    "charts/interest_rate_analysis.png"
)

plt.close()

# ------------------------------------------
# Banking Sector Growth
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.bar(
    df["Year"],
    df["BankingGrowth"]
)

plt.title(
    "Banking Sector Growth"
)

plt.xlabel("Year")
plt.ylabel("Growth (%)")

plt.savefig(
    "charts/banking_sector_growth.png"
)

plt.close()

print(
    "\nAll Banking Charts Generated Successfully.\n"
)