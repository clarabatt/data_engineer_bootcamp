-- CREATE TABLE BILLBOARD

CREATE TABLE public."Billboard" (
    "date" date NULL,
    rank INT4 NULL,
    song VARCHAR(300) NULL,
    artist VARCHAR(300) NULL,
    "last-week" FLOAT8 NULL,
    "peak-rank" INT4 NULL,
    "weeks-on-board" INT4 NULL
);

SELECT count(*) AS amount
FROM PUBLIC."Billboard" LIMIT 100;

SELECT "date"
	,rank
	,song
	,artist
	,"last-week"
	,"peak-rank"
	,"weeks-on-board"
FROM PUBLIC."Billboard" LIMIT 100;

SELECT t1.artist
	,t1.song
FROM PUBLIC."Billboard" as t1
WHERE t1.artist = 'Olivia Rodrigo';

SELECT b.song
    ,b.artist
    , COUNT(*) AS song_amount
FROM PUBLIC."Billboard" as b
WHERE b.artist = 'Lady Gaga' or b.artist = 'Olivia Rodrigo'
GROUP BY b.song, b.artist
ORDER BY song_amount desc;