#!/usr/bin/python3
"""Takes a state name argument and displays matching states from
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

    # Execute SQL query (Safe input handling)
    sql_query = ("SELECT * FROM states WHERE name BINARY '{}'"
                 .format(sys.argv[4]))

    cursor.execute(sql_query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
