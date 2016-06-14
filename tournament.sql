-- this will create and connect to a new database (replacing any existing ones)

drop database if exists tournament;

create database tournament;

\c tournament;

-- the datatypes assigned to 'players' table should be self-explanatory, we used serial datatype as we wanted an id to be automatically assigned, note that the same field uniquely identifies the record so it has been assigned the primary key

create table players (
    id serial primary key,
    name text
);

-- created simple table recording match data, the match_number uniquely identifies the record so has been assigned primary key. Given that winner and loser id has to be from players table, we have given both a foreign key and the match record will be deleted if one of the relevant players no longer exist in the players table

create table matches (
    match_number serial primary key,
    winner_id integer references players (id) on delete cascade,
    loser_id integer references players (id) on delete cascade
);

-- created view called standings, which displays player id, name, wins, and matches

create view standings as (
    select id, name,
    (select count(*) from matches where players.id = winner_id) as wins,
    (select count(*) from matches where players.id IN (winner_id, loser_id)) as matches
    from players order by wins desc
);