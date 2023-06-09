from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
from faker import Faker

from models import Flight, Passenger, Reservation



engine = create_engine('sqlite:///trip.db')
Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()

reservation_dict = {}

def retrieve_reservation(input):
    ref_code = text(input)
    
    reservation = session.query(Reservation).filter(Reservation.reference_code.like(f'%{ref_code}%')).first()
    if reservation:
        reservation_dict['reference_code'] = reservation.reference_code
        reservation_dict['passenger'] = reservation.passenger
        reservation_dict['flight'] = reservation.flight

    return reservation
    

def view_my_info(name):
    
    print(reservation_dict['passenger'])
    

def edit_my_info(name, edits):
    
    for passenger in session.query(Passenger).filter_by(name = name).all():
        passenger.name = edits[0]
        passenger.age = edits [1]
        passenger.budget = edits [2]
    session.commit()

    return passenger


def cancel_reservation(reference):
    reservation = session.query(Reservation).filter_by(reference_code= reference).first()
    session.delete(reservation)
    session.commit()

def fetch_flights(city):
    flights_with_city = session.query(Flight).filter_by(departure_city = city).all()
    return flights_with_city


    
def book_flight(flight_number, name, age, budget):
    # something is wrong here...it's making 4 new reservations. It only makes one new passenger though if the passenger doesn't already exist.
    
    passenger = session.query(Passenger).filter_by(name = name).first()
    if passenger:
        
        new_res = Reservation(reference_code=f'{fake.color()}', passenger_id=f'{passenger.id}', flight_id = f'{flight_number}')
        session.add(new_res)
        session.commit()
        
        return new_res
    else:
        
        new_passenger = Passenger(name=f'{name}', age = f'{age}', budget= f'{budget}')
        session.add(new_passenger)
        session.commit()
        new_res = Reservation(reference_code=f'{fake.color()}', passenger_id=f'{new_passenger.id}', flight_id = f'{flight_number}')
        session.add(new_res)
        session.commit()
        
        return new_res

def change_flight(reference, flight_id):

    for reservation in session.query(Reservation).filter_by(reference_code = reference).all():
        reservation.flight_id = flight_id
    session.commit()

    return reservation

