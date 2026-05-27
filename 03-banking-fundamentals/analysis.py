# ==========================================
# Author : Saloni Tiwari
# Project : Banking Fundamentals Analytics
# File : analysis.py
# Description : Banking Sector Data Analysis
# ==========================================

import pandas as pd

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv(
    "data/banking_fundamentals_data.csv"
)

print("\n========== BANKING FUNDAMENTALS DATA ==========\n")
print(df)

# ------------------------------------------
# Basic Statistics
# ------------------------------------------

print("\n========== DESCRIPTIVE STATISTICS ==========\n")
print(df.describe())

# ------------------------------------------
# Total Deposits
# ------------------------------------------

total_deposits = df["Deposits"].sum()

print("\nTotal Deposits:")
print(total_deposits)

# ------------------------------------------
# Total Loans
# ------------------------------------------

total_loans = df["Loans"].sum()

print("\nTotal Loans:")
print(total_loans)

# ------------------------------------------
# Average Interest Rate
# ------------------------------------------

avg_interest = df["InterestRate"].mean()

print("\nAverage Interest Rate:")
print(round(avg_interest, 2))

# ------------------------------------------
# Maximum Deposit Year
# ------------------------------------------

max_deposit_year = df.loc[
    df["Deposits"].idxmax(),
    "Year"
]

print("\nHighest Deposit Year:")
print(max_deposit_year)

# ------------------------------------------
# Maximum Loan Year
# ------------------------------------------

max_loan_year = df.loc[
    df["Loans"].idxmax(),
    "Year"
]

print("\nHighest Loan Year:")
print(max_loan_year)

# ------------------------------------------
# Banking Growth Rate
# ------------------------------------------

growth_rate = (
    (
        df["BankingGrowth"].iloc[-1]
        -
        df["BankingGrowth"].iloc[0]
    )
    /
    df["BankingGrowth"].iloc[0]
) * 100

print("\nBanking Growth Increase (%):")
print(round(growth_rate, 2))

# ------------------------------------------
# Credit Deposit Ratio Average
# ------------------------------------------

avg_ratio = df["CreditDepositRatio"].mean()

print("\nAverage Credit Deposit Ratio:")
print(round(avg_ratio, 2))

# ------------------------------------------
# Correlation Matrix
# ------------------------------------------

print("\nCorrelation Matrix:\n")

correlation = df[
    [
        "Deposits",
        "Loans",
        "InterestRate",
        "CreditDepositRatio",
        "BankingGrowth"
    ]
].corr()

print(correlation)

# ------------------------------------------
# Top Performing Year
# ------------------------------------------

top_year = df.loc[
    df["BankingGrowth"].idxmax(),
    "Year"
]

print("\nBest Banking Growth Year:")
print(top_year)

# ------------------------------------------
# Final Summary
# ------------------------------------------

print("\n========== ANALYSIS COMPLETED ==========\n")