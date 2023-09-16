#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City

def list_cities(username, password, database_name):
    # Create a database connection
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database to retrieve City objects
    cities = session.query(City).join(State).order_by(City.id).all()

    # Print the results
    for city in cities:
        print(f'{city.id}: {city.name} ({city.state.name})')

    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_cities(username, password, database_name)
