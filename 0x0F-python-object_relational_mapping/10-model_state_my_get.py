#!/usr/bin/python3
"""Prints the State object with the specified name from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def find_state_by_name(username, password, database_name, state_name):
    """Prints the State object with the specified name from the database hbtn_0e_6_usa"""

    # Create the SQLAlchemy engine
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}")

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with the specified name
    found_state = session.query(State).filter_by(name=state_name).first()

    # Display the result or "Not found" if not found
    if found_state:
        print(found_state.id)
    else:
        print("Not found")

    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database_name> <state_name>")
        sys.exit(1)

    username, password, database_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    find_state_by_name(username, password, database_name, state_name)
