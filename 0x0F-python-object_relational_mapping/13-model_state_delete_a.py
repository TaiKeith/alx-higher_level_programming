#!/usr/bin/python3
"""
This script deletes all State objects with a name containing letter 'a'
from the database hbtn_0e_4_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and deletes State objects with letter a
    """
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    to_delete = session.query(State).filter(State.name.ilike('%a%')).all()

    if to_delete:
        for state in to_delete:
            session.delete(state)
        session.commit()

    session.close()
