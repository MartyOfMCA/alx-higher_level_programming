-- Retrieves records without NULL values
SELECT	score,
	name
FROM	second_table
WHERE NAME IS NOT NULL
ORDER BY score DESC;
