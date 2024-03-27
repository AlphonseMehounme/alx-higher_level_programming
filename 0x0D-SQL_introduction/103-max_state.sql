-- script that displays the max temperature of each state (ordered by State name)
-- We use SELECT, MAX and GROUP BY
SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state ASC;
