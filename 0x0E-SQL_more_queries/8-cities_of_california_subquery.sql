-- List all the cities found in the
-- state California
SELECT	id,
	name
FROM	cities
WHERE	state_id =
	(
		SELECT	id
		FROM	states
		WHERE	name = 'California'
	)
ORDER BY id;
