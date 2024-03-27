-- lists the number of records with the same score in the table second_table
-- We use SELECT and GROUP BY
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
