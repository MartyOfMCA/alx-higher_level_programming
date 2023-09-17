#!/usr/bin/python3
"""
Prints all City objects along with the
States they belong to.
The MySQL username, password and database
are given as arguments to the module
"""
from sys import argv
from model_state import Base, State
from model_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if (__name__ == "__main__"):
    engine = create_engine(f"mysql:///{argv[3]}",
                           pool_pre_ping=True)
    session = sessionmaker(engine)

    with session() as session:
        cities = session.query(City)

        for city in cities:
            print(f"{city.state.name}: ({city.id}) {city.name}")
