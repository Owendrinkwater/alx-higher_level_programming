#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
in the format: <state name>: (<city id>) <city name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = (
        session.query(State, City)
        .join(City, State.id == City.state_id)
        .order_by(City.id)
        .all()
    )
    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")
