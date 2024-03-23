#!/usr/bin/python3

"""
This script establishes a connection to a MySQL database and retrieves data from the 'state' table using SQLAlchemy.

Usage:
    python3 script_name.py <username> <password> <database_name>

Arguments:
    username (str): The username for the MySQL database.
    password (str): The password for the MySQL database.
    database_name (str): The name of the MySQL database.

Example:
    python3 script_name.py root password my_database

Dependencies:
    - SQLAlchemy (Install using 'pip install sqlalchemy')

Description:
    This script connects to a MySQL database using SQLAlchemy and retrieves all records from the 'state' table.
    It then prints the ID and name of each state record retrieved from the database.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Extracting command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Establishing connection to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}')

    # Creating all tables defined in the Base class
    Base.metadata.create_all(engine)

    # Creating a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying all instances of the State class from the 'state' table and printing their ID and name
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
