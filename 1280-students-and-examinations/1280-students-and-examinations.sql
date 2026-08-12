# Write your MySQL query statement below
select s.student_id, s.student_name, su.subject_name, count(e.student_id) as attended_exams
from students s
cross join subjects su 
left join examinations e on e.student_id=s.student_id 
AND e.subject_name = su.subject_name
group by student_id,
student_name,
subject_name
order by student_id asc
