# ==========================================
# Author : Saloni Tiwari
# Project : Money & Currency Analytics
# File : analysis.py
# Description : Statistical Analysis
# ==========================================

import pandas as pd

# Load Dataset
df = pd.read_csv("data/money_currency_data.csv")

print("\n========== MONEY & CURRENCY ANALYSIS ==========\n")

# Basic Statistics
print("Dataset Summary")
print(df.describe())

# Mean Values
print("\nAverage Currency Circulation:")
print(round(df["CurrencyInCirculation"].mean(), 2))

print("\nAverage Digital Payments:")
print(round(df["DigitalPayments"].mean(), 2))

print("\nAverage Inflation Rate:")
print(round(df["InflationRate"].mean(), 2))

print("\nAverage Money Supply:")
print(round(df["MoneySupply"].mean(), 2))

# Maximum Values
print("\nMaximum Currency Circulation:")
print(df["CurrencyInCirculation"].max())

print("\nMaximum Digital Payments:")
print(df["DigitalPayments"].max())

# Growth Rates
currency_growth = (
    (
        df["CurrencyInCirculation"].iloc[-1]
        - df["CurrencyInCirculation"].iloc[0]
    )
    /
    df["CurrencyInCirculation"].iloc[0]
) * 100

digital_growth = (
    (
        df["DigitalPayments"].iloc[-1]
        - df["DigitalPayments"].iloc[0]
    )
    /
    df["DigitalPayments"].iloc[0]
) * 100

money_growth = (
    (
        df["MoneySupply"].iloc[-1]
        - df["MoneySupply"].iloc[0]
    )
    /
    df["MoneySupply"].iloc[0]
) * 100

print("\nCurrency Growth Rate (%):")
print(round(currency_growth, 2))

print("\nDigital Payments Growth Rate (%):")
print(round(digital_growth, 2))

print("\nMoney Supply Growth Rate (%):")
print(round(money_growth, 2))

# Correlation Matrix
print("\nCorrelation Matrix:")
print(
    df[
        [
            "CurrencyInCirculation",
            "DigitalPayments",
            "InflationRate",
            "MoneySupply"
        ]
    ].corr()
)

print("\n========== ANALYSIS COMPLETED ==========\n")