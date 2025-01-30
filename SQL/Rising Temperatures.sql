-- Write your PostgreSQL query statement below
select w1.id
from weather w1, weather w2
where w1.temperature>w2.temperature
and w1.recordDate-1 = w2.recordDate
