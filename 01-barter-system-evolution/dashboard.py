# ==========================================
# Author : Saloni Tiwari
# Project : 01_Barter_System_Evolution
# File : dashboard.py
# Description : Charts & Visualization
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")

df = pd.read_csv("data/barter_system_data.csv")

# ------------------------------------------------
# Trade Efficiency Growth
# ------------------------------------------------

plt.figure(figsize=(10,6))
plt.plot(
    df["Year"],
    df["Efficiency_Index"],
    color="green",
    marker="o",
    linewidth=3
)

plt.title("Trade Efficiency Growth")
plt.xlabel("Year")
plt.ylabel("Efficiency Index")
plt.grid(True)
plt.savefig("charts/trade_efficiency_growth.png")
plt.close()

# ------------------------------------------------
# Barter vs Money
# ------------------------------------------------

plt.figure(figsize=(10,6))

colors = [
    "brown",
    "orange",
    "gold",
    "green",
    "blue",
    "purple",
    "red",
    "cyan",
    "magenta",
    "teal",
    "navy"
]

plt.bar(
    df["Trade_System"],
    df["Trade_Volume"],
    color=colors[:len(df)]
)

plt.title("Barter vs Money Systems")
plt.xticks(rotation=45)
plt.savefig("charts/barter_vs_money.png")
plt.close()

# ------------------------------------------------
# Transaction Success Rate
# ------------------------------------------------

plt.figure(figsize=(10,6))

plt.plot(
    df["Year"],
    df["Transaction_Success_Rate"],
    color="purple",
    marker="o",
    linewidth=3
)

plt.title("Transaction Success Rate")
plt.xlabel("Year")
plt.ylabel("Success Rate")
plt.grid(True)

plt.savefig("charts/transaction_success_rate.png")
plt.close()

# ------------------------------------------------
# Trade Volume Growth
# ------------------------------------------------

plt.figure(figsize=(10,6))

plt.plot(
    df["Year"],
    df["Trade_Volume"],
    color="darkgreen",
    marker="s",
    linewidth=3
)

plt.title("Trade Volume Growth")
plt.xlabel("Year")
plt.ylabel("Trade Volume")

plt.grid(True)

plt.savefig("charts/trade_volume_growth.png")
plt.close()

# ------------------------------------------------
# Market Complexity
# ------------------------------------------------

plt.figure(figsize=(10,6))

plt.plot(
    df["Year"],
    df["Market_Complexity"],
    color="red",
    marker="D",
    linewidth=3
)

plt.title("Market Complexity")
plt.xlabel("Year")
plt.ylabel("Complexity")

plt.grid(True)

plt.savefig("charts/market_complexity.png")
plt.close()

# ------------------------------------------------
# Exchange Evolution
# ------------------------------------------------

plt.figure(figsize=(10,6))

plt.bar(
    df["Year"],
    df["Efficiency_Index"],
    color="orange"
)

plt.title("Exchange Evolution")
plt.xlabel("Year")
plt.ylabel("Efficiency")

plt.savefig("charts/exchange_evolution.png")
plt.close()

# ------------------------------------------------
# Economic Efficiency
# ------------------------------------------------

plt.figure(figsize=(10,6))

plt.bar(
    df["Year"],
    df["Efficiency_Index"],
    color="teal"
)

plt.title("Economic Efficiency")
plt.xlabel("Year")
plt.ylabel("Efficiency")

plt.savefig("charts/economic_efficiency.png")
plt.close()

# ------------------------------------------------
# Population vs Trade
# ------------------------------------------------

plt.figure(figsize=(10,6))

plt.scatter(
    df["Population_Million"],
    df["Trade_Volume"],
    color="purple",
    s=150
)

plt.title("Population vs Trade Volume")
plt.xlabel("Population (Million)")
plt.ylabel("Trade Volume")

plt.grid(True)

plt.savefig("charts/population_vs_trade.png")
plt.close()

# ------------------------------------------------
# Statistical Variance
# ------------------------------------------------

variance_data = [
    df["Trade_Volume"].var(),
    df["Efficiency_Index"].var(),
    df["Market_Complexity"].var()
]

labels = [
    "Trade Volume",
    "Efficiency",
    "Complexity"
]

plt.figure(figsize=(10,6))

plt.bar(
    labels,
    variance_data,
    color=["red","blue","green"]
)

plt.title("Statistical Variance Analysis")

plt.savefig("charts/statistical_variance.png")
plt.close()

print("\n========== DASHBOARD COMPLETED ==========\n")
print("All charts saved successfully in charts folder.")