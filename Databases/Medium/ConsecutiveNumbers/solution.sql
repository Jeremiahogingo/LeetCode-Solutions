SELECT DISTINCT
    num AS ConsecutiveNums
FROM (
    SELECT
        num,
        LAG(num, 1) OVER (ORDER BY id) AS prev_num,
        LAG(num, 2) OVER (ORDER BY id) AS prev_prev_num
    FROM Logs
) t
WHERE num = prev_num
  AND num = prev_prev_num;