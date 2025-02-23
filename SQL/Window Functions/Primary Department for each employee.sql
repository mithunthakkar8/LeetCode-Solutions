-- Write your PostgreSQL query statement below
with employee_dept_count as (
select employee_id
    , department_id
    , count(*) over (partition by employee_id) as dept_count
    , primary_flag
from employee)
select employee_id
    , department_id
from employee_dept_count
where primary_flag = 'Y'
    or dept_count = 1
