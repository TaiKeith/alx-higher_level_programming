-- This script lists all shows from hbtn_0d_tvshows_rate by their rating
-- Each record displays: tv_shows.title - rating sum
-- Results are sorted in descending order by the rating
SELECT tv_shows.title, SUM(rate) AS rating FROM tv_shows
INNER JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title ORDER BY rating DESC;
