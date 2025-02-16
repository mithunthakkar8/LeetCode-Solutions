-- Write your PostgreSQL query statement below
with daily_sales as (
    select visited_on
            , sum(amount) as sale
    from customer
    group by visited_on
),
moving_averages_preprocessed as (
select visited_on   
    , sum(sale) over (order by visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as amount
    , round(avg(sale) over (order by visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW),2) as average_amount
    , row_number() over () ranker
from daily_sales)
select visited_on
    , amount
    , average_amount
from moving_averages_preprocessed
where ranker > 6

