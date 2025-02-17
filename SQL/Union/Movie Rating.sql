-- Write your PostgreSQL query statement below
(select u.name as results
from users u 
join movierating mr
on u.user_id = mr.user_id
group by u.name
order by count(movie_id) desc, u.name, length(u.name)
offset 0 rows
fetch next 1 row only )
union all
(select title as results
from movies m
join movierating mr
on m.movie_id = mr.movie_id
where to_char(created_at, 'YYYY-MM') = '2020-02'
group by title
order by avg(rating) desc, title, length(title)
offset 0 rows 
fetch next 1 row only)
