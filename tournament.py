#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

class Query():
    """Define class for efficiency in database connection"""
    def __init__(self):
        self.connection = psycopg2.connect("dbname=tournament")
        self.cursor = self.connection.cursor()
    
    def execute(self, sql_string, commit = True):
        self.cursor.execute(sql_string)
        
        if commit == False:
            return self
        else:
            self.connection.commit()
            self.close()

    def security(self):
        return self
    
    def close(self):
        self.cursor.close()
        self.connection.close()
        
def deleteMatches():
    """Clears matches from database"""
    Query().execute("DELETE FROM matches")

def deletePlayers():
    """Clear players from database"""
    Query().execute("DELETE FROM players")

def countPlayers():
    """Find total number of players"""
    object = Query().execute("SELECT COUNT(*) FROM players", False)
    result = object.cursor.fetchone()
    object.close()
    return result[0]

def registerPlayer(name):
    """Add new record to players, protecting against SQL injection attacks"""
    object = Query().security()
    object.cursor.execute("INSERT INTO players(name) VALUES(%s)", (name,))
    object.connection.commit()
    object.close()

def playerStandings():
    """Query view to return list of players sorted by wins"""
    object = Query().execute("SELECT * FROM standings", False)
    results = object.cursor.fetchall()
    object.close()
    return results

def reportMatch(winner, loser):
    """Add new record to matches, protecting against SQL injection attacks"""
    object = Query().security()
    object.cursor.execute("INSERT INTO matches(winner_id, loser_id) VALUES(%s, %s)", (winner, loser,))
    object.connection.commit()
    object.close()
 
 
def swissPairings():
    """Returns a list of pairs of payers, matched according to wins"""
    object = Query().execute("SELECT id, name FROM standings", False)
    results = object.cursor.fetchall()
    
    # find out how many players there are, which gives us pairs we need to make
    pairs = len(results)/2
    
    # declare a new list to return, and tuple to hold player pairs
    list = []
    tuple = ()
    
    # iterate through the players (already sorted by wins), storing pairs in tuples and appending to the list
    for i in range(pairs):
        tuple = results.pop() + results.pop()
        list.append(tuple)
    
    object.close()
    return list
