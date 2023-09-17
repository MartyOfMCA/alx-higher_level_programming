#!/usr/bin/python3
"""
Fetch all States from the given database.
"""
from sys import argv
from model_state import Base, State

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, select


if (__name__ == "__main__"):
    engine = create_engine(f"mysql:///{argv[3]}",
                           pool_pre_ping=True)

    Session = sessionmaker(engine)

    with Session() as session:
        states = session.query(State)

        for state in states:
            print(f"{state.id}: {state.name}")
