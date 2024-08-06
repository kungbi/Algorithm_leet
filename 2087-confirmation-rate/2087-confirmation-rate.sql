-- SELECT  s.user_id, ROUND(IFNULL((
--     SELECT  COUNT(*)
--     FROM    confirmations c
--     WHERE   c.action = 'confirmed' AND s.user_id = c.user_id
-- ) / (
--     SELECT  COUNT(*)
--     FROM    confirmations c
--     WHERE   s.user_id = c.user_id
-- ), 0), 2) AS confirmation_rate
-- FROM    signups s

SELECT      s.user_id, ROUND(
    AVG(IF(c.action = 'confirmed', 1, 0))
, 2) AS 'confirmation_rate'
FROM        signups s LEFT JOIN confirmations c ON s.user_id = c.user_id
GROUP BY    s.user_id