#!/usr/bin/python3
""" This Model lists all City objects from
the database hbtn_0e_101_usa. """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State

if __name__ == "__main__":
    url = "mysql://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for c in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(c.id, c.name, c.state.name))
