#!/usr/bin/python3
"""creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from relationship_state import State
from relationship_city import Base, City
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)

    new_state = State(name="California")
    new_state.cities = [City(name="San Francisco")]

    session.add(new_state)
    session.commit()
    session.close()
