#!/usr/bin/python3
"""Takes a state name argument and displays matching states from
the database hbtn_0e_0_usa."""

import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Database Connection
    try:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=username,
                             passwd=password,
                             db=db_name)
        cursor = db.cursor()

        # Execute SQL query (Safe input handling)
        sql_query = ("SELECT id, name FROM states "
                     "WHERE name = %s ORDER BY id ASC")

        cursor.execute(sql_query, (state_name,))  # Parameterized query
        results = cursor.fetchall()

        # Print Results
        if not results:  # Check if any results were found
            print("Not found")
        else:
            for row in results:
                print(f"{row[0]}: {row[1]}")

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        # Close database connections
        if cursor:
            cursor.close()
        if db:
            db.close()
