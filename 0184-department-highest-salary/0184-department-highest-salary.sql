# Write your MySQL query statement below
select Department.name as Department , Employee.name as Employee, Employee.salary
from Department join Employee on Employee.departmentId=Department.id
WHERE(departmentId, salary) IN
(select departmentId, MAX(salary) from Employee group by departmentId) ;