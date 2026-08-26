# Write your MySQL query statement below
with new_table as (
    select 
        d.name as Department,
        e.name as Employee,
        e.salary as Salary,
        DENSE_RANK() over (
            partition by d.name
            order by e.salary desc 
        ) as Ranking
    from Employee e
    left join Department d
        ON e.departmentId = d.id
)
select 
    Department,
    Employee,
    Salary
from new_table
where Ranking <= 3;