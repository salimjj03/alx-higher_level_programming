#!/usr/bin/python3
""" This module lists all State objects from
the database hbtn_0e_6_usa. """


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


url = "mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3])
engine = create_engine(url, pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()

result = session.query(State).order_by(State.id)
for row in result:
    print("{}: {}".format(row.id, row.name))
