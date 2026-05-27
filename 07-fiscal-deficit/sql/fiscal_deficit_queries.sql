-- =========================================
-- Author : Saloni Tiwari
-- Project : Fiscal Deficit Analytics
-- File : fiscal_deficit_queries.sql
-- Description : SQL Analysis Queries
-- =========================================

-- View Complete Dataset

SELECT *
FROM fiscal_deficit_data;

------------------------------------------------

-- Average Fiscal Deficit

SELECT
AVG(FiscalDeficit) AS AvgFiscalDeficit
FROM fiscal_deficit_data;

------------------------------------------------

-- Average Government Revenue

SELECT
AVG(GovernmentRevenue) AS AvgRevenue
FROM fiscal_deficit_data;

------------------------------------------------

-- Average Government Expenditure

SELECT
AVG(GovernmentExpenditure) AS AvgExpenditure
FROM fiscal_deficit_data;

------------------------------------------------

-- Average Public Debt

SELECT
AVG(PublicDebt) AS AvgDebt
FROM fiscal_deficit_data;

------------------------------------------------

-- Average Borrowing

SELECT
AVG(Borrowing) AS AvgBorrowing
FROM fiscal_deficit_data;

------------------------------------------------

-- Average GDP

SELECT
AVG(GDP) AS AvgGDP
FROM fiscal_deficit_data;

------------------------------------------------

-- Highest Fiscal Deficit Year

SELECT *
FROM fiscal_deficit_data
ORDER BY FiscalDeficit DESC
LIMIT 1;

------------------------------------------------

-- Lowest Fiscal Deficit Year

SELECT *
FROM fiscal_deficit_data
ORDER BY FiscalDeficit ASC
LIMIT 1;

------------------------------------------------

-- Highest Public Debt Year

SELECT *
FROM fiscal_deficit_data
ORDER BY PublicDebt DESC
LIMIT 1;

------------------------------------------------

-- Highest Borrowing Year

SELECT *
FROM fiscal_deficit_data
ORDER BY Borrowing DESC
LIMIT 1;

------------------------------------------------

-- Revenue Less Than Expenditure

SELECT
Year,
GovernmentRevenue,
GovernmentExpenditure,
FiscalDeficit
FROM fiscal_deficit_data
WHERE GovernmentRevenue <
GovernmentExpenditure;

------------------------------------------------

-- Fiscal Deficit Greater Than 300

SELECT *
FROM fiscal_deficit_data
WHERE FiscalDeficit > 300;

------------------------------------------------

-- Public Debt Greater Than 7000

SELECT *
FROM fiscal_deficit_data
WHERE PublicDebt > 7000;

------------------------------------------------

-- Borrowing Greater Than 300

SELECT *
FROM fiscal_deficit_data
WHERE Borrowing > 300;

------------------------------------------------

-- GDP Greater Than 15000

SELECT *
FROM fiscal_deficit_data
WHERE GDP > 15000;

------------------------------------------------

-- Fiscal Deficit vs GDP

SELECT
Year,
FiscalDeficit,
GDP
FROM fiscal_deficit_data;

------------------------------------------------

-- Revenue vs Expenditure

SELECT
Year,
GovernmentRevenue,
GovernmentExpenditure
FROM fiscal_deficit_data;

------------------------------------------------

-- Debt Growth Analysis

SELECT
Year,
PublicDebt
FROM fiscal_deficit_data
ORDER BY Year;

------------------------------------------------

-- Borrowing Trend Analysis

SELECT
Year,
Borrowing
FROM fiscal_deficit_data
ORDER BY Year;

------------------------------------------------

-- Fiscal Deficit Ranking

SELECT
Year,
FiscalDeficit,
RANK() OVER(
ORDER BY FiscalDeficit DESC
) AS DeficitRank
FROM fiscal_deficit_data;

------------------------------------------------

-- Public Debt Ranking

SELECT
Year,
PublicDebt,
RANK() OVER(
ORDER BY PublicDebt DESC
) AS DebtRank
FROM fiscal_deficit_data;

------------------------------------------------

-- GDP Ranking

SELECT
Year,
GDP,
RANK() OVER(
ORDER BY GDP DESC
) AS GDPRank
FROM fiscal_deficit_data;

------------------------------------------------

-- Economic Summary Report

SELECT
AVG(GovernmentRevenue) AS AvgRevenue,
AVG(GovernmentExpenditure) AS AvgExpenditure,
AVG(FiscalDeficit) AS AvgDeficit,
AVG(PublicDebt) AS AvgDebt,
AVG(Borrowing) AS AvgBorrowing,
AVG(GDP) AS AvgGDP
FROM fiscal_deficit_data;

------------------------------------------------

-- Deficit to GDP Ratio

SELECT
Year,
ROUND(
(FiscalDeficit * 100.0) / GDP,
2
) AS DeficitToGDPRatio
FROM fiscal_deficit_data;

------------------------------------------------

-- Debt to GDP Ratio

SELECT
Year,
ROUND(
(PublicDebt * 100.0) / GDP,
2
) AS DebtToGDPRatio
FROM fiscal_deficit_data;

------------------------------------------------

-- Revenue Efficiency Ratio

SELECT
Year,
ROUND(
(GovernmentRevenue * 100.0)
/ GovernmentExpenditure,
2
) AS RevenueEfficiency
FROM fiscal_deficit_data;

------------------------------------------------

-- Top 5 Highest Debt Years

SELECT *
FROM fiscal_deficit_data
ORDER BY PublicDebt DESC
LIMIT 5;

------------------------------------------------

-- Top 5 Highest Fiscal Deficit Years

SELECT *
FROM fiscal_deficit_data
ORDER BY FiscalDeficit DESC
LIMIT 5;

------------------------------------------------

-- Final Fiscal Dashboard Summary

SELECT
MAX(FiscalDeficit) AS HighestDeficit,
MIN(FiscalDeficit) AS LowestDeficit,
MAX(PublicDebt) AS HighestDebt,
MAX(Borrowing) AS HighestBorrowing,
MAX(GDP) AS HighestGDP
FROM fiscal_deficit_data;