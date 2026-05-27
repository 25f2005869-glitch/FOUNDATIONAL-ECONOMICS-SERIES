-- Total Trade Volume

SELECT SUM(Trade_Volume)
FROM barter_system_data;

--------------------------------------------------

-- Average Efficiency

SELECT AVG(Efficiency_Index)
FROM barter_system_data;

--------------------------------------------------

-- Trade Systems

SELECT DISTINCT Trade_System
FROM barter_system_data;

--------------------------------------------------

-- Highest Success Rate

SELECT *
FROM barter_system_data
ORDER BY Transaction_Success_Rate DESC
LIMIT 1;

--------------------------------------------------

-- Average Trade Volume By System

SELECT
Trade_System,
AVG(Trade_Volume)
FROM barter_system_data
GROUP BY Trade_System;

--------------------------------------------------

-- Efficiency Above 70

SELECT *
FROM barter_system_data
WHERE Efficiency_Index > 70;

--------------------------------------------------

-- Population Vs Trade

SELECT
Population_Million,
Trade_Volume
FROM barter_system_data;

--------------------------------------------------

-- Top 5 Trade Volumes

SELECT *
FROM barter_system_data
ORDER BY Trade_Volume DESC
LIMIT 5;