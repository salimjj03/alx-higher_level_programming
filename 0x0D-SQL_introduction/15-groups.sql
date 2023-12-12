-- This script lists all databases of your MySQL server.
-- Display all databases.
SELECT `score`, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
