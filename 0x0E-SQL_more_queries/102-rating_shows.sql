-- Retrieves all shows by their ratings
SELECT	title,
	SUM(rate) AS rating
FROM	tv_shows
	INNER JOIN tv_show_ratings
		ON id = show_id
GROUP BY title
ORDER BY rating DESC;
