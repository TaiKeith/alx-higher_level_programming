#!/usr/bin/python3
"""
This script prints the first State object from the database hbtn_0e_4_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and retrieve the frirst State object only
    """
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
