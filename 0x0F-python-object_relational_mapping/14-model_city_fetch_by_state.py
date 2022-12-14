#!/usr/bin/python3
"""deletes all State objects with a name containing the letter
a from the database hbtn_0e_6_usa
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)
    for s, c in session.query(State, City)\
                       .filter(State.id == City.state_id)\
                       .order_by(City.id):
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.close()
