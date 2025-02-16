-- Write your PostgreSQL query statement below
with units_revenue as (
select  p.product_id
        , coalesce(round(price*units,2),0) as revenue
        , coalesce(units,1) as units
from prices p
left join unitssold u
on p.product_id = u.product_id
where purchase_date between start_date and end_date
or u.product_id is null
)
select product_id
    , round(round(sum(revenue),2)/sum(units),2) as average_price
from units_revenue
group by product_id
