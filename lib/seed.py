from faker import Faker
import random
from random import choice as rc

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import  Flight, Passenger, Reservation


engine = create_engine('sqlite:///trip.db')
Session = sessionmaker(bind=engine)
session = Session()

def delete_records():
    session.query(Flight).delete()
    session.query(Passenger).delete()
    session.query(Reservation).delete()
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
        ) for i in range(300)
    ]
    reservations = [
        Reservation(
            reference_code = fake.unique.word(),
            passenger_id = random.randint(0, 500),
            flight_id = random.randint(1,301)
        ) for i in range(900)
    ]
    passengers =[
        Passenger(
            name = fake.unique.name(),
            age = random.randint(15,90),
            budget = random.randint(50, 2000)
        ) for i in range (800)
    ]
    session.add_all(flights + passengers + reservations)
    session.commit()
    return flights, passengers, reservations

def relate_records(flights, passengers, reservations):
    for reservation in reservations:
        reservation.flight = rc(flights)
        reservation.passenger = rc(passengers)

   

    session.add_all(flights + passengers + reservations)
    session.commit()

if __name__ == '__main__':
    delete_records()
    flights, passengers, reservations = create_records()
    relate_records(flights, passengers, reservations)