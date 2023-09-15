#!/usr/bin/python3
"""
model_state.py - this defines a class `State` and an instance
`Base` of declarative_base from SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_city import City
from model_base import Base


class State(Base):
    """State class inherits from Base"""

    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column('name', String(128), nullable=False)

    # `backpopulate` points to the `state` attrubite on the `City` class
    cities = relationship('City', order_by=City.id, back_populates='state')
