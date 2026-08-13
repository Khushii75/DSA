-- # Write your MySQL query statement below
-- select e1.name
-- from employee e1, employee e2
-- where e1.id = e2.managerId 
-- group by e1.id , e1.name
-- having count(*)>=5

# Write your MySQL query statement below 
select e1.name
from Employee as e1
join Employee as e2 on 
e1.id = e2.managerId
group by e2.managerId
having count(e2.managerId)>=5;