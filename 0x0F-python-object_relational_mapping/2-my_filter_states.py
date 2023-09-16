#!/usr/bin/python3
"""
Lists all states matching a given state name.
The MySQL username, password, database name
and the searched state are given as arguments
to the module.
"""


from sys import argv
import MySQLdb

if (__name__ == "__main__"):
    with MySQLdb.connect(db=argv[3]) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name\
                            FROM states\
                            WHERE BINARY name = '{}';".
                           format(argv[4]))

            for row in cursor.fetchall():
                print(row)
