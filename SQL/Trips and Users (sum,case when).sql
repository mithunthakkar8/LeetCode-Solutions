-- Write your PostgreSQL query statement below
select request_at as Day
    , round(cast(sum(case when status = 'cancelled_by_driver' 
                    or status = 'cancelled_by_client'
                    then 1 else 0 end) as numeric(8,2))/count(*),2)  as "Cancellation Rate"
from trips t
left join users u1
on t.client_id = u1.users_id
left join users u2
on t.driver_id = u2.users_id
where u1.banned = 'No'
    and u2.banned = 'No'
    and request_at between '2013-10-01' and '2013-10-03'
group by request_at
