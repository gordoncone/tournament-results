#!/usr/bin/env python

# tournament.py -- implementation of a Swiss-system tournament


import psycopg2

#Connecting to tournament database 
def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

#Deleting all data from record table
def deleteMatches():
    """Remove all the match records from the database."""
    db = connect
    c = db.cursor ()
    c.execute("delete from record")
    db.commit()
    db.close();


#Deleting all data from players table
def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor ()
    c.execute("delete from players1")
    db.commit()
    db.close();

#Count number of players in tournament
def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute("select count(player_id) from players1")
    rows = c.fetchall()
    db.commit()
    db.close();
    return rows

#Registering a new player
def registerPlayer(first_name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    #Used this to load data into my players1 table... I tried to upload the data using a csv file but couldn't get it t work.
    c.execute("insert into players1 values (%s)",(player_id, first_name, last_name, age))
    db.commit()
    db.close();

#Based on the Swiss system each round has the same number of matches and players
#I created a bracket swiss system and matched players based on win vs lose ratio    
def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    c = db.cursor()
    c.execute("select record.player_id, players1.first_name, record.wins, record.t_matches from record, players1 where record.player_id = players1.player_id order by wins desc ")
    rows = c.fetchall()
    db.close()
    returen rows
    

#Created a table that tracked all the matches during the swiss tournament
def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
     db = connect()
     c = db.cursor()
     c.execute("insert into matches values (%s)", ('matches','winners','losers'))
     db.commit()
     db.close()

 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
#Need a little more time to figure this out. 
    db = connect()
    c = db.cursor()
    c.execute("select players1.player_id, players1.first_name, matches.matches from players, matches where players1.player_id = matches.matches")
    db.commit()
    db.close()

