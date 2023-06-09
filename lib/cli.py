#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from seed import dep_cities
from models import Flight, Passenger, Reservation
from helpers import (
    retrieve_reservation,
    view_my_info,
    edit_my_info,
    cancel_reservation,
    fetch_flights,
    book_flight,
    change_flight
)

engine = create_engine('sqlite:///trip.db')
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    
    def menu_loop():
        print('What actions would you like to take today?')
        menu = input('"view my info", "manage my flight", "new reservation", or "exit": ')
        print('')
        if menu == 'exit':
            print('Thanks for visiting!')
        elif menu == 'view my info':
            print('Here is your info: ')
            view_my_info (retrieve_reservation(reference).passenger.name)
            edit_choice = input('Would you like to make any changes to your info? y/n : ')
            if edit_choice == 'n':
                print('')
                menu_loop()
            elif edit_choice == 'y':
                print('')
                edits = []
                edits_name = input('Name : ')
                edits.append(edits_name)
                edits_age = input('Age : ')
                edits.append(edits_age)
                edits_budget = input('Budget : $')
                edits.append(edits_budget)
                print('')
                print('Here is your updated info: ')
                print(edit_my_info(retrieve_reservation(reference).passenger.name, edits))
                print('')
                menu_loop()
        elif menu == 'manage my flight':
            print('')
            print('Here is your current flight information for your reservation: ')

            for flight in retrieve_reservation(reference).passenger.flights:
                if flight.id == retrieve_reservation(reference).flight.id:
                    print(flight)
            print('')
            change_flight = input('Would you like to make changes to your flight? y/n : ')
            print('')
            if change_flight == 'y':
                change_or_cancel = input('What changes would you like to make? "change flight", "cancel flight", or "menu" : ')
                if change_or_cancel == 'change flight':
                    print('')
                    change_reservation()
                
                elif change_or_cancel == 'cancel flight':
                    print('')
                    cancel_reservation(reference)
                elif change_or_cancel == 'menu':
                    print('')
                    menu_loop()
            elif change_flight == 'n':
                print('')
                menu_loop()
        elif menu == 'new reservation':
            print('')
            make_reservation()
            
    def change_reservation():
        print('Let\'s get started!')
        print(set(dep_cities))
        choose_dep_city = input('Please choose a departure city from the list above: ')
        fetch_flights(choose_dep_city)
        print('')
        print(f'Here are the flights from {choose_dep_city}: {fetch_flights(choose_dep_city)}')
        choose_flight = input('Which of these flights would you like? Please enter the desired flight number. If none of these fit your needs, say "go back" to view flights from a different departure city, or say "menu". ')
        if choose_flight == 'go back':
            print('')
            make_reservation()
        elif choose_flight == 'menu':
            print('')
            menu_loop()
        else:
            print('')
            
            change_flight(reference, choose_flight)
            print('')
            print(f'Your reservation has been updated! Here is your reference code: {reference}')
            print('')
            res_tuple = (change_flight(reference, choose_flight).passenger, change_flight(reference, choose_flight).flight)
            print(f'Here is your reservation info: ')
            print(res_tuple)
            print('')
            print('Thanks for visiting!')

    def make_reservation():
        print('Let\'s get started!')
        print(set(dep_cities))
        choose_dep_city = input('Please choose a departure city from the list above: ')
        fetch_flights(choose_dep_city)
        print('')
        print(f'Here are the flights from {choose_dep_city}: {fetch_flights(choose_dep_city)}')
        choose_flight = input('Which of these flights would you like? Please enter the desired flight number. If none of these fit your needs, say "go back" to view flights from a different departure city, or say "menu". ')
        if choose_flight == 'go back':
            print('')
            make_reservation()
        elif choose_flight == 'menu':
            print('')
            menu_loop()
        else:
            print('')
            passenger_name = input('Passenger name: ')
            passenger_age = input('Passenger age: ')
            passenger_budget = input('Passenger budget: $')
        
            book_flight(choose_flight, passenger_name, passenger_age, passenger_budget)
            print('')
            print(f'You\'re booked! Here is your reference code: {book_flight(choose_flight, passenger_name, passenger_age, passenger_budget).reference_code}')
            print('')
            res_tuple = (book_flight(choose_flight, passenger_name, passenger_age, passenger_budget).passenger, book_flight(choose_flight, passenger_name, passenger_age, passenger_budget).flight)
            print(f'Here is your reservation info: ')
            print(res_tuple)
            print('')
            print('Thanks for visiting!')
            
    print("")
    reference = input('Please enter your reservation reference code: ')
    
    retrieve_reservation(reference)
    if retrieve_reservation(reference) == None:
        print("")
        print('Invalid reference code.')
        create_reservation = input('Would you like to make a flight reservation? y/n : ')
        if create_reservation == 'y':
            print("")
            make_reservation()
            
        else:
            print('Okay! Please keep us in mind for your next travel plans.')
    else:
        print("")
        print(f'Welcome! We\'ve found your reservation: {retrieve_reservation(reference)}.')
        menu_loop()       
