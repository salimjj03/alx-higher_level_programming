#!/usr/bin/python3
""" This Module prints the first State object
from the database hbtn_0e_6_usa. """


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    url = "mysql://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
    engine = create_engine(url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    newState = State()
    newState.name = "Louisiana"

    session.add(newState)
    session.commit()
    print(newState.id)
