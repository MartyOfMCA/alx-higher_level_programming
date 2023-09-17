#!/usr/bin/python3
"""
Deletes States with names containing the letter
`a`.
The MySQL username, password and database
are given as arguments to the module
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
        states = session.query(State).filter(
                State.name.contains("a"))

        for state in states:
            session.delete(state)

        session.commit()
