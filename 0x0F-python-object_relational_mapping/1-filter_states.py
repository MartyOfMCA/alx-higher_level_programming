#!/usr/bin/python3
"""
Lists all states from the given database
with the state name starting with the letter N.
The MySQL username, password and database
are given as arguments to the module
"""


from sys import argv
import MySQLdb

if (__name__ == "__main__"):
    with MySQLdb.connect(db=argv[3],
         passwd=argv[2], user=argv[1])\
         as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name\
                            FROM states\
                            WHERE BINARY name LIKE %s;",
                           ("N%",))

            for row in cursor.fetchall():
                print(row)
