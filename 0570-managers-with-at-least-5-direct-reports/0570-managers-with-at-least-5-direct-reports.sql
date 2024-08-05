-- SELECT  e1.name
-- FROM    Employee e1
-- WHERE   5 <= (
--     SELECT  COUNT(*)
--     FROM    Employee e2
--     WHERE   e1.id = e2.managerId
-- ) 

SELECT  e1.name
FROM    Employee e1 JOIN Employee e2 ON e1.id = e2.managerId
GROUP BY    e1.id
HAVING      5 <= COUNT(e1.id)
