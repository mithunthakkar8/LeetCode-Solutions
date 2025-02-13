-- Write your PostgreSQL query statement below
select activity_date as day
    , count(distinct user_id) active_users
from activity
where activity_date <= '2019-07-27'
and activity_date > date '2019-07-27'-30
group by activity_date

