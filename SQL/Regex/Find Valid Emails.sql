-- Write your PostgreSQL query statement below
select user_id
    , email
from users
where email ~ '^\w+@[a-zA-Z]+\.com$'
order by user_id
