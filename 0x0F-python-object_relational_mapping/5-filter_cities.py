#!/usr/bin/python3
"""
Lists all cities for the given state.
The MySQL username, password, database name
and the searched state are given as arguments
to the module.
"""


from sys import argv
from MySQLdb import connect

if (__name__ == "__main__"):
    cities = ""

    with connect(db=argv[3]) as connection:
        with connection.cursor() as cursor:

            cursor.execute("SELECT cities.name\
                            FROM states INNER JOIN cities\
                            ON states.id = state_id\
                            WHERE states.name = %s;",
                           (argv[4],))

            for row in cursor.fetchall():
                cities += f"{row[0]}, "

            print(cities[0:-2])
