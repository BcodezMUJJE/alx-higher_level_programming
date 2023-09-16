#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def add_louisiana_to_database(username, password, database_name):
    # Create a connection to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}')
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    # Create a new State object for Louisiana
    louisiana = State(name="Louisiana")
    # Add the Louisiana object to the database
    session.add(louisiana)
    session.commit()
    # Print the new state's id
    print(f"New state '{louisiana.name}' added with id: {louisiana.id}")
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    add_louisiana_to_database(username, password, database_name)
