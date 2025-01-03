DROP TABLE IF EXISTS anime_table;
DROP TABLE IF EXISTS test_table;
DROP TABLE IF EXISTS sourcekey;
DROP TABLE IF EXISTS ratingkey;
DROP TABLE IF EXISTS typekey;

CREATE TABLE anime_table(
    mal_id int PRIMARY KEY,
    name varchar(100),
    score float,
    genres varchar(125),
    type_lookup int,
    episodes int, 
    aired varchar(28),
    producers varchar(375),
    studios varchar(80),
    source_lookup int,
    duration varchar(21),
    rating_lookup int,
    popularity int
);

CREATE TABLE ratingkey (
    rating_lookup int PRIMARY KEY,
    rating varchar(30)
);

CREATE TABLE sourcekey (
    source_lookup int PRIMARY KEY,
    source varchar(13)
);

CREATE TABLE typekey (
    type_lookup int PRIMARY KEY,
    type varchar(7)
);

\copy anime_table from 'anime_edited.csv' with(format csv, null 'Unknown');
\copy ratingkey from 'ratingkey.csv' csv;
\copy sourcekey from 'sourcekey.csv' csv;
\copy typekey from 'typekey.csv' csv;

CREATE TABLE test_table as select * from anime_table limit 10;