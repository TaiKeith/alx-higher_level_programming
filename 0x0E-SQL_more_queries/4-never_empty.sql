-- This script create a table id_not_null on MySQL server
-- id attribute has a default value 1
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256) NOT NULL);
