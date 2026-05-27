-- =========================================
-- Author : Saloni Tiwari
-- Project : Trade & Forex Analytics
-- File : trade_forex_queries.sql
-- Description : SQL Analysis Queries
-- =========================================

-- View Complete Dataset

SELECT *
FROM trade_forex_data;

------------------------------------------------

-- Average Exports

SELECT
AVG(Exports) AS AvgExports
FROM trade_forex_data;

------------------------------------------------

-- Average Imports

SELECT
AVG(Imports) AS AvgImports
FROM trade_forex_data;

------------------------------------------------

-- Average Trade Balance

SELECT
AVG(TradeBalance) AS AvgTradeBalance
FROM trade_forex_data;

------------------------------------------------

-- Average Exchange Rate

SELECT
AVG(ExchangeRate) AS AvgExchangeRate
FROM trade_forex_data;

------------------------------------------------

-- Average Forex Reserves

SELECT
AVG(ForexReserves) AS AvgForexReserves
FROM trade_forex_data;

------------------------------------------------

-- Average GDP

SELECT
AVG(GDP) AS AvgGDP
FROM trade_forex_data;

------------------------------------------------

-- Highest Export Year

SELECT *
FROM trade_forex_data
ORDER BY Exports DESC
LIMIT 1;

------------------------------------------------

-- Highest Import Year

SELECT *
FROM trade_forex_data
ORDER BY Imports DESC
LIMIT 1;

------------------------------------------------

-- Largest Trade Deficit Year

SELECT *
FROM trade_forex_data
ORDER BY TradeBalance ASC
LIMIT 1;

------------------------------------------------

-- Highest Forex Reserve Year

SELECT *
FROM trade_forex_data
ORDER BY ForexReserves DESC
LIMIT 1;

------------------------------------------------

-- Exchange Rate Above 75

SELECT *
FROM trade_forex_data
WHERE ExchangeRate > 75;

------------------------------------------------

-- Exports Above 400

SELECT *
FROM trade_forex_data
WHERE Exports > 400;

------------------------------------------------

-- Imports Above 700

SELECT *
FROM trade_forex_data
WHERE Imports > 700;

------------------------------------------------

-- Trade Balance Analysis

SELECT
Year,
Exports,
Imports,
TradeBalance
FROM trade_forex_data;

------------------------------------------------

-- Exchange Rate Trend

SELECT
Year,
ExchangeRate
FROM trade_forex_data
ORDER BY Year;

------------------------------------------------

-- Forex Reserve Trend

SELECT
Year,
ForexReserves
FROM trade_forex_data
ORDER BY Year;

------------------------------------------------

-- Export Ranking

SELECT
Year,
Exports,
RANK() OVER(
ORDER BY Exports DESC
) AS ExportRank
FROM trade_forex_data;

------------------------------------------------

-- Import Ranking

SELECT
Year,
Imports,
RANK() OVER(
ORDER BY Imports DESC
) AS ImportRank
FROM trade_forex_data;

------------------------------------------------

-- Forex Reserve Ranking

SELECT
Year,
ForexReserves,
RANK() OVER(
ORDER BY ForexReserves DESC
) AS ForexRank
FROM trade_forex_data;

------------------------------------------------

-- Exchange Rate Ranking

SELECT
Year,
ExchangeRate,
RANK() OVER(
ORDER BY ExchangeRate DESC
) AS ExchangeRateRank
FROM trade_forex_data;

------------------------------------------------

-- Export to Import Ratio

SELECT
Year,
ROUND(
(Exports * 100.0) / Imports,
2
) AS ExportImportRatio
FROM trade_forex_data;

------------------------------------------------

-- Trade Deficit to GDP Ratio

SELECT
Year,
ROUND(
(ABS(TradeBalance) * 100.0) / GDP,
2
) AS TradeDeficitToGDPRatio
FROM trade_forex_data;

------------------------------------------------

-- Economic Summary Report

SELECT
AVG(Exports) AS AvgExports,
AVG(Imports) AS AvgImports,
AVG(TradeBalance) AS AvgTradeBalance,
AVG(ExchangeRate) AS AvgExchangeRate,
AVG(ForexReserves) AS AvgForexReserves,
AVG(GDP) AS AvgGDP
FROM trade_forex_data;

------------------------------------------------

-- Dashboard Summary

SELECT
MAX(Exports) AS HighestExports,
MAX(Imports) AS HighestImports,
MIN(TradeBalance) AS LargestTradeDeficit,
MAX(ForexReserves) AS HighestForexReserve,
MAX(ExchangeRate) AS HighestExchangeRate
FROM trade_forex_data;