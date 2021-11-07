CREATE TABLE tb_web_site AS (
    WITH cte_dedup_table AS (
        SELECT t1."date"
            ,t1.rank
            ,t1.artist
            ,row_number() OVER(PARTITION BY artist ORDER by artist, "date") as "dedup"
        FROM PUBLIC."Billboard" as t1
        ORDER BY t1.artist, t1."date"
    )
    SELECT t1."date"
        ,t1.rank
        ,t1.artist
    FROM cte_dedup_table AS t1
    WHERE t1.dedup = 1
);

SELECT * FROM tb_web_site

CREATE TABLE tb_artist AS (
    SELECT t1."date"
            ,t1.rank
            ,t1.artist
            ,t1.song
        FROM PUBLIC."Billboard" as t1
        WHERE t1.artist = 'AC/DC'
        ORDER BY t1.artist, t1."date"
)

SELECT * FROM tb_artist

CREATE VIEW view_artist AS (
    WITH cte_dedup_table AS (
        SELECT t1."date"
            ,t1.rank
            ,t1.artist
            ,row_number() OVER(PARTITION BY artist ORDER by artist, "date") as "dedup"
        FROM tb_artist as t1
        ORDER BY t1.artist, t1."date"
    )
    SELECT t1."date"
        ,t1.rank
        ,t1.artist
    FROM cte_dedup_table AS t1
    WHERE t1.dedup = 1
);

SELECT * FROM view_artist