-- List number of records with same score
SELECT score, COUNT(1) as number FROM second_table GROUP BY score ORDER BY number DESC;
