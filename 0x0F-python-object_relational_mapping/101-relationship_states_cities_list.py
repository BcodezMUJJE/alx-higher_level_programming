#!/usr/bin/python3
"""
Link class to table in database
"""

import sys
from sqlalchemy import create_engine
from model_base import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import joinedload
from relationship_city import City
from relationship_state import State

if __name__ == "__main__":
    av = sys.argv

    user = av[1]
    passwd = av[2]
    db = av[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            user, passwd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).options(
            joinedload(State.cities)).order_by(State.id)

    for state in states:
        print("{}: {}".format(state.id, state.name))

        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

        session.close()
