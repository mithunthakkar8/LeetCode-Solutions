-- Write your PostgreSQL query statement below
select name
    , sum(amount) as balance
from users u
join transactions t
on u.account = t.account
group by name
having sum(amount)>10000
