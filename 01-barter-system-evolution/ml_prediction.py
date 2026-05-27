# ==========================================
# Author : Saloni Tiwari
# Project : 01_Barter_System_Evolution
# File : ml_prediction.py
# Description : Machine Learning Prediction
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

df = pd.read_csv("data/barter_system_data.csv")

X = df[["Year"]]
y = df["Efficiency_Index"]

model = LinearRegression()
model.fit(X, y)

future_years = pd.DataFrame({
    "Year":[2030,2040,2050]
})

predictions = model.predict(future_years)

print("\n========== FUTURE PREDICTIONS ==========\n")

for year, value in zip(
        future_years["Year"],
        predictions):

    print(
        f"{year} : {value:.2f}"
    )

plt.figure(figsize=(8,5))

plt.scatter(
    df["Year"],
    y,
    label="Historical Data"
)

plt.plot(
    future_years["Year"],
    predictions,
    marker="o",
    label="Prediction"
)

plt.title("Future Trade Efficiency Prediction")
plt.xlabel("Year")
plt.ylabel("Efficiency Index")
plt.legend()

plt.savefig(
    "charts/ml_trade_prediction.png"
)

plt.close()

print("\nML chart saved successfully.")