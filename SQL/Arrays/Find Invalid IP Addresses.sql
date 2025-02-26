-- Write your PostgreSQL query statement below
with invalid_ips as (
select ip
from logs
where array_length(string_to_array(ip, '.'),1) <> 4
or ip ~ '^0'
or ip ~ '.*\.0'
or 255<any(string_to_array(ip, '.')::int[])
)
select ip
    , count(*) as invalid_count
from invalid_ips
group by ip
order by invalid_count desc, ip desc

