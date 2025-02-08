-- Write your PostgreSQL query statement below
with customer_product_counts as (
select customer_id
    , count(distinct c.product_key) product_count
from customer c
join product p
on c.product_key = p.product_key
group by customer_id)
select customer_id 
from customer_product_counts 
where product_count = (select count(*)
from product)
