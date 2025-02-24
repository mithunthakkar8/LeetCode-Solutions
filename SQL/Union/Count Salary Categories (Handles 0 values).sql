SELECT 'Low Salary' AS category, 
       COUNT(case when income<20000 then 1 else null end) AS accounts_count
FROM Accounts
UNION ALL
SELECT 'Average Salary', 
       COUNT(case when income>=20000 and income<=50000 then 1 else null end)
FROM Accounts
UNION ALL
SELECT 'High Salary', 
       COUNT(case when income>50000 then 1 else null end)
FROM Accounts;
