#!/usr/bin/python3
"""
This script lists all State objects that contain letter a
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

    for instance in session.query(State).order_by(State.id).filter(
            State.name.ilike('%a%')):
        print(f"{instance.id}: {instance.name}")
