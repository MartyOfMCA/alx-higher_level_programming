#!/usr/bin/python3
"""
Defines a class that maps to a database
table called cities.
"""
from relationship_state import Base

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """
    Repesents the cities for the various
    states.
    """

    __tablename__ = "cities"

    id = Column(Integer,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(ForeignKey("states.id"),
                      nullable=False)
