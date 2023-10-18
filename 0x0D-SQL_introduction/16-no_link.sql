-- This script lists all records of second_table
-- Don't list rows without a name value
-- Results should display in the order score and name
-- Records are in descending order
SELECT score, name FROM second_table WHERE name != "" ORDER BY score DESC;
