# ==========================================
# Author : Saloni Tiwari
# Project : GDP & Development Analytics
# File : analysis.py
# Description : Statistical Analysis
# ==========================================

import pandas as pd

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv(
    "data/gdp_development_data.csv"
)

print(
    "\n========== GDP & DEVELOPMENT ANALYSIS ==========\n"
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
# GDP Analysis
# ------------------------------------------

print("\nAverage GDP:")

print(
    round(
        df["GDP"].mean(),
        2
    )
)

# ------------------------------------------
# Per Capita Income
# ------------------------------------------

print(
    "\nAverage Per Capita Income:"
)

print(
    round(
        df["PerCapitaIncome"].mean(),
        2
    )
)

# ------------------------------------------
# HDI Analysis
# ------------------------------------------

print(
    "\nAverage HDI:"
)

print(
    round(
        df["HDI"].mean(),
        3
    )
)

# ------------------------------------------
# GDP Growth
# ------------------------------------------

gdp_growth = (
    (
        df["GDP"].iloc[-1]
        -
        df["GDP"].iloc[0]
    )
    /
    df["GDP"].iloc[0]
) * 100

print(
    "\nGDP Growth Rate (%):"
)

print(
    round(
        gdp_growth,
        2
    )
)

# ------------------------------------------
# Income Growth
# ------------------------------------------

income_growth = (
    (
        df["PerCapitaIncome"].iloc[-1]
        -
        df["PerCapitaIncome"].iloc[0]
    )
    /
    df["PerCapitaIncome"].iloc[0]
) * 100

print(
    "\nPer Capita Income Growth (%):"
)

print(
    round(
        income_growth,
        2
    )
)

# ------------------------------------------
# Sector Analysis
# ------------------------------------------

print(
    "\n========== SECTOR ANALYSIS ==========\n"
)

print(
    "Average Agriculture Contribution:"
)

print(
    round(
        df["Agriculture"].mean(),
        2
    )
)

print(
    "\nAverage Industry Contribution:"
)

print(
    round(
        df["Industry"].mean(),
        2
    )
)

print(
    "\nAverage Services Contribution:"
)

print(
    round(
        df["Services"].mean(),
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
        "GDP",
        "PerCapitaIncome",
        "Agriculture",
        "Industry",
        "Services",
        "HDI",
        "GrowthRate"
    ]
].corr()

print(corr)

# ------------------------------------------
# Best GDP Year
# ------------------------------------------

best_year = df.loc[
    df["GDP"].idxmax(),
    "Year"
]

print(
    "\nHighest GDP Year:"
)

print(
    best_year
)

print(
    "\n========== ANALYSIS COMPLETED ==========\n"
)