-- Write your PostgreSQL query statement below
with last_change_dates as (
select product_id
    , max(change_date) last_change_date
from products
where change_date <= '2019-08-16'
group by product_id)
select distinct p1.product_id
    , case when p1.product_id not in (select product_id from last_change_dates) then 10 else new_price end as price
from products p1
left join last_change_dates lcd
on p1.product_id = lcd.product_id
where lcd.last_change_date = p1.change_date 
or p1.product_id not in (select product_id from last_change_dates)
