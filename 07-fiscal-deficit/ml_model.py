# ==========================================
# Author : Saloni Tiwari
# Project : Fiscal Deficit Analytics
# File : ml_model.py
# Description : Machine Learning Prediction
# ==========================================

import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

os.makedirs("charts", exist_ok=True)

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv(
    "data/fiscal_deficit_data.csv"
)

# ------------------------------------------
# Features & Target
# ------------------------------------------

X = df[
    [
        "GovernmentRevenue",
        "GovernmentExpenditure",
        "PublicDebt",
        "Borrowing",
        "GDP"
    ]
]

y = df["FiscalDeficit"]

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
# Model
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

predictions = model.predict(X_test)

score = r2_score(
    y_test,
    predictions
)

print("\n========== ML RESULTS ==========\n")

print(
    "R2 Score:",
    round(score,4)
)

# ------------------------------------------
# Future Prediction
# ------------------------------------------

future_data = pd.DataFrame(
    {
        "GovernmentRevenue":[2850,3100],
        "GovernmentExpenditure":[3200,3450],
        "PublicDebt":[9100,9500],
        "Borrowing":[260,230],
        "GDP":[21000,22500]
    }
)

future_prediction = model.predict(
    future_data
)

print(
    "\nPredicted Fiscal Deficit"
)

print(
    "2025:",
    round(
        future_prediction[0],
        2
    )
)

print(
    "2026:",
    round(
        future_prediction[1],
        2
    )
)

# ------------------------------------------
# Feature Importance
# ------------------------------------------

importance = pd.DataFrame(
    {
        "Feature":X.columns,
        "Importance":model.feature_importances_
    }
)

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

plt.figure(figsize=(8,5))

plt.bar(
    importance["Feature"],
    importance["Importance"]
)

plt.title(
    "Feature Importance"
)

plt.tight_layout()

plt.savefig(
    "charts/feature_importance.png"
)

plt.close()

# ------------------------------------------
# Actual vs Predicted
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.scatter(
    y_test,
    predictions
)

plt.plot(
    [y.min(),y.max()],
    [y.min(),y.max()]
)

plt.xlabel(
    "Actual Deficit"
)

plt.ylabel(
    "Predicted Deficit"
)

plt.title(
    "Actual vs Predicted Fiscal Deficit"
)

plt.tight_layout()

plt.savefig(
    "charts/ml_prediction.png"
)

plt.close()

print(
    "\nCharts Saved Successfully."
)

print(
    "\n========== MODEL COMPLETED ==========\n"
)