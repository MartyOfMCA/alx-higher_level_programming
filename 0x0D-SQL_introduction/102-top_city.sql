-- Retrieves the top 3 city's temperature
-- during the month of July and August
-- ordered by temperature
SELECT	city,
	AVG(value) AS avg_temp
FROM	temperatures
WHERE	month IN(7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
