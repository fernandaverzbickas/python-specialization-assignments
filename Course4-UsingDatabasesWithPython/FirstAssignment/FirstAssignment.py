# If you don't already have it, install the SQLite Browser from http://sqlitebrowser.org/.
import sqlite3

conn = sqlite3.connect('firstassignment.sqlite')
cur = conn.cursor()

#Then, create a SQLITE database or use an existing database and create a table in the database called "Ages":
cur.execute('DROP TABLE IF EXISTS Ages')

cur.execute(
    '''
    CREATE TABLE Ages ( 
        name VARCHAR(128), 
        age INTEGER
    )'''
)

# Then make sure the table is empty by deleting any rows that you previously inserted, and insert these rows and only these rows with the following commands:

cur.executescript(
    '''
        DELETE FROM Ages;
        INSERT INTO Ages (name, age) VALUES ('Anees', 24);
        INSERT INTO Ages (name, age) VALUES ('Hajrah', 22);
        INSERT INTO Ages (name, age) VALUES ('Frederick', 13);
        INSERT INTO Ages (name, age) VALUES ('Keris', 16);
        INSERT INTO Ages (name, age) VALUES ('Hagun', 35);
    '''
)

# This assignment must be done using SQLite - in particular, the SELECT query will not work in any other database. 
# So you cannot use MySQL or Oracle for this assignment.

#Once the inserts are done, run the following SQL command: SELECT hex(name || age) AS X FROM Ages ORDER BY X
#Expected output: 416E6565733234 

