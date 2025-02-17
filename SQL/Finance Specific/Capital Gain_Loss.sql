-- Write your PostgreSQL query statement below
with stock_operations_grouped as (
select stock_name, operation, sum(price) as total_price
from stocks
group by stock_name, operation), 
gain_loss as (
select stock_name
    , case when operation = 'Sell' then total_price - lag(total_price) over (partition by stock_name order by operation) else 0 end as capital_gain_loss
    , operation
from stock_operations_grouped)
select stock_name
    , capital_gain_loss
from gain_loss
where operation = 'Sell'
