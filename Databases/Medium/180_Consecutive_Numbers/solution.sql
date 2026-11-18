
WITH ConsecutiveLogs AS (
    SELECT
        id,
        num,

        LAG(num) OVER (
            ORDER BY id
        ) AS previous_num,

        LEAD(num) OVER (
            ORDER BY id
        ) AS next_num

    FROM Logs
)

SELECT DISTINCT
    num AS ConsecutiveNums
FROM ConsecutiveLogs
WHERE
    num = previous_num
    AND num = next_num;
