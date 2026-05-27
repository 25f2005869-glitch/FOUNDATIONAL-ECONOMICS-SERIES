-- =========================================
-- Author : Saloni Tiwari
-- Project : RBI & Monetary Policy Analytics
-- File : rbi_monetary_policy_queries.sql
-- Description : SQL Analysis Queries
-- =========================================

-- View Complete Dataset

SELECT *
FROM rbi_monetary_policy_data;

------------------------------------------------

-- Average Repo Rate

SELECT
AVG(RepoRate) AS AvgRepoRate
FROM rbi_monetary_policy_data;

------------------------------------------------

-- Average Reverse Repo Rate

SELECT
AVG(ReverseRepoRate) AS AvgReverseRepoRate
FROM rbi_monetary_policy_data;

------------------------------------------------

-- Average CRR

SELECT
AVG(CRR) AS AvgCRR
FROM rbi_monetary_policy_data;

------------------------------------------------

-- Average SLR

SELECT
AVG(SLR) AS AvgSLR
FROM rbi_monetary_policy_data;

------------------------------------------------

-- Average Inflation Rate

SELECT
AVG(InflationRate) AS AvgInflation
FROM rbi_monetary_policy_data;

------------------------------------------------

-- Average Money Supply

SELECT
AVG(MoneySupply) AS AvgMoneySupply
FROM rbi_monetary_policy_data;

------------------------------------------------

-- Highest Repo Rate Year

SELECT *
FROM rbi_monetary_policy_data
ORDER BY RepoRate DESC
LIMIT 1;

------------------------------------------------

-- Lowest Repo Rate Year

SELECT *
FROM rbi_monetary_policy_data
ORDER BY RepoRate ASC
LIMIT 1;

------------------------------------------------

-- Highest Inflation Year

SELECT *
FROM rbi_monetary_policy_data
ORDER BY InflationRate DESC
LIMIT 1;

------------------------------------------------

-- Highest Money Supply Year

SELECT *
FROM rbi_monetary_policy_data
ORDER BY MoneySupply DESC
LIMIT 1;

------------------------------------------------

-- Repo Rate Above 6%

SELECT *
FROM rbi_monetary_policy_data
WHERE RepoRate > 6;

------------------------------------------------

-- Inflation Above 6%

SELECT *
FROM rbi_monetary_policy_data
WHERE InflationRate > 6;

------------------------------------------------

-- Money Supply Above 200

SELECT *
FROM rbi_monetary_policy_data
WHERE MoneySupply > 200;

------------------------------------------------

-- Repo Rate vs Inflation

SELECT
Year,
RepoRate,
InflationRate
FROM rbi_monetary_policy_data;

------------------------------------------------

-- Reverse Repo Trend

SELECT
Year,
ReverseRepoRate
FROM rbi_monetary_policy_data
ORDER BY Year;

------------------------------------------------

-- CRR vs SLR

SELECT
Year,
CRR,
SLR
FROM rbi_monetary_policy_data;

------------------------------------------------

-- Repo Rate Ranking

SELECT
Year,
RepoRate,
RANK() OVER(
ORDER BY RepoRate DESC
) AS RepoRank
FROM rbi_monetary_policy_data;

------------------------------------------------

-- Inflation Ranking

SELECT
Year,
InflationRate,
RANK() OVER(
ORDER BY InflationRate DESC
) AS InflationRank
FROM rbi_monetary_policy_data;

------------------------------------------------

-- Money Supply Ranking

SELECT
Year,
MoneySupply,
RANK() OVER(
ORDER BY MoneySupply DESC
) AS MoneySupplyRank
FROM rbi_monetary_policy_data;

------------------------------------------------

-- Monetary Policy Summary

SELECT
AVG(RepoRate) AS AvgRepoRate,
AVG(ReverseRepoRate) AS AvgReverseRepoRate,
AVG(CRR) AS AvgCRR,
AVG(SLR) AS AvgSLR,
AVG(InflationRate) AS AvgInflation,
AVG(MoneySupply) AS AvgMoneySupply
FROM rbi_monetary_policy_data;

------------------------------------------------

-- Inflation Control Analysis

SELECT
Year,
RepoRate,
InflationRate,
MoneySupply
FROM rbi_monetary_policy_data;

------------------------------------------------

-- Money Supply Growth

SELECT
Year,
MoneySupply
FROM rbi_monetary_policy_data
ORDER BY Year;

------------------------------------------------

-- CRR Changes

SELECT
Year,
CRR
FROM rbi_monetary_policy_data;

------------------------------------------------

-- SLR Changes

SELECT
Year,
SLR
FROM rbi_monetary_policy_data;

------------------------------------------------

-- Monetary Dashboard Summary

SELECT
MAX(RepoRate) AS HighestRepoRate,
MIN(RepoRate) AS LowestRepoRate,
MAX(InflationRate) AS HighestInflation,
MAX(MoneySupply) AS HighestMoneySupply
FROM rbi_monetary_policy_data;