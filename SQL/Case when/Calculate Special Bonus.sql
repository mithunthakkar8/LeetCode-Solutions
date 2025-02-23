-- Write your PostgreSQL query statement below
select employee_id
    , case when employee_id % 2=1 
    and upper(left(name,1)) != 'M' then salary else 0 end bonus
from employees
order by employee_id
