#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


class Query:
    """Define class for efficiency in database interaction"""

    def __init__(self):
        self.connection = psycopg2.connect("dbname=tournament")
        self.cursor = self.connection.cursor()

    def execute(self, sql_string, placeholder=(), commit=True):
        self.cursor.execute(sql_string, placeholder)

        if commit == False:
            return self.cursor.fetchall()
        else:
            self.connection.commit()

        self.close()

    def close(self):
        self.cursor.close()
        self.connection.close()


def deleteMatches():
    """Clears all records from matches table"""
    Query().execute("DELETE FROM matches")


def deletePlayers():
    """Clears all records from players table"""
    Query().execute("DELETE FROM players")


def countPlayers():
    """Find total number of players"""
    return Query().execute("SELECT COUNT(*) FROM players", commit=False)[0][0]


def registerPlayer(name):
    """Add new record to players table, protecting against SQL injection attacks"""
    Query().execute("INSERT INTO players(name) VALUES(%s)", (name,))


def playerStandings():
    """Return list of players sorted by wins from standings view"""
    return Query().execute("SELECT * FROM standings", commit=False)


def reportMatch(winner, loser):
    """Add new record to matches table, protecting against SQL injection attacks"""
    Query().execute(
        "INSERT INTO matches(winner_id, loser_id) VALUES(%s, %s)", (winner, loser,)
    )


def swissPairings():
    """Returns a list of pairs of payers matched according to wins"""
    results = Query().execute("SELECT id, name FROM standings", commit=False)
    pairs = len(results) / 2
    list_pairs = []

    for i in range(pairs):
        list_pairs.append(results.pop() + results.pop())

    return list_pairs
