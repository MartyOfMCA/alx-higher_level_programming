#!/usr/bin/python3
"""
Defines a class that maps to a database
table called states.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """
    Represents the states resided by people
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
