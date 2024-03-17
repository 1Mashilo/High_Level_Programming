#!/usr/bin/python3
"""Takes a state name argument and displays matching states from
the database hbtn_0e_0_usa."""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[1],
                         db=sys.argv[1])
    cursor = db.cursor()

    sql_query = ("SELECT * FROM states WHERE name BINARY '{}'"
                 .format(sys.argv[4]))

    cursor.execute(sql_query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
