-- this lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- CREATE DATABASE IF NOT EXISTS hbtn_0d_tvshows;
-- USE hbtn_0d_tvshows;

-- populate `hbtn_0d_tvshows` from dump file `hbtn_0d_tvshows.sql`
-- source hbtn_0d_tvshows.sql
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
