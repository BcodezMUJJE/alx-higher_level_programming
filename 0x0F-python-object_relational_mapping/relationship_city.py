#!/usr/bin/python3
"""model_city.py - this defines a class `City` and an instance
`Base` of declarative_base from SQLAlchemy.
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from model_base import Base

class City(Base):
    """city class inherits from Base"""

    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey('states.id'))

    # `backpopulate` points to the `cities` attrubite on the `State` class
    state = relationship('State', back_populates='cities')
