-- Write your PostgreSQL query statement below
with employees_ranked_by_department as (
select d.name Department
    , e.name Employee
    , e.salary Salary
    , rank() over (partition by d.name order by e.salary desc) rank_
from employee e
join department d
on e.departmentId = d.id)
select Department
    , Employee
    , Salary
from employees_ranked_by_department
where rank_=1
