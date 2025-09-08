#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch the first state ordered by id
    state = session.query(State).order_by(State.id).first()

    # Print result
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    session.close()
