#!/usr/bin/python3
"""
This file contains the class definition of a State and an instance
Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


"""Create an instance"""
Base = declarative_base()


class State(Base):
    """
    Defines a State class that inherits from Base and links
    to the MySQL table states
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return f"<State(id={self.id}, name={self.name})>"
