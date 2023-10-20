-- This script lists all shows without the genre Comedy in the database
-- tv_genres table contains only 1 record where name = Comedy but id can be different
-- Results sorted in ascending order by the show title
SELECT tv_shows.title FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name != "Comedy"
ORDER BY tv_shows.title ASC;
