-- The database name will be passed as an argument of the mysql command
-- If the table first_table already exists, your script should not fail
-- You are not allowed to use the SELECT or SHOW statements
-- script creates table called first_table with id(INT) and name VARCHAR(256)
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
