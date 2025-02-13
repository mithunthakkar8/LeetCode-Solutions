-- Write your PostgreSQL query statement below
with user_orders as (
select u.user_id as buyer_id
    , count(*) orders_in_2019
from orders o
right join users u
on u.user_id = o.buyer_id
where date_part('year', order_date) = 2019
group by u.user_id)
select u.user_id as buyer_id
    , join_date
    , coalesce(orders_in_2019,0) as orders_in_2019
from users u
left join user_orders uo
on uo.buyer_id = u.user_id
