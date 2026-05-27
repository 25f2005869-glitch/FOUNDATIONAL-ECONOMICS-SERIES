-- =========================================
-- Author : Saloni Tiwari
-- Project : Budget & Taxation Analytics
-- File : budget_taxation_queries.sql
-- Description : SQL Analysis Queries
-- =========================================

-- View Complete Dataset

SELECT *
FROM budget_taxation_data;

------------------------------------------------

-- Average Government Revenue

SELECT
AVG(GovernmentRevenue) AS AvgRevenue
FROM budget_taxation_data;

------------------------------------------------

-- Average Government Expenditure

SELECT
AVG(GovernmentExpenditure) AS AvgExpenditure
FROM budget_taxation_data;

------------------------------------------------

-- Average Direct Tax

SELECT
AVG(DirectTax) AS AvgDirectTax
FROM budget_taxation_data;

------------------------------------------------

-- Average Indirect Tax

SELECT
AVG(IndirectTax) AS AvgIndirectTax
FROM budget_taxation_data;

------------------------------------------------

-- Average Fiscal Balance

SELECT
AVG(FiscalBalance) AS AvgFiscalBalance
FROM budget_taxation_data;

------------------------------------------------

-- Highest Revenue Year

SELECT *
FROM budget_taxation_data
ORDER BY GovernmentRevenue DESC
LIMIT 1;

------------------------------------------------

-- Highest Expenditure Year

SELECT *
FROM budget_taxation_data
ORDER BY GovernmentExpenditure DESC
LIMIT 1;

------------------------------------------------

-- Fiscal Deficit Years

SELECT *
FROM budget_taxation_data
WHERE FiscalBalance < 0;

------------------------------------------------

-- Direct Tax Greater Than 800

SELECT
Year,
DirectTax
FROM budget_taxation_data
WHERE DirectTax > 800;

------------------------------------------------

-- Indirect Tax Greater Than 1000

SELECT
Year,
IndirectTax
FROM budget_taxation_data
WHERE IndirectTax > 1000;

------------------------------------------------

-- GDP Above 15000

SELECT *
FROM budget_taxation_data
WHERE GDP > 15000;

------------------------------------------------

-- Revenue vs Expenditure

SELECT
Year,
GovernmentRevenue,
GovernmentExpenditure
FROM budget_taxation_data;

------------------------------------------------

-- Tax Collection Summary

SELECT
Year,
DirectTax,
IndirectTax,
(DirectTax + IndirectTax) AS TotalTax
FROM budget_taxation_data;

------------------------------------------------

-- Revenue Ranking

SELECT
Year,
GovernmentRevenue,
RANK() OVER (
ORDER BY GovernmentRevenue DESC
) AS RevenueRank
FROM budget_taxation_data;

------------------------------------------------

-- Expenditure Ranking

SELECT
Year,
GovernmentExpenditure,
RANK() OVER (
ORDER BY GovernmentExpenditure DESC
) AS ExpenditureRank
FROM budget_taxation_data;

------------------------------------------------

-- Fiscal Balance Ranking

SELECT
Year,
FiscalBalance,
RANK() OVER (
ORDER BY FiscalBalance DESC
) AS FiscalRank
FROM budget_taxation_data;

------------------------------------------------

-- Economic Summary

SELECT
AVG(GovernmentRevenue) AS AvgRevenue,
AVG(GovernmentExpenditure) AS AvgExpenditure,
AVG(DirectTax) AS AvgDirectTax,
AVG(IndirectTax) AS AvgIndirectTax,
AVG(FiscalBalance) AS AvgFiscalBalance,
AVG(GDP) AS AvgGDP
FROM budget_taxation_data;