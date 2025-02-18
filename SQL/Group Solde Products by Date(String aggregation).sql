-- Write your PostgreSQL query statement below
select sell_date
    , count(product) as num_sold
    , string_agg(product, ',' order by product) as products
from (select distinct * from activities)
group by sell_date
