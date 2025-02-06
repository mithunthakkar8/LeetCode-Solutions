-- Write your PostgreSQL query statement below
with requester_friends as (
    select requester_id id
        , count(accepter_id) number_of_friends
    from requestaccepted
    group by requester_id
), accepter_friends as (
    select accepter_id id
        , count(requester_id) number_of_friends
    from requestaccepted
    group by accepter_id
), friends_by_id as (
select id
    , number_of_friends
from accepter_friends 
union all
select id
    , number_of_friends
from requester_friends)
select id
    , sum(number_of_friends) num
from friends_by_id
group by id
order by num desc
offset 0 rows
fetch next 1 rows only
