#!/usr/bin/env python3

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
import random
from faker import Faker

from models import  Flight, Reservation, Passenger
fake = Faker()
if __name__ == '__main__':


    engine = create_engine('sqlite:///trip.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    import ipdb; ipdb.set_trace()