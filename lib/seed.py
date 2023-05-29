from faker import Faker
import random
from random import choice as rc

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import  Flight


engine = create_engine('sqlite:///trip.db')
Session = sessionmaker(bind=engine)
session = Session()

def delete_records():
    session.query(Flight).delete()
    # session.query(Passenger).delete()
    # session.query(Plane).delete()
    session.commit()


fake = Faker()

dep_cities = [
    'Denver', 'Houston', 'San Francisco', 'Portland', 'Boston',
        'Chicago', 'Miami', 'Nashville', 'Phoenix', 'Des Moines', 'San Diego', 'Rio de Janeiro', 'Toronto', 'Mexico City', 'Dublin', 'Phuket', 'Rome', 'Brisbane', 'Auckland', 'Edmonton', 'Juneau', 'Honolulu'
]
arr_cities = [
    'Los Angeles', 'Anchorage', 'Dallas', 'Salt Lake City', 'Seattle',
    'Detroit', 'Charleston', 'St. Louis', 'Kansas City', 'Omaha', 'London', 'Tel Aviv', 'Amsterdam', 'Nairobi', 'Bogota', 'Sydney', 'Brussels', 'Paris', 'Tokyo', 'Beijing', 'Rabat', 'Istanbul', 'Beirut', 'Mumbai'
]
plane_types = ['737', '757', '787', 'A321']

def create_records():
    flights = [
        Flight(
            departure_city=random.choice(dep_cities),
            arrival_city=random.choice(arr_cities),
        ) for i in range(50)
    ]
    session.add_all(flights)
    session.commit()
    return flights

if __name__ == '__main__':
    delete_records()
    flights = create_records()