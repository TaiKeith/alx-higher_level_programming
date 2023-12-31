-- This script lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- Each record displays <TV Show genre> - <Number of shows linked to this genre>
-- First column is called genre
-- Second column is called number_of_shows
-- Genres without any shows linked are not displayed
-- Results sorted in descending order by the number of shows linked
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows FROM tv_show_genres
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre ORDER BY number_of_shows DESC;
