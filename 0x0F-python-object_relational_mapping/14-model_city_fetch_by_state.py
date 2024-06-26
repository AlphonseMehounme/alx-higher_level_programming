#!/usr/bin/python3
"""Fetch All Cities
"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)
    for state in states:
        cities = session.query(City).filter(City.state_id ==
                                            state.id).order_by(City.id)
        for city in cities:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
