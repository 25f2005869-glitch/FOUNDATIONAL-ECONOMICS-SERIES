# ==========================================
# Author : Saloni Tiwari
# Project : Money & Currency Analytics
# File : ml_model.py
# Description : Machine Learning Prediction
# ==========================================

import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# ------------------------------------------
# Create Charts Folder
# ------------------------------------------

os.makedirs(
    "charts",
    exist_ok=True
)

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv(
    "data/money_currency_data.csv"
)

# ------------------------------------------
# Features & Target
# ------------------------------------------

X = df[
    [
        "DigitalPayments",
        "InflationRate",
        "MoneySupply"
    ]
]

y = df[
    "CurrencyInCirculation"
]

# ------------------------------------------
# Train Test Split
# ------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)

# ------------------------------------------
# Model Training
# ------------------------------------------

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

# ------------------------------------------
# Prediction
# ------------------------------------------

predictions = model.predict(
    X_test
)

score = r2_score(
    y_test,
    predictions
)

print("\n========== MACHINE LEARNING RESULTS ==========\n")

print(
    f"R2 Score : {round(score,4)}"
)

# ------------------------------------------
# Future Prediction
# ------------------------------------------

future_data = pd.DataFrame(
    {
        "DigitalPayments": [15000, 18000],
        "InflationRate": [5.0, 5.2],
        "MoneySupply": [230, 250]
    }
)

future_prediction = model.predict(
    future_data
)

print("\nPredicted Currency Circulation")

print(
    f"2025 : {round(future_prediction[0],2)}"
)

print(
    f"2026 : {round(future_prediction[1],2)}"
)

# ------------------------------------------
# Feature Importance Chart
# ------------------------------------------

importance = pd.DataFrame(
    {
        "Feature": X.columns,
        "Importance": model.feature_importances_
    }
)

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

plt.figure(
    figsize=(8,5)
)

plt.bar(
    importance["Feature"],
    importance["Importance"]
)

plt.title(
    "Feature Importance"
)

plt.xlabel(
    "Features"
)

plt.ylabel(
    "Importance"
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        "charts",
        "feature_importance.png"
    )
)

plt.close()

# ------------------------------------------
# Actual vs Predicted Chart
# ------------------------------------------

plt.figure(
    figsize=(8,5)
)

plt.scatter(
    y_test,
    predictions
)

plt.plot(
    [y.min(), y.max()],
    [y.min(), y.max()]
)

plt.title(
    "Actual vs Predicted Currency Circulation"
)

plt.xlabel(
    "Actual Values"
)

plt.ylabel(
    "Predicted Values"
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        "charts",
        "ml_prediction.png"
    )
)

plt.close()

print(
    "\nCharts Saved Successfully:"
)

print(
    "charts/feature_importance.png"
)

print(
    "charts/ml_prediction.png"
)

print(
    "\n========== MODEL COMPLETED ==========\n"
)