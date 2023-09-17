#!/usr/bin/python3
"""
Adds a new State object with a new City
object for the state added.
The MySQL username, password and database
are given as arguments to the module
"""
from sys import argv
from relationship_city import City
from relationship_state import State, Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if (__name__ == "__main__"):
    engine = create_engine(f"mysql:///{argv[3]}",
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)

    with session() as session:
        state = State()
        state.name = "California"
        session.add(state)
        session.commit()

        city = City()
        city.name = "San Francisco"
        city.state_id = state.id
        session.add(city)
        session.commit()
