##README

###Overview

*In this section we explain what the project does, and the skills completing it demonstrates.*

Built a PostgreSQL relational database scheme to store the results of a game tournament. Also provided a number of queries to efficiently report the results of the tournament and determine the winner. You will learn how to architect and develop a database containing fully normalized data within multiple tables. You’ll then learn how to modify this data and query it to meet the demands of a variety of use cases.


###How to Run

There are three files: `tournament.sql` (contains database schema), `tournament.py` (contains python functions for manipulating database), and `tournament_test.py`; changes have been made to the first two files as part of the project but not to the third.

Now we will set up our database: open the psql command line tools by typing

`psql`

We will then import and run tournament.sql, which will create and connect to a new database (dropping any which already exists) and create relevant tables and views, please refer to the specific file to see precise steps on how it does this

`\i tournament.sql`

The database (called tournament), tables (players and matches), and views(standings) have been created, to test that they function correctly in conjunction with `tournament.py`, exit psql and run the test file:

`\quit`

`python tournament_test.py`
