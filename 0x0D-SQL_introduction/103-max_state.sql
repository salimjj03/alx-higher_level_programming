-- converts hbtn_0c_0 database to UTF8
-- converts hbtn_0c_0 database to UTF8
SELECT state, MAX(value) AS max_temp
FROM temperatures GROUP BY state ORDER BY state;
