#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def connect():
    try:
        connection = psycopg2.connect("dbname=tournament")
        cursor = connection.cursor()
        return connection, cursor
    except:
        print("Could not connect to database")

def close(connection, cursor):
    connection.close()
    cursor.close()

def deleteMatches():
    connection, cursor = connect()
    cursor.execute("DELETE FROM matches")
    connection.commit()
    close(connection, cursor)

def deletePlayers():
    connection, cursor = connect()
    cursor.execute("DELETE FROM players")
    connection.commit()
    close(connection, cursor)

def countPlayers():
    connection, cursor = connect()
    cursor.execute("SELECT COUNT(*) FROM players")
    result = cursor.fetchone()
    close(connection, cursor)
    # extract and return the result
    return result[0]

def registerPlayer(name):
    connection, cursor = connect()
    # we use a tuple here to prevent SQL injection attack
    cursor.execute("INSERT INTO players(name) VALUES(%s)", (name,))
    connection.commit()
    close(connection, cursor)

def playerStandings():
    connection, cursor = connect()
    # here we are querying the view we created
    cursor.execute("SELECT * FROM standings")
    results = cursor.fetchall()
    close(connection, cursor)
    return results

def reportMatch(winner, loser):
    connection, cursor = connect()
    # record the match result
    cursor.execute("INSERT INTO matches(winner_id, loser_id) VALUES(%s, %s)", (winner, loser,))
    connection.commit()
    close(connection, cursor)
 
 
def swissPairings():
    connection, cursor = connect()
    cursor.execute("SELECT id, name FROM standings")
    results = cursor.fetchall()
    
    # find out how many players there are, which gives us pairs we need to make
    pairs = len(results)/2
    
    # declare a new list to return, a tuple to hold player pairs we will append to list
    list = []
    tuple = ()
    
    # iterate through the results (already sorted by wins), storing pairs in tuples and appending to the list
    for i in range(pairs):
        tuple = results.pop() + results.pop()
        list.append(tuple)
    
    close(connection, cursor)
    return list
