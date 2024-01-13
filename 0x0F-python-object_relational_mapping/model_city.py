#!/usr/bin/python3
""" This is the base model for cities. """


from sqlalchemy import Column, Integer, ForeignKey, String
from model_state import State, Base


class City(Base):
    """ This is the Based cities class. """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
