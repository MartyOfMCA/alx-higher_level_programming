#!/usr/bin/python3
"""
Prints all City objects along with name of
the state they belong.
The MySQL username, password and database
are given as arguments to the module
"""
from sys import argv
from relationship_city import City
from relationship_state import State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if (__name__ == "__main__"):
    engine = create_engine(f"mysql:///{argv[3]}",
                           pool_pre_ping=True)
    session = sessionmaker(engine)

    with session() as session:
        cities = session.query(City)

        for city in cities:
            state = city.state
            print(f"{city.id}: {city.name} -> {state.name}")
