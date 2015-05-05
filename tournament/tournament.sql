-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Create Database
Create Database tournament;

-- Create Database Tables
CREATE TABLE players1(
	player_id INT PRIMARY KEY    NOT NULL,
	first_name           TEXT    NOT NULL,
	last_name            TEXT    NOT NULL,
	age                  INT     NOT NULL
);

CREATE TABLE record(
	player_id INT PRIMARY KEY           NOT NULL,
	wins			 INT        NOT NULL,
	loses			 INT	    NOT NULL,
	t_matches		 INT	    Not Null
);

-- Test Database Tables
testdb-# \d public.players1;

testdb-# \d record;

- Inserting data into players & record tables:
insert into players1 values ('1','Gordon','Cone','21');

insert into record values (‘1’,’1’,’2’,’3’);


-- Player Standings
select record.player_id, players1.first_name, record.wins, record.t_matches from record, players1 where record.player_id = players1.player_id order by wins desc;


-- Report Match wins
insert into matches  values ('matches','winners','losers')



--Create a View showing showing players standings
Create view Standings AS
	select record.player_id, players1.first_name, record.wins, record.t_matches from record, players1 where record.player_id = players1.player_id order by wins desc;



--Create a View showing all players by ID, Name, Age
	Create view All_players
	select player_id, first_name, age from players1;
  


