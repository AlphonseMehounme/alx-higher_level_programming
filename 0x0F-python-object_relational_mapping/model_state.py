#!/usr/bin/python3
"""
  Model Module
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


# Base class
Base = declarative_base()

class State(Base):
    """
      State class
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
