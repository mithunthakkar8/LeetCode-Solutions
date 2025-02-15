-- Write your PostgreSQL query statement below
select query_name
    , round(avg(round(rating,2)/position),2) quality
    , round(round(sum(case when rating <3 then 1 else 0 end),2)/count(*)*100,2) poor_query_percentage
from queries
group by query_name
