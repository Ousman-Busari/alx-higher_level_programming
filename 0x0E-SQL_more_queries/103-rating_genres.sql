-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT name, SUM(rate) as rating
FROM tv_show_ratings
     INNER JOIN tv_show_genres
     	   ON tv_show_ratings.show_id = tv_show_genres.show_id
     INNER JOIN tv_genres
     	   ON tv_show_genres.genre_id = tv_genres.id
GROUP BY name
ORDER BY rating DESC
