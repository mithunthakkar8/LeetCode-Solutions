-- Write your PostgreSQL query statement below
with procesing_time_per_process as (
select machine_id
    , timestamp
    - lag(timestamp) over (order by machine_id, process_id, activity_type desc) 
    as processing_time
    , activity_type
from activity)
select machine_id
    , round(cast(avg(processing_time) as numeric),3) as processing_time
from procesing_time_per_process
where activity_type = 'end'
group by machine_id
