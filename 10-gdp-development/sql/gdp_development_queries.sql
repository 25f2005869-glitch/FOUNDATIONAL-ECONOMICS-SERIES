-- =========================================
-- Author : Saloni Tiwari
-- Project : GDP & Development Analytics
-- File : gdp_development_queries.sql
-- Description : SQL Analysis Queries
-- =========================================

-- View Complete Dataset

SELECT *
FROM gdp_development_data;

------------------------------------------------

-- Average GDP

SELECT
AVG(GDP) AS AvgGDP
FROM gdp_development_data;

------------------------------------------------

-- Average Per Capita Income

SELECT
AVG(PerCapitaIncome) AS AvgIncome
FROM gdp_development_data;

------------------------------------------------

-- Average HDI

SELECT
AVG(HDI) AS AvgHDI
FROM gdp_development_data;

------------------------------------------------

-- Average Growth Rate

SELECT
AVG(GrowthRate) AS AvgGrowthRate
FROM gdp_development_data;

------------------------------------------------

-- Highest GDP Year

SELECT *
FROM gdp_development_data
ORDER BY GDP DESC
LIMIT 1;

------------------------------------------------

-- Highest Income Year

SELECT *
FROM gdp_development_data
ORDER BY PerCapitaIncome DESC
LIMIT 1;

------------------------------------------------

-- Highest HDI Year

SELECT *
FROM gdp_development_data
ORDER BY HDI DESC
LIMIT 1;

------------------------------------------------

-- Highest Growth Rate Year

SELECT *
FROM gdp_development_data
ORDER BY GrowthRate DESC
LIMIT 1;

------------------------------------------------

-- GDP Above 15000

SELECT *
FROM gdp_development_data
WHERE GDP > 15000;

------------------------------------------------

-- Income Above 100000

SELECT *
FROM gdp_development_data
WHERE PerCapitaIncome > 100000;

------------------------------------------------

-- HDI Above 0.68

SELECT *
FROM gdp_development_data
WHERE HDI > 0.68;

------------------------------------------------

-- GDP Trend

SELECT
Year,
GDP
FROM gdp_development_data
ORDER BY Year;

------------------------------------------------

-- Income Trend

SELECT
Year,
PerCapitaIncome
FROM gdp_development_data
ORDER BY Year;

------------------------------------------------

-- HDI Trend

SELECT
Year,
HDI
FROM gdp_development_data
ORDER BY Year;

------------------------------------------------

-- Sector Contribution

SELECT
Year,
Agriculture,
Industry,
Services
FROM gdp_development_data;

------------------------------------------------

-- GDP Ranking

SELECT
Year,
GDP,
RANK() OVER(
ORDER BY GDP DESC
) AS GDPRank
FROM gdp_development_data;

------------------------------------------------

-- Income Ranking

SELECT
Year,
PerCapitaIncome,
RANK() OVER(
ORDER BY PerCapitaIncome DESC
) AS IncomeRank
FROM gdp_development_data;

------------------------------------------------

-- HDI Ranking

SELECT
Year,
HDI,
RANK() OVER(
ORDER BY HDI DESC
) AS HDIRank
FROM gdp_development_data;

------------------------------------------------

-- Growth Rate Ranking

SELECT
Year,
GrowthRate,
RANK() OVER(
ORDER BY GrowthRate DESC
) AS GrowthRank
FROM gdp_development_data;

------------------------------------------------

-- Agriculture Share Trend

SELECT
Year,
Agriculture
FROM gdp_development_data
ORDER BY Year;

------------------------------------------------

-- Industry Share Trend

SELECT
Year,
Industry
FROM gdp_development_data
ORDER BY Year;

------------------------------------------------

-- Services Share Trend

SELECT
Year,
Services
FROM gdp_development_data
ORDER BY Year;

------------------------------------------------

-- Economic Summary Report

SELECT
AVG(GDP) AS AvgGDP,
AVG(PerCapitaIncome) AS AvgIncome,
AVG(HDI) AS AvgHDI,
AVG(GrowthRate) AS AvgGrowthRate,
AVG(Agriculture) AS AvgAgriculture,
AVG(Industry) AS AvgIndustry,
AVG(Services) AS AvgServices
FROM gdp_development_data;

------------------------------------------------

-- Development Dashboard Summary

SELECT
MAX(GDP) AS HighestGDP,
MAX(PerCapitaIncome) AS HighestIncome,
MAX(HDI) AS HighestHDI,
MAX(GrowthRate) AS HighestGrowthRate
FROM gdp_development_data;