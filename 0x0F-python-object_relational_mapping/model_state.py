#!/usr/bin/python3
"""
  Model Module
"""
import MySQLdb
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
# from sqlalchemy import (create_engine)


Base = declarative_base()


class State(Base):
    """
      State class
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


# engine = create_engine('mysql+mysqldb://root:root@localhost/hbtn_0e_6_usa')
