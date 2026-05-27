# ==========================================
# Author : Saloni Tiwari
# Project : 01_Barter_System_Evolution
# File : analysis.py
# Description : Statistical Analysis
# ==========================================

import pandas as pd
import numpy as np

df = pd.read_csv("data/barter_system_data.csv")

print("\n========== DATASET ==========\n")
print(df)

print("\n========== SUMMARY STATISTICS ==========\n")
print(df.describe())

print("\n========== MEAN ==========\n")
print(df.mean(numeric_only=True))

print("\n========== MEDIAN ==========\n")
print(df.median(numeric_only=True))

print("\n========== STANDARD DEVIATION ==========\n")
print(df.std(numeric_only=True))

print("\n========== VARIANCE ==========\n")
print(df.var(numeric_only=True))

print("\n========== CORRELATION ==========\n")
print(df.corr(numeric_only=True))

print("\n========== HIGHEST TRADE VOLUME ==========\n")
print(df.loc[df["Trade_Volume"].idxmax()])

print("\n========== HIGHEST EFFICIENCY ==========\n")
print(df.loc[df["Efficiency_Index"].idxmax()])

print("\n========== DIGITAL ECONOMY DATA ==========\n")
print(df[df["Trade_System"] == "Digital"])

print("\n========== ANALYSIS COMPLETED ==========\n")