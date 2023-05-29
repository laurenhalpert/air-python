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
            plane_type=random.choice(plane_types),
            cost = random.randint(49, 1500)
        ) for i in range(50)
    ]
    # planes = [
    #     Plane(
    #         plane_type = random.choice(plane_types),
    #         passenger_limit = random.randint(120, 300),
    #         flight_id = random.randint(1,50)
    #     ) for i in range(50)
    # ]
    # passengers =[
    #     Passenger(
    #         passenger_name = fake.unique.name(),
    #         passenger_age = random.randint(15,90),
    #         plane_id = random.randint(1, 50)
    #     ) for i in range (3000)
    # ]
    session.add_all(flights)
    session.commit()
    return flights

# def relate_records(flights, planes, passengers):
#     for plane in planes:
#         plane.flight = rc(flights)

#     for passenger in passengers:
#         passenger.plane = rc(planes)

#     session.add_all(planes + passengers)
#     session.commit()

if __name__ == '__main__':
    delete_records()
    flights = create_records()
    # relate_records(flights, planes, passengers)