-- converts hbtn_0c_0 database to UTF8
-- converts hbtn_0c_0 database to UTF8
SELECT city, AVG(value) AS avg_temp
FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
