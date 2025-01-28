/* Write your T-SQL query statement below */
with lagging_nums as (
select num
    , lag(num,1) over (order by id) lag_1
    , lag(num,2) over (order by id) lag_2
from logs)
select distinct num ConsecutiveNums
from lagging_nums
where num = lag_1 
and num = lag_2
