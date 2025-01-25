CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
            select distinct salary
            from employee
            order by salary desc
            offset case when @N-1<0 then 999999 else @N-1 end rows
            fetch next 1 row only

    );
END
