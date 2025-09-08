#!/usr/bin/python3
"""
Displays all values in the states table where name matches the user input
"""

import sys
import MySQLdb


if __name__ == "__main__":
    # Get login credentials and arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor
    cursor = db.cursor()

    # Build query using format() (deliberately vulnerable to SQL injection)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    # Execute query
    cursor.execute(query)
     
    # Fetch all results
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close connection
    cursor.close()
    db.close()

