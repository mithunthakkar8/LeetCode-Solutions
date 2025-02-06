-- Write your PostgreSQL query statement below
select name
from salesperson 
where sales_id not in 
(select sales_id
from orders o
left join company c
on o.com_id = c.com_id
where c.name = 'RED')
