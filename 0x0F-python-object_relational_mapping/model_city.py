#!/usr/bin/python3
"""State class definition, and Base class from SQLAlchmey ORM"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """general object represenation of rows in cities table in a MySQL database

    __tablename__ (str): The name of the table in the database
    id (sqlalchemy.Integer): The id of the row
    name (sqlalchemy.String): The name of the city
    state_id (sqlalchemy.Integer): the id of the state the city belongs to
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state_id'))
