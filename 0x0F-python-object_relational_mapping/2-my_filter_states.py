#!/usr/bin/python3
import MySQLdb
import sys

def search_states(username, password, database_name, state_name):
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

        # Use format to create the SQL query with the user input
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        # Fetch all the rows as a list of tuples
        states = cursor.fetchall()

        # Display the results
        for state in states:
            print(state)

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
    search_states(username, password, database_name, state_name)
