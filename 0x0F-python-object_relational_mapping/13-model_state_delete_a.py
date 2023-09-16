#!/usr/bin/python3
"""deletes all State objects with a name containing the letter a from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def delete_states_with_letter_a(username, password, database_name):
    # Create a connection to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}')
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query and delete all State objects with a name containing 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    if states_to_delete:
        for state in states_to_delete:
            session.delete(state)

        session.commit()
        print(f"Deleted {len(states_to_delete)} state(s) with 'a' in their names.")
    else:
        print("No states with 'a' in their names found in the database.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    delete_states_with_letter_a(username, password, database_name)
