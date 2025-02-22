-- Write your PostgreSQL query statement below
select contest_id  
    , round(round(count(user_id),2)*100/(select count(*) from users),2) as percentage
from register r
group by contest_id
order by percentage desc, contest_id
