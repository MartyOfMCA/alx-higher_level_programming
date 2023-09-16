#!/usr/bin/python3
"""
Lists all states from the given database.
The MySQL username, password and database
are given as arguments to the module
"""


from sys import argv
import MySQLdb

if (__name__ == "__main__"):
    connection = MySQLdb.connect(user=argv[1],
                                 passwd=argv[2],
                                 db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM states;")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    connection.close()
