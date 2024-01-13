#!/usr/bin/python3
""" This prints all City objects from the
database hbtn_0e_14_usa. """


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City, Base
from model_state import State
from sys import argv


if __name__ == "__main__":
    url = "mysql://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
    engine = create_engine(url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City, State).filter(
            State.id == City.state_id).order_by(City.id)
    for r in result:
        print("{}: ({}) {}".format(
            r["State"].name, r["City"].id, r["City"].name))
