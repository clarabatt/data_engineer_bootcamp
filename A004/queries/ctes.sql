WITH cte_artist AS (
    SELECT t1.artist
        ,COUNT(*) AS "#artist"
    FROM PUBLIC."Billboard" as t1
    GROUP BY t1.artist
    ORDER BY t1.artist ASC
),

cte_song AS (
    SELECT t1.song
        ,COUNT(*) AS "#song"
    FROM PUBLIC."Billboard" as t1
    GROUP BY t1.song
    ORDER BY t1.song ASC
),

SELECT DISTINCT t1.artist
    ,t2.qtd_artist
    ,t1.song
    ,t3.qtd_song
FROM PUBLIC."Billboard" as t1
LEFT JOIN cte_artist AS t2 ON (t1.artist = t2.artist)
LEFT JOIN cte_song AS t3 ON (t1.song = t3.song)
ORDER BY t1.artist, t1.song;

------------------------------

WITH cte_billboard AS (
    SELECT DISTINCT t1.artist
	,t1.song
    ,row_number() OVER(order by artist, song) as "row_number"
    ,row_number() OVER(partition by artist order by artist, song) as "row_number_artist"
    ,rank() OVER(partition by artist order by artist, song) as "rank"
    ,lag(song, 1) OVER(partition by artist order by artist, song) as "lag_song"
    ,lead(song, 1) OVER(partition by artist order by artist, song) as "lead_song"
    ,first_value(song) OVER(partition by artist order by artist, song) as "lead_song"
FROM PUBLIC."Billboard" as t1
ORDER BY t1.artist, t1.song
)

SELECT *
FROM cte_billboard
--WHERE "row_number_artist" = 1