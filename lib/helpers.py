from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker

from models import Flight, Passenger, Reservation

# view my info
# view my flight info
# change my route
# cancel my flight
# transfer my flight to someone else


engine = create_engine('sqlite:///trip.db')
Session = sessionmaker(bind=engine)
session = Session()

def retrieve_reservation(input):
    ref_code = text(input)
    
    reservation = session.query(Reservation).filter(Reservation.reference_code.like(f'%{ref_code}%')).first()
    return reservation
    

def view_my_info(name):
    my_info = session.query(Passenger).filter(Passenger.name.like(f'%{name}%')).first()
    print( my_info)
    # option_to_edit = input('Would you like to edit your info? y/n: ')
    # return option_to_edit

def edit_my_info(name, edits):
    # session.query(Passenger).update({
    #     Passenger.name: edits[0],
    #     Passenger.age: edits[1],
    #     Passenger.budget: edits[2]
    # })
    # updated_my_info = session.query(Passenger).filter(Passenger.name.like(f'%{edits[0]}%')).first()
    # print(updated_my_info)
    for passenger in session.query(Passenger).filter(Passenger.name.like(f'%{name}%')).all():
        passenger.name = edits[0]
        passenger.age = edits [1]
        passenger.budget = edits [2]
    session.commit()

    return passenger

def view_flight_info(flights):
    print(flights[0].id)

def cancel_reservation(reference):
    reservation = session.query(Reservation).filter(Reservation.reference_code.like(f'%{reference}%')).first()
    session.delete(reservation)
    session.commit()
    
