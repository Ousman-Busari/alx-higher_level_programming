-- creates a table id_not_null on my MySQL server
-- in a database that will be passsed as an argument
CREATE TABLE IF NOT EXISTS id_not_null
       (id INT DEFAULT 1, name VARCHAR(256));
