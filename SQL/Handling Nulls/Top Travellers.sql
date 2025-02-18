-- Write your PostgreSQL query statement below
with top_travellers_by_id as (
select u.id
    , sum(coalesce(distance,0)) as travelled_distance
from users u
left join rides r
on u.id = r.user_id
group by u.id)
select name
    , travelled_distance
from top_travellers_by_id ttid
join users u
on u.id = ttid.id
order by travelled_distance desc, name



