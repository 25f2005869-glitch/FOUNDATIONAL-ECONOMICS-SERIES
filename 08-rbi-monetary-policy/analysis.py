# ==========================================
# Author : Saloni Tiwari
# Project : RBI & Monetary Policy Analytics
# File : analysis.py
# Description : Statistical Analysis
# ==========================================

import pandas as pd

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv(
    "data/rbi_monetary_policy_data.csv"
)

print(
    "\n========== RBI MONETARY POLICY ANALYSIS ==========\n"
)

# ------------------------------------------
# Dataset Preview
# ------------------------------------------

print(df)

# ------------------------------------------
# Descriptive Statistics
# ------------------------------------------

print(
    "\n========== DESCRIPTIVE STATISTICS ==========\n"
)

print(df.describe())

# ------------------------------------------
# Repo Rate Analysis
# ------------------------------------------

print("\nAverage Repo Rate:")

print(
    round(
        df["RepoRate"].mean(),
        2
    )
)

# ------------------------------------------
# Reverse Repo Rate
# ------------------------------------------

print(
    "\nAverage Reverse Repo Rate:"
)

print(
    round(
        df["ReverseRepoRate"].mean(),
        2
    )
)

# ------------------------------------------
# CRR Analysis
# ------------------------------------------

print("\nAverage CRR:")

print(
    round(
        df["CRR"].mean(),
        2
    )
)

# ------------------------------------------
# SLR Analysis
# ------------------------------------------

print("\nAverage SLR:")

print(
    round(
        df["SLR"].mean(),
        2
    )
)

# ------------------------------------------
# Inflation Analysis
# ------------------------------------------

print(
    "\nAverage Inflation Rate:"
)

print(
    round(
        df["InflationRate"].mean(),
        2
    )
)

# ------------------------------------------
# Money Supply Growth
# ------------------------------------------

growth = (
    (
        df["MoneySupply"].iloc[-1]
        -
        df["MoneySupply"].iloc[0]
    )
    /
    df["MoneySupply"].iloc[0]
) * 100

print(
    "\nMoney Supply Growth (%):"
)

print(
    round(
        growth,
        2
    )
)

# ------------------------------------------
# Correlation Matrix
# ------------------------------------------

print(
    "\n========== CORRELATION MATRIX ==========\n"
)

corr = df[
    [
        "RepoRate",
        "ReverseRepoRate",
        "CRR",
        "SLR",
        "InflationRate",
        "MoneySupply"
    ]
].corr()

print(corr)

# ------------------------------------------
# Highest Inflation Year
# ------------------------------------------

highest_year = df.loc[
    df["InflationRate"].idxmax(),
    "Year"
]

print(
    "\nHighest Inflation Year:"
)

print(
    highest_year
)

print(
    "\n========== ANALYSIS COMPLETED ==========\n"
)