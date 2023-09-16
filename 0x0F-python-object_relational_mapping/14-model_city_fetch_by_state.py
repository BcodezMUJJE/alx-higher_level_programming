#!/usr/bin/python3
"""a Python file similar to model_state.py named model_city.py that contains the class definition of a City."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

def fetch_cities_by_state(username, password, database_name):
    # Create a connection to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}')
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query and print all City objects ordered by city id
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python 14-model_city_fetch_by_state.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    fetch_cities_by_state(username, password, database_name)
