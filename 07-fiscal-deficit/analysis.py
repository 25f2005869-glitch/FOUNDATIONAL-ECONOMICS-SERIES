# ==========================================
# Author : Saloni Tiwari
# Project : Fiscal Deficit Analytics
# File : analysis.py
# Description : Statistical Analysis
# ==========================================

import pandas as pd

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv(
    "data/fiscal_deficit_data.csv"
)

print(
    "\n========== FISCAL DEFICIT ANALYSIS ==========\n"
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
# Fiscal Deficit Analysis
# ------------------------------------------

print("\nAverage Fiscal Deficit:")
print(
    round(
        df["FiscalDeficit"].mean(),
        2
    )
)

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
# Public Debt Analysis
# ------------------------------------------

print("\nAverage Public Debt:")
print(
    round(
        df["PublicDebt"].mean(),
        2
    )
)

# ------------------------------------------
# Borrowing Analysis
# ------------------------------------------

print("\nAverage Borrowing:")
print(
    round(
        df["Borrowing"].mean(),
        2
    )
)

# ------------------------------------------
# Fiscal Deficit Growth Rate
# ------------------------------------------

deficit_growth = (
    (
        df["FiscalDeficit"].iloc[-1]
        -
        df["FiscalDeficit"].iloc[0]
    )
    /
    df["FiscalDeficit"].iloc[0]
) * 100

print(
    "\nFiscal Deficit Growth Rate (%):"
)

print(
    round(
        deficit_growth,
        2
    )
)

# ------------------------------------------
# Debt Growth Rate
# ------------------------------------------

debt_growth = (
    (
        df["PublicDebt"].iloc[-1]
        -
        df["PublicDebt"].iloc[0]
    )
    /
    df["PublicDebt"].iloc[0]
) * 100

print(
    "\nPublic Debt Growth Rate (%):"
)

print(
    round(
        debt_growth,
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
        "FiscalDeficit",
        "PublicDebt",
        "Borrowing",
        "GDP"
    ]
].corr()

print(corr)

# ------------------------------------------
# Highest Deficit Year
# ------------------------------------------

highest_deficit_year = df.loc[
    df["FiscalDeficit"].idxmax(),
    "Year"
]

print(
    "\nHighest Fiscal Deficit Year:"
)

print(
    highest_deficit_year
)

print(
    "\n========== ANALYSIS COMPLETED ==========\n"
)