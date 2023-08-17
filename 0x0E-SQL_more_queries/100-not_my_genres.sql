-- Retrieves all genres for the shows
-- not linked with the show called Dexter
SELECT	name
FROM	tv_genres
WHERE	id NOT IN
	(
		SELECT	genre_id
		FROM	tv_show_genres
			INNER JOIN tv_shows
				ON id = show_id
		WHERE	title = 'Dexter'
	)
ORDER BY name;
