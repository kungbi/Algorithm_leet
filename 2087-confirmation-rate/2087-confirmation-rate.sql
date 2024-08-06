SELECT  s.user_id, ROUND(IFNULL((
    SELECT  COUNT(*)
    FROM    confirmations c
    WHERE   c.action = 'confirmed' AND s.user_id = c.user_id
) / (
    SELECT  COUNT(*)
    FROM    confirmations c
    WHERE   s.user_id = c.user_id
), 0), 2) AS confirmation_rate
FROM    signups s