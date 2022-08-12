-- Script updates Bob's score to 10 in the hbtn_0c-0 database
-- of mySQL using only the name field and not the id value
-- The database name will be passed as an argument of the mysql command
UPDATE second_table SET score = 10 WHERE name = "Bob";
