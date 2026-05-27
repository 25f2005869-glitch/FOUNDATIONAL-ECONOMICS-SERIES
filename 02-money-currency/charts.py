# ==========================================
# Author : Saloni Tiwari
# Project : Money & Currency Analytics
# File : charts.py
# Description : Data Visualizations
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("data/money_currency_data.csv")

# ------------------------------------------
# 1 Currency Circulation
# ------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    df["Year"],
    df["CurrencyInCirculation"],
    marker="o"
)

plt.title("Currency Circulation Over Time")
plt.xlabel("Year")
plt.ylabel("Currency In Circulation")

plt.grid(True)

plt.savefig(
    "charts/currency_circulation.png"
)

plt.close()

# ------------------------------------------
# 2 Digital Payments Growth
# ------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    df["Year"],
    df["DigitalPayments"]
)

plt.title("Digital Payments Growth")
plt.xlabel("Year")
plt.ylabel("Transactions")

plt.savefig(
    "charts/digital_payments_growth.png"
)

plt.close()

# ------------------------------------------
# 3 Inflation vs Money Supply
# ------------------------------------------

fig, ax1 = plt.subplots(figsize=(8, 5))

ax1.plot(
    df["Year"],
    df["InflationRate"],
    marker="o"
)

ax1.set_ylabel("Inflation Rate")

ax2 = ax1.twinx()

ax2.plot(
    df["Year"],
    df["MoneySupply"],
    marker="s"
)

ax2.set_ylabel("Money Supply")

plt.title("Inflation vs Money Supply")

plt.savefig(
    "charts/inflation_vs_money_supply.png"
)

plt.close()

# ------------------------------------------
# 4 Money Supply Analysis
# ------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    df["Year"],
    df["MoneySupply"],
    marker="o"
)

plt.title("Money Supply Analysis")
plt.xlabel("Year")
plt.ylabel("Money Supply")

plt.grid(True)

plt.savefig(
    "charts/money_supply_analysis.png"
)

plt.close()

# ------------------------------------------
# 5 Evolution of Money
# ------------------------------------------

stages = [
    "Barter",
    "Commodity",
    "Coins",
    "Paper",
    "Banking",
    "Digital",
    "CBDC"
]

plt.figure(figsize=(10, 2))

plt.plot(
    range(len(stages)),
    [1] * len(stages),
    marker="o"
)

plt.yticks([])

plt.xticks(
    range(len(stages)),
    stages
)

plt.title("Evolution of Money")

plt.savefig(
    "charts/evolution_of_money.png"
)

plt.close()

# ------------------------------------------
# 6 Correlation Matrix
# ------------------------------------------

plt.figure(figsize=(6, 5))

sns.heatmap(
    df[
        [
            "CurrencyInCirculation",
            "DigitalPayments",
            "InflationRate",
            "MoneySupply"
        ]
    ].corr(),
    annot=True
)

plt.title("Correlation Matrix")

plt.savefig(
    "charts/correlation_matrix.png"
)

plt.close()

# ------------------------------------------
# 7 Currency Growth Rate
# ------------------------------------------

growth = (
    df["CurrencyInCirculation"]
    .pct_change()
    * 100
)

plt.figure(figsize=(8, 5))

plt.bar(
    df["Year"][1:],
    growth[1:]
)

plt.title("Currency Growth Rate (%)")
plt.xlabel("Year")
plt.ylabel("Growth %")

plt.savefig(
    "charts/currency_growth_rate.png"
)

plt.close()

print(
    "All charts generated successfully."
)