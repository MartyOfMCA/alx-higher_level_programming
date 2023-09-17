#!/usr/bin/python3
"""
Prints all States and their corresponding
City objects.
The MySQL username, password and database
are given as arguments to the module
"""
from sys import argv
from relationship_state import State
from relationship_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if (__name__ == "__main__"):
    engine = create_engine(f"mysql:///{argv[3]}",
                           pool_pre_ping=True)
    session = sessionmaker(engine)

    with session() as session:
        states = session.query(State)

        for state in states:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"    {city.id}: {city.name}")

    """
    An overly complicated approach to the previous
    code. The search starts with the city rather
    than the state and reverses back to the cities
    for a state.
    =============================================
    with session() as session:
        cities = session.query(City)

        previous_state = ""
        for city in cities:
            if (city.state.name != previous_state):
                print(f"{city.state.id}: {city.state.name}")
                for city_in_state in city.state.cities:
                    print(f"    {city_in_state.id}: {city_in_state.name}")
            previous_state = city.state.name
    """
