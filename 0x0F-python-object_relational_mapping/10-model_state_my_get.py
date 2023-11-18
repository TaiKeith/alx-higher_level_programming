#!/usr/bin/python3
"""
This script prints the State object with the name passed as argument
from the database hbtn_0e_4_usa
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

    state_search = sys.argv[4]
    result = session.query(State).filter(State.name == state_search).first()
    if result:
        print(result.id)
    else:
        print("Not found")
