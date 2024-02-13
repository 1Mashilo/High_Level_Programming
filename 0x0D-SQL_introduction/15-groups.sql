-- This script groups records by 'score' and displays counts, sorted in descending order
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;

