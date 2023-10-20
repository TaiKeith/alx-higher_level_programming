-- This script uses hbtn_0d_tvshows database to list all genres of the show Dexter
-- The tv_shows table contains only 1 record where title = Dexter but id can be different
-- Each record displays: tv_genres.name
-- Results are sorted in ascending order by the genre name
SELECT `tv_genres`.`name`
FROM `tv_show_genres` INNER JOIN `tv_genres`
ON `tv_show_genres`.`genre_id` = `tv_genres`.`id`
INNER JOIN `tv_shows`
ON `tv_shows`.`id` = `tv_show_genres`.`show_id`
WHERE `tv_shows`.`title` LIKE 'Dexter'
ORDER BY `tv_genres`.`name`;
