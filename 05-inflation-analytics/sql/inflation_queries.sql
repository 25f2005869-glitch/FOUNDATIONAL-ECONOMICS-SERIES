-- =========================================
-- Author : Saloni Tiwari
-- Project : Inflation Analytics
-- File : inflation_queries.sql
-- Description : SQL Analysis Queries
-- =========================================

-- View Complete Dataset

SELECT *
FROM inflation_data;

------------------------------------------------

-- Average Inflation Rate

SELECT
AVG(InflationRate) AS AvgInflation
FROM inflation_data;

------------------------------------------------

-- Average CPI

SELECT
AVG(CPI) AS AvgCPI
FROM inflation_data;

------------------------------------------------

-- Average WPI

SELECT
AVG(WPI) AS AvgWPI
FROM inflation_data;

------------------------------------------------

-- Highest Inflation Year

SELECT *
FROM inflation_data
ORDER BY InflationRate DESC
LIMIT 1;

------------------------------------------------

-- Lowest Inflation Year

SELECT *
FROM inflation_data
ORDER BY InflationRate ASC
LIMIT 1;

------------------------------------------------

-- Average Income

SELECT
AVG(AverageIncome) AS AvgIncome
FROM inflation_data;

------------------------------------------------

-- Purchasing Power Trend

SELECT
Year,
PurchasingPower
FROM inflation_data
ORDER BY Year;

------------------------------------------------

-- CPI Greater Than 150

SELECT
Year,
CPI
FROM inflation_data
WHERE CPI > 150;

------------------------------------------------

-- WPI Greater Than 150

SELECT
Year,
WPI
FROM inflation_data
WHERE WPI > 150;

------------------------------------------------

-- Inflation Above 6 Percent

SELECT *
FROM inflation_data
WHERE InflationRate > 6;

------------------------------------------------

-- Income Above 40000

SELECT *
FROM inflation_data
WHERE AverageIncome > 40000;

------------------------------------------------

-- Purchasing Power Below 90

SELECT *
FROM inflation_data
WHERE PurchasingPower < 90;

------------------------------------------------

-- Top 5 CPI Values

SELECT *
FROM inflation_data
ORDER BY CPI DESC
LIMIT 5;

------------------------------------------------

-- Top 5 WPI Values

SELECT *
FROM inflation_data
ORDER BY WPI DESC
LIMIT 5;

------------------------------------------------

-- Inflation Ranking

SELECT
Year,
InflationRate,
RANK() OVER (
ORDER BY InflationRate DESC
) AS InflationRank
FROM inflation_data;

------------------------------------------------

-- Income Ranking

SELECT
Year,
AverageIncome,
RANK() OVER (
ORDER BY AverageIncome DESC
) AS IncomeRank
FROM inflation_data;

------------------------------------------------

-- Inflation vs Income

SELECT
Year,
InflationRate,
AverageIncome
FROM inflation_data;

------------------------------------------------

-- CPI vs WPI Comparison

SELECT
Year,
CPI,
WPI
FROM inflation_data;

------------------------------------------------

-- Economic Summary

SELECT
AVG(CPI) AS AvgCPI,
AVG(WPI) AS AvgWPI,
AVG(InflationRate) AS AvgInflation,
AVG(AverageIncome) AS AvgIncome,
AVG(PurchasingPower) AS AvgPurchasingPower
FROM inflation_data;