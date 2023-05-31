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
    
def show_menu():
    print('What actions would you like to take today?')
    menu = input('"view my info", "view my flight info", "change my flight", "cancel my flight", or "exit": ')
    return menu

def view_my_info(name):
    my_info = session.query(Passenger).filter(Passenger.name.like(f'%{name}%')).first()
    print( my_info)
    # option_to_edit = input('Would you like to edit your info? y/n: ')
    # return option_to_edit

def edit_my_info():
    edit = input('Name, Age, Budget :')
    return edit

def update_my_info(personal_info):
    # do something to update the db with the new personal_info
    pass

def update_message():
    print('Here is your updated info:')
    view_my_info()
    confirm_edited_info= input('Is this correct? y/n')
    return confirm_edited_info
