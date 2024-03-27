-- script that lists all records with a score >= 10 in the table second_table
-- We use SELECT, WHERE and ORDER BY
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
