#!/usr/bin/python3
""" prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)
    sig = 0
    for state in session.query(State):
        if state.name == sys.argv[4]:
            sig = 1
            print(state.id)
    if (sig == 0):
        print("Not found")
