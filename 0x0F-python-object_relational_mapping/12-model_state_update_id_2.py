#!/usr/bin/pytho3
"""changes the name of a State object from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def change_state_name(username, password, database_name):
    # Create a connection to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}')

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with id 2 and change its name to "New Mexico"
    state_to_change = session.query(State).filter_by(id=2).first()
    if state_to_change:
        state_to_change.name = "New Mexico"
        session.commit()
        print(f"State with id {state_to_change.id} renamed to '{state_to_change.name}'")
    else:
        print("State with id 2 not found in the database")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    change_state_name(username, password, database_name)
