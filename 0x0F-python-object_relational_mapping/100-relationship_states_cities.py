#!/usr/bin/python3
"""
  New City
"""
from model_state import Base
from relationship_city import City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine("mysql+lysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
