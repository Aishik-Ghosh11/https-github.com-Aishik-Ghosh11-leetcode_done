select e.name as Employee from Employee e
where e.salary > 
(
    select salary from Employee
    where e.managerId = id
) ;