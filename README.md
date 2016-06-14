##README

###Overview

This application runs a Swiss-system tournament where losing players are not eliminated but paired with other players, who have a similar number of wins, in the subsequent rounds. The first stage of the project involved defining a relational database schema containing normalised data relating to players, their standings, and matches in multiple tables. The second stage involved writing SQL queries and Python functions to modify and extract this data, ensuring tournament progression and accurate reporting of information.


###How to Run

This application is dependent upon Postgresql and is made of three files: `tournament.sql` (contains database schema), `tournament.py` (updates and queries the database), and `tournament_test.py` (engages in unit testing).

Upon downloading the application, we will set up the database: open the psql command line tools by typing

`psql`

We will then import and run `tournament.sql`, which will create and connect to a new database (dropping any which already exists) and create relevant tables and views. Please refer to the specific file to see precise steps on how it does this

`\i tournament.sql`

The database (called tournament), tables (players and matches), and views (standings) have been created, to test that they function correctly in conjunction with `tournament.py`, exit psql and run the test file:

`\quit`

`python tournament_test.py`
