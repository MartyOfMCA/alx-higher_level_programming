#!/usr/bin/python3
"""
Updates the name of a state in the given
database.
The MySQL username, password, database name
and the searched state are given as arguments
to the module.
"""
from sys import argv
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if (__name__ == "__main__"):
    engine = create_engine(f"mysql:///{argv[3]}",
                           pool_pre_ping=True)
    session = sessionmaker(engine)

    with session() as session:
        state = session.query(State).get(2)
        state.name = "New Mexico"
        session.add(state)
        session.commit()
