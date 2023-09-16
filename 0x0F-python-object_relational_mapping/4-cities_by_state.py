#!/usr/bin/python3
"""
Lists all cities with the states they belong to.
The MySQL username, password and database name
are given as arguments to the module.
"""


from sys import argv
from MySQLdb import connect

if (__name__ == "__main__"):
    with connect(db=argv[3]) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT cities.id,\
                            cities.name,\
                            states.name\
                            FROM states INNER JOIN cities\
                            ON state_id = states.id\
                            ORDER BY cities.id;")

            for row in cursor.fetchall():
                print(row)
