if (select count(distinct salary) from employee)>1
Begin
select distinct salary SecondHighestSalary
from employee 
order by salary desc
offset 1 rows
fetch next 1 row only
End
else 
begin
select null SecondHighestSalary
end
