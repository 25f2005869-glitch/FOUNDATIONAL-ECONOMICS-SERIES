SELECT * FROM money_currency;

SELECT AVG(InflationRate)
FROM money_currency;

SELECT MAX(CurrencyInCirculation)
FROM money_currency;

SELECT Year,
       DigitalPayments
FROM money_currency
ORDER BY Year;

SELECT Year,
       MoneySupply
FROM money_currency
ORDER BY MoneySupply DESC;

SELECT AVG(MoneySupply) AS AvgMoneySupply,
       AVG(InflationRate) AS AvgInflation
FROM money_currency;