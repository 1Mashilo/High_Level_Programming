#!/usr/bin/python3
"""Lists all states with names starting with N from
the database hbtn_0e_0_usa."""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Database Connection
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    cursor = db.cursor()

    # Execute SQL query (with filtering)
    cursor.execute("""SELECT * FROM states WHERE name
            LIKE BINARY 'N%' ORDER BY states.id""")
    results = cursor.fetchall()

    # Print Results
    for row in results:
        print(row)

    # Close database connections
    if cursor:
        cursor.close()
    if db:
        db.close()
