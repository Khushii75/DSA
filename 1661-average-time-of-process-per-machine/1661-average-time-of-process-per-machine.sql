# Write your MySQL query statement below
select machine_id , 
round(avg(case when activity_type='end' then timestamp end)- 
avg(case when activity_type='start' then timestamp end),3) as processing_time
from activity
group by machine_id
