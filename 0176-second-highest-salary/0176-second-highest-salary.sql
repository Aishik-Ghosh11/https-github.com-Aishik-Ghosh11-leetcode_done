WITH RankedSalaries AS (
    SELECT 
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM Employee
)
SELECT (
    SELECT DISTINCT salary 
    FROM RankedSalaries 
    WHERE rnk = 2
) AS SecondHighestSalary;