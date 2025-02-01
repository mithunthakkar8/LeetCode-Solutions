select e2.name Employee
from employee e1
join employee e2
on e1.id = e2.managerId
where e2.salary>e1.salary
