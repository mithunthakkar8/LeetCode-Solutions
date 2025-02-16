-- Write your PostgreSQL query statement below
select s.student_id
    , student_name
    , sj.subject_name
    , count(e.subject_name) as attended_exams
from subjects sj
cross join students s
left join examinations e
on e.subject_name = sj.subject_name
and s.student_id = e.student_id
group by s.student_id, student_name, sj.subject_name
order by student_id
