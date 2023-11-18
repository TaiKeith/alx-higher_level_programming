#!/usr/bin/python3
"""
This script changes the name of a State object
to the database hbtn_0e_4_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and change the name of a State object
    """
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_id_to_change = 2
    new_state_name = "New Mexico"
    change = session.query(State).filter_by(id=state_id_to_change).first()

    if change:
        change.name = new_state_name
        session.commit()

    session.close()
