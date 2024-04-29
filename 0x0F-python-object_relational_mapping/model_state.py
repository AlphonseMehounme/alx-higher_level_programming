"""
  Model Module
"""
import SQLAlchemy
import MySQLdb
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer)
    name = Column(String(128))
