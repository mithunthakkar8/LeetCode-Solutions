-- Write your PostgreSQL query statement below
with aggregated_weight as (
select person_id    
    , person_name
    , weight
    , turn 
    , sum(weight) over (order by turn) cum_sum
from queue
)
select person_name
from aggregated_weight
where cum_sum<=1000
order by cum_sum desc
offset 0 rows
fetch next 1 row only


