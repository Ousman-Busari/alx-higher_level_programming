#!/usr/bin/python3
"""updates the name of a State object from the database hbtn_0e_6_usa"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)

    id_state = session.query(State).get(2)
    id_state.name = "New Mexico"
    session.add(id_state)
    session.commit()
    session.close()
