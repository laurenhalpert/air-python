#!/usr/bin/env python3
# class MyFlight:
#     def __init__(self, user_input):
#         self.value = user_input

# move to helpers.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from seed import dep_cities
from models import Flight, Passenger, Reservation
from helpers import (
    retrieve_reservation,
    view_my_info,
    edit_my_info,
    view_flight_info,
    cancel_reservation,
    fetch_flights,
    book_flight
)

engine = create_engine('sqlite:///trip.db')
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    # passenger_flights = []
    def menu_loop():
        print('What actions would you like to take today?')
        menu = input('"view my info", "manage my flight", "new reservation", or "exit": ')
        if menu == 'exit':
            print('Thanks for visiting!')
        elif menu == 'view my info':
            print('Here is your info: ')
            view_my_info (retrieve_reservation(reference).passenger.name)
            edit_choice = input('Would you like to make any changes to your info? y/n : ')
            if edit_choice == 'n':
                menu_loop()
            elif edit_choice == 'y':
                edits = []
                edits_name = input('Name : ')
                edits.append(edits_name)
                edits_age = input('Age : ')
                edits.append(edits_age)
                edits_budget = input('Budget : $')
                edits.append(edits_budget)
                print('Here is your updated info: ')
                print(edit_my_info(retrieve_reservation(reference).passenger.name, edits))
                menu_loop()
        elif menu == 'manage my flight':
            print('Here is your current flight information for your reservation: ')
    
            for flight in retrieve_reservation(reference).passenger.flights:
                if flight.id == retrieve_reservation(reference).flight.id:
                    print(flight)
            change_flight = input('Would you like to make changes to your flight? y/n : ')
            if change_flight == 'y':
                change_or_cancel = input('What changes would you like to make? "change flight", "cancel flight", or "menu" : ')
                if change_or_cancel == 'change flight':
                    # user can search flights
                    # update reservation record
                    pass
                elif change_or_cancel == 'cancel flight':
                    cancel_reservation(reference)
                elif change_or_cancel == 'menu':
                    menu_loop()
            elif change_flight == 'n':
                menu_loop()
        elif menu == 'new reservation':
            make_reservation()
            # create a reservation record

    

    def make_reservation():
        print('Let\'s get started!')
        print(set(dep_cities))
        choose_dep_city = input('Please choose a departure city from the list above: ')
        fetch_flights(choose_dep_city)
        print(f'Here are the flights from {choose_dep_city}: {fetch_flights(choose_dep_city)}')
        choose_flight = input('Which of these flights would you like? Please enter the desired flight number. If none of these fit your needs, say "go back" to view flights from a different departure city, or say "menu". ')
        if choose_flight == 'go back':
            make_reservation()
        elif choose_flight == 'menu':
            menu_loop()
        else:
            passenger_name = input('Passenger name: ')
            passenger_age = input('Passenger age: ')
            passenger_budget = input('Passenger budget: $')
            book_flight(choose_flight, passenger_name, passenger_age, passenger_budget)
            print(f'You\'re booked! Here is your reference code: {book_flight(choose_flight, passenger_name, passenger_age, passenger_budget)}')
            print(f'Here is your flight info: {session.query(Flight).filter_by(id= choose_flight).first()}')
            print('Thanks for visiting!')
            

    reference = input('Please enter your reservation reference code: ')
    # while name:
    #     passenger_flights.append(name)
        #  name = input('Please enter your name: ')
    retrieve_reservation(reference)
    if retrieve_reservation(reference) == None:
        print('Invalid reference code.')
        create_reservation = input('Would you like to make a flight reservation? y/n : ')
        if create_reservation == 'y':
            make_reservation()
            # print('Let\'s get started!')
            # print('Please enter the following details')
            # function to make a reservation
            # choose from existing flight records
            # flight must be in passenger's budget
            # if new passenger, create new passenger record
            # if current passenger, their flights and reservations should update
        else:
            print('Okay! Please keep us in mind for your next travel plans.')
    else:
        print(f'Welcome! We\'ve found your reservation: {retrieve_reservation(reference)}.')
        # print('What actions would you like to take today?')
        # menu = input('"view my info", "manage my flight", or "exit": ')
        # if menu == 'exit':
        #     print('Thanks for visiting!')
        # elif menu == 'view my info':
        #     print('Here is your info.')
        #     view_my_info (retrieve_reservation(reference).passenger.name)
        #     edit_choice = input('Would you like to make any changes to your info? y/n : ')
        #     if edit_choice == 'n':
        menu_loop()       

    # if retrieve_passenger_info(name):
    #     print(f'Hello, {name}.')
    #     print('What actions would you like to take today?')
    #     menu = input('"view my info", "manage my flight", or "exit": ')
    #     if menu == 'view my info':
    #         print('Here is your info: ')
    #         view_my_info(name)
    #         edit_choice = input('Would you like to edit your info? y/n : ')
    #         if edit_choice == 'y':
    #             edit = input('Name, Age :')
    #             print('Here is your updated info: ')
    #             view_my_info(name)
    #             print(f'Thanks for visiting {name}. Goodbye!')
    #         elif edit_choice == 'n':
    #             # menu = input('"view my info", "view my flight info", "change my flight", "cancel my flight", or "exit": ')
    #             # menu
    #             print(f'Thanks for visiting {name}. Goodbye!')
    #     elif menu == 'manage my flight':
    #         print('Here is your flight info: ')
    #         # pull up route info associated with their flight
    #         manage_options = input('Select an action: "change flight", "cancel flight", or "exit" : ')
    #         if manage_options == "change flight":
    #             print("Okay! Let's change your flight.")
    #             change_flight = input('new route details')
    #             # function to update route
    #             print('Here is your updated flight info: ')
    #             print(f'Thanks for visiting {name}. Goodbye!')
    #         elif manage_options == "cancel flight":
    #             print("We're sorry you won't be flying with us.")
    #             # function to delete flight reservation
    #             print("We have canceled your flight.")
    #             print(f'Thanks for visiting {name}. Goodbye!')
    #         elif manage_options == 'exit':
    #             print(f'Thanks for visiting, {name}. Goodbye!')
    #         pass
        
    #     elif menu == 'exit':
    #         print(f'Thanks for visiting {name}. Goodbye!')
    #     else:
    #         print('Sorry, that is not an option. Please select from the given options.')

    # if retrieve_passenger_info(name):
    #     print (f'Hello, {name}.')
    #     show_menu()
    #     if show_menu() == "view my info":
    #         view_my_info(name)
    #         if view_my_info(name) == 'y':
    #             edit_my_info()
    #             edited_info = edit_my_info()
    #             update_my_info(edited_info)
    #             update_message()
    #             if update_message() == 'y':
    #                 show_menu()
    #             elif update_message() == 'n':
    #                 edit_my_info()
    #                 edited_info = edit_my_info()
    #                 update_my_info(edited_info)
    #                 update_message()
    #         elif view_my_info(name) == 'n':
    #             show_menu()
        

    # else:
    #     print (f'It looks like there is no flight reservation under that name. Would you like to make a reservation?')
    # update_flight_report(passenger_flights)