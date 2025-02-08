-- Write your PostgreSQL query statement below
select id
    ,case when id%2=0 then lag(student) over (order by id)
        when id%2=1 and id <> (select max(id) from seat) 
            then lead(student) over (order by id) 
            else student end student
from seat
