-- Retrieves the maximum temperature of each
-- state ordered by the state name
SELECT	state,
	MAX(value) max_temp
FROM	temperatures
GROUP BY state
ORDER BY state;
