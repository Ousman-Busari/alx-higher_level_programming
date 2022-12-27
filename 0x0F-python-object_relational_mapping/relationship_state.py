#!/usr/bin/python3
"""State class definition, and Base class from SQLAlchmey ORM"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """general object represenation of rows in states table in a MySQL database

    Attributes:
        __tablename__ (str): The name of the table in the database
        id (sqlalchemy.Integer): The id of the row
        name (sqlalchemy.String): The name of the state
        cities (list): list of the cities under the State
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
