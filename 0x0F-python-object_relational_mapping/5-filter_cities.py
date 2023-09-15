#!/usr/bin/python3
"""
5-filter_cities - this displays all cities for the state
that matches the search argument from table `hbtn_0e_0_usa`.
"""
import MySQLdb
import sys

def list_cities_by_state(username, password, database_name, state_name):
    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )
        # Create a cursor object to interact with the database
        cursor = connection.cursor()
        # Define the SQL query with a parameterized query
        query = "SELECT cities.id, cities.name, states.name FROM cities \
                 INNER JOIN states ON cities.state_id = states.id \
                 WHERE states.name = %s ORDER BY cities.id ASC"
        # Execute the SQL query with the state_name as a parameter
        cursor.execute(query, (state_name,))
        # Fetch all the rows as a list of tuples
        cities = cursor.fetchall()
        # Display the results
        for city in cities:
            print(city)
        # Close the cursor and the connection
        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database_name> <state_name>")
        sys.exit(1)

    username, password, database_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    list_cities_by_state(username, password, database_name, state_name)
