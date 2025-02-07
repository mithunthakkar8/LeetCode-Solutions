-- Write your PostgreSQL query statement below
select coalesce(
    (select num
    from MyNumbers
    group by num
    having count(*)=1
    order by num desc
    offset 0 rows 
    fetch next 1 rows only)
    , null) num
