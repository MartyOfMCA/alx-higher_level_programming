-- Retrieves all shows not having the
-- genre named Comedy
SELECT	title
FROM	tv_shows
WHERE	id NOT IN
	(
		SELECT	show_id
		FROM	tv_show_genres
			INNER JOIN tv_genres
				ON id = genre_id
		WHERE	name = 'Comedy'
	)
ORDER BY title;
