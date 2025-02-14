-- Write your PostgreSQL query statement below
with first_order_dates as 
(
    select customer_id 
        , min(order_date) as first_order_date
    from delivery
    group by customer_id
)
select round(round(count(case when order_date = customer_pref_delivery_date and order_date = first_order_date then d.customer_id end),2)/count(distinct d.customer_id)*100,2) as immediate_percentage
from delivery d 
join first_order_dates fod
on d.customer_id = fod.customer_id




