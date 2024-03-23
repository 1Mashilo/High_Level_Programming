#!usr/bin/python3

"""
This module provides the SQLAlchemy model definition for representing states within
a database. It includes the 'State' class.
"""

from sqlalchemy import Column, Integer, String, Identity
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)
class State(Base):
    """
    A class to represent states within a database.

    Attributes:
        id (int): The unique identifier for the state.
        name (str): The name of the state.
    """
    __tablename__ = "state"
    id = Column(Integer,unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)