-- This script lists records from 'second_table'; filters out null names, ordered by score (descending)
SELECT score, name FROM second_table 
WHERE name IS NOT NULL 
ORDER BY score DESC; 

