#!/usr/bin/python3
"""
Fetch all states with the given name.
The name is given as a command-line
argument.
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
                State.name == argv[4])

        if (states.count() == 0):
            print("Not found")
        else:
            for state in states:
                print(f"{state.id}")
