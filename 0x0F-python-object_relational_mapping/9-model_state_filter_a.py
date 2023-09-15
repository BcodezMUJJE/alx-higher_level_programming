#!/usr/bin/python3
"""Lists all State objects containing the letter 'a' from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_states_with_letter_a(username, password, database_name):
    """Lists all State objects containing the letter 'a' from the database hbtn_0e_6_usa"""
    # Create the SQLAlchemy engine
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}")
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query State objects that contain the letter 'a' and sort by states.id
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    # Display the results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")
    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states_with_letter_a(username, password, database_name)
