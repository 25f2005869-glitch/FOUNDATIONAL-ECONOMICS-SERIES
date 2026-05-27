# ==========================================
# Author : Saloni Tiwari
# Project : Budget & Taxation Analytics
# File : analysis.py
# Description : Statistical Analysis
# ==========================================

import pandas as pd

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv(
    "data/budget_taxation_data.csv"
)

print(
    "\n========== BUDGET & TAXATION ANALYSIS ==========\n"
)

# ------------------------------------------
# Dataset Preview
# ------------------------------------------

print(df)

# ------------------------------------------
# Statistical Summary
# ------------------------------------------

print(
    "\n========== DESCRIPTIVE STATISTICS ==========\n"
)

print(df.describe())

# ------------------------------------------
# Revenue Analysis
# ------------------------------------------

print("\nAverage Government Revenue:")
print(
    round(
        df["GovernmentRevenue"].mean(),
        2
    )
)

# ------------------------------------------
# Expenditure Analysis
# ------------------------------------------

print("\nAverage Government Expenditure:")
print(
    round(
        df["GovernmentExpenditure"].mean(),
        2
    )
)

# ------------------------------------------
# Direct Tax Analysis
# ------------------------------------------

print("\nAverage Direct Tax:")
print(
    round(
        df["DirectTax"].mean(),
        2
    )
)

# ------------------------------------------
# Indirect Tax Analysis
# ------------------------------------------

print("\nAverage Indirect Tax:")
print(
    round(
        df["IndirectTax"].mean(),
        2
    )
)

# ------------------------------------------
# Fiscal Balance
# ------------------------------------------

print("\nAverage Fiscal Balance:")
print(
    round(
        df["FiscalBalance"].mean(),
        2
    )
)

# ------------------------------------------
# Revenue Growth Rate
# ------------------------------------------

revenue_growth = (
    (
        df["GovernmentRevenue"].iloc[-1]
        -
        df["GovernmentRevenue"].iloc[0]
    )
    /
    df["GovernmentRevenue"].iloc[0]
) * 100

print("\nRevenue Growth Rate (%):")
print(
    round(
        revenue_growth,
        2
    )
)

# ------------------------------------------
# Expenditure Growth Rate
# ------------------------------------------

expenditure_growth = (
    (
        df["GovernmentExpenditure"].iloc[-1]
        -
        df["GovernmentExpenditure"].iloc[0]
    )
    /
    df["GovernmentExpenditure"].iloc[0]
) * 100

print("\nExpenditure Growth Rate (%):")
print(
    round(
        expenditure_growth,
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
        "GovernmentRevenue",
        "GovernmentExpenditure",
        "DirectTax",
        "IndirectTax",
        "FiscalBalance",
        "GDP"
    ]
].corr()

print(corr)

# ------------------------------------------
# Best Revenue Year
# ------------------------------------------

best_year = df.loc[
    df["GovernmentRevenue"].idxmax(),
    "Year"
]

print("\nHighest Revenue Year:")
print(best_year)

print(
    "\n========== ANALYSIS COMPLETED ==========\n"
)