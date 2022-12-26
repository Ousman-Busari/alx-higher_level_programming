#!/usr/bin/python3
"""State class definition, and Base class from SQLAlchmey ORM"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """general object represenation of rows in states table in a MySQL database

    __tablename__ (str): The name of the table in the database
    id (sqlalchemy.Integer): The id of the row
    name (sqlalchemy.String): The name of the state
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
