#!/usr/bin/python3
"""
Fetch the first State from the given database
"""
from sys import argv
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


if (__name__ == "__main__"):
    engine = create_engine(f"mysql:///{argv[3]}",
                           pool_pre_ping=True)

    Session = sessionmaker(engine)

    with Session() as session:
        state = session.query(State).first()
        if (state):
            print(f"{state.id}: {state.name}")
        else:
            print("Nothing")
