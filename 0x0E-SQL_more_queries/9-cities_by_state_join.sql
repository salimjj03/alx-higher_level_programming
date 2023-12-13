-- script that lists all privileges of the MySQL users user_0d_1
-- and user_0d_2 on your server (in localhost)
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON states.id = cities.state_id
ORDER BY id ASC;
