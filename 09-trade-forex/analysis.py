# ==========================================
# Author : Saloni Tiwari
# Project : Trade & Forex Analytics
# File : analysis.py
# Description : Statistical Analysis
# ==========================================

import pandas as pd

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv(
    "data/trade_forex_data.csv"
)

print(
    "\n========== TRADE & FOREX ANALYSIS ==========\n"
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
# Export Analysis
# ------------------------------------------

print("\nAverage Exports:")

print(
    round(
        df["Exports"].mean(),
        2
    )
)

# ------------------------------------------
# Import Analysis
# ------------------------------------------

print("\nAverage Imports:")

print(
    round(
        df["Imports"].mean(),
        2
    )
)

# ------------------------------------------
# Trade Balance Analysis
# ------------------------------------------

print(
    "\nAverage Trade Balance:"
)

print(
    round(
        df["TradeBalance"].mean(),
        2
    )
)

# ------------------------------------------
# Exchange Rate Analysis
# ------------------------------------------

print(
    "\nAverage Exchange Rate:"
)

print(
    round(
        df["ExchangeRate"].mean(),
        2
    )
)

# ------------------------------------------
# Forex Reserves Analysis
# ------------------------------------------

print(
    "\nAverage Forex Reserves:"
)

print(
    round(
        df["ForexReserves"].mean(),
        2
    )
)

# ------------------------------------------
# Export Growth
# ------------------------------------------

export_growth = (
    (
        df["Exports"].iloc[-1]
        -
        df["Exports"].iloc[0]
    )
    /
    df["Exports"].iloc[0]
) * 100

print(
    "\nExport Growth Rate (%):"
)

print(
    round(
        export_growth,
        2
    )
)

# ------------------------------------------
# Import Growth
# ------------------------------------------

import_growth = (
    (
        df["Imports"].iloc[-1]
        -
        df["Imports"].iloc[0]
    )
    /
    df["Imports"].iloc[0]
) * 100

print(
    "\nImport Growth Rate (%):"
)

print(
    round(
        import_growth,
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
        "Exports",
        "Imports",
        "TradeBalance",
        "ExchangeRate",
        "ForexReserves",
        "GDP"
    ]
].corr()

print(corr)

# ------------------------------------------
# Best Export Year
# ------------------------------------------

best_year = df.loc[
    df["Exports"].idxmax(),
    "Year"
]

print(
    "\nHighest Export Year:"
)

print(
    best_year
)

print(
    "\n========== ANALYSIS COMPLETED ==========\n"
)