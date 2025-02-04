-- Write your PostgreSQL query statement below
with order_details as (
select customer_number
    , count(*) number_of_orders
from orders
group by customer_number)
select customer_number
from order_details
order by number_of_orders desc
offset 0 rows 
fetch next 1 rows only
