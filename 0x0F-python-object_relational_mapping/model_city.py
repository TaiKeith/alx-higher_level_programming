#!/usr/bin/python3
"""
This file contains the class definition of a City that inherits
from Base imported from model_state
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    Defines a City class that inherits from Base and links
    to the MySQL table cities
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
