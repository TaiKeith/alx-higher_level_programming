#!/usr/bin/python3
"""
This script lists all State and corresponding City Objects
from the database hbtn_0e_100_usa
"""

import sys
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and retrieves all State and corresponding City objects
    """
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")
