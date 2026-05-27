-- ==========================================
-- Author : Saloni Tiwari
-- Project : Banking Fundamentals Analytics
-- File : banking_queries.sql
-- ==========================================

-- View Entire Dataset

SELECT *
FROM banking_fundamentals_data;

------------------------------------------------

-- Average Deposits

SELECT
AVG(Deposits) AS Average_Deposits
FROM banking_fundamentals_data;

------------------------------------------------

-- Average Loans

SELECT
AVG(Loans) AS Average_Loans
FROM banking_fundamentals_data;

------------------------------------------------

-- Average Interest Rate

SELECT
AVG(InterestRate) AS Average_Interest_Rate
FROM banking_fundamentals_data;

------------------------------------------------

-- Maximum Deposits

SELECT
MAX(Deposits) AS Maximum_Deposits
FROM banking_fundamentals_data;

------------------------------------------------

-- Maximum Loans

SELECT
MAX(Loans) AS Maximum_Loans
FROM banking_fundamentals_data;

------------------------------------------------

-- Year-wise Deposits

SELECT
Year,
Deposits
FROM banking_fundamentals_data
ORDER BY Year;

------------------------------------------------

-- Year-wise Loans

SELECT
Year,
Loans
FROM banking_fundamentals_data
ORDER BY Year;

------------------------------------------------

-- Credit Deposit Ratio

SELECT
Year,
CreditDepositRatio
FROM banking_fundamentals_data
ORDER BY Year;

------------------------------------------------

-- Banking Growth Ranking

SELECT
Year,
BankingGrowth
FROM banking_fundamentals_data
ORDER BY BankingGrowth DESC;

------------------------------------------------

-- Deposits Greater Than 1200

SELECT *
FROM banking_fundamentals_data
WHERE Deposits > 1200;

------------------------------------------------

-- Loans Greater Than 1000

SELECT *
FROM banking_fundamentals_data
WHERE Loans > 1000;

------------------------------------------------

-- Interest Rate Below 6%

SELECT *
FROM banking_fundamentals_data
WHERE InterestRate < 6;

------------------------------------------------

-- Highest Banking Growth Year

SELECT *
FROM banking_fundamentals_data
ORDER BY BankingGrowth DESC
LIMIT 1;

------------------------------------------------

-- Deposits and Loans Comparison

SELECT
Year,
Deposits,
Loans
FROM banking_fundamentals_data
ORDER BY Year;