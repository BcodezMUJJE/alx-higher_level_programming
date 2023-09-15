#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def get_first_state(username, password, database_name):
    """Prints the first State object from the database hbtn_0e_6_usa"""

    # Create the SQLAlchemy engine
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}")

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first State object based on states.id
    first_state = session.query(State).order_by(State.id).first()

    # Display the result or "Nothing" if the table is empty
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    get_first_state(username, password, database_name)
