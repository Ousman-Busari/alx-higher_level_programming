-- create a table second_table in databse hbtn_0c_0
-- in my MySQL server
CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT) ;
INSERT INTO second_table
VALUES
	(1, 'John', 10),
	(2, 'ALex', 3),
	(3, 'Bob', 14),
	(4, 'George', 8) ;
