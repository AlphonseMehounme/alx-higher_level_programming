-- creates the table unique_id on your MySQL server
-- We use CREATE TABLE, DEFAULT and UNIQUE
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
