# Air Python

This command line interface allows a passenger to look up their flight reservation, view their personal info, manage their flight, or book a new reservation. 


## Usage Overview

-Start by running python cli.py

-Enter your reservation reference code (if you have one)

-if you don't have one, you will be given the option of booking a flight

-If you do have one, you'll be given the option of viewing your personal info, managing your flight, or creating a new reservation

-If you select 'view my info' you will be given the opportunity to edit your info

-If you select 'manage my flight', you will be given your current flight info and the option to make changes (if you opt to make changes, you can choose to either change your flight or cancel your flight)

-If you select 'new reservation', you will be prompted to choose a flight

## cli.py description

The script begins by prompting the user to enter a reference code. Next, the retrieve_reservation helper function is called, passing in the user input as an argument. 

### Reservation with the reference code the user input does not exist

If a reservation with the reference code the user input does not exist, they will be asked if they want to make a reservation. If they want to make a new reservation, the make_reservation() function will be called and the user will then be prompted to make some choices about their desired flight, resulting in a reservation being created. The make_reservation() function calls on some other helper functions to help complete its task. 

#### make_reservation()

The make_reservation() function prompts the user to choose a departure city from a set of departure cities. Their choice is then passed through the fetch_flights() helper function as an argument.

The user is then prompted to choose a flight departing from the selected departure city, or they have the option to go back and choose a different departure city, or to return to the menu.

##### user chose a flight

The user will be prompted to enter their name, age, and budget. THe book_flight() helper function is then called with the chosen flight number, their name, age, and budget as arguments. The user is then shown their new reservation with its details and is thanked for visiting.

##### user opted to go back

If a user opts to go back, the make_reservation() function is called and they are looped back to choosing a departure city.

##### user opted to go to the menu

The menu_loop() function will be called and the user will be brought to the menu.

### Reservation with the reference code the user input does exist

If a reservation with the reference code the user input does exist, they will be prompted to select an option from the menu by calling on menu_loop(). The function menu_loop() was created so that a user can loop back to the menu and make other choices if they desire. 

#### menu_loop()

From the menu, a user can opt to view their info, manage their flight, create a new reservation, or exit.

##### user opted to view their info

A user is shown their info thanks to the view_my_info() helper function. The user is then asked if they'd like to change their info.

###### user opts to change their info

If a user opts to change their info, they will be prompted to enter their name, age, and budget, which then get appended to an edits list. The edits list gets passed in as an argument to the edit_my_info() function, where changes are made to that particular user's record in the passengers table. The user is then taken back to the menu via the menu_loop() function.

###### user opts to keep their info the same

The user is taken back to the menu via the menu_loop() function.

##### user opted to manage their flight

A user is shown their current flight info and is then asked if they'd like to make any changes. 

###### a user opts to make changes to their flight

A user is asked if they'd like to change their flight, cancel their flight, or return to the menu.

If they change their flight, the change_reservation() function will be called, which executes similarly to the make_reservation() function except instead of creating a new reservation, we are updating the current reservation, so the reference_code and passenger_id will remain the same, but the flight_id will change. After changing their flight, the user will be thanked. 

If they cancel their flight, the cancel_reservation() helper function will be called and the current reservation record will be deleted. The user will receive a message notifying them that their flight reservation was canceled and will receive a goodbye message.

If they opt to return to the menu, the menu_loop() function will be called and they will be brought back to the menu. 

###### a user opts not to make changes to their flight

The menu_loop() function is called and the user is brought back to the menu.

##### a user opts to make a new reservation

The make_reservation() function is called. 

##### a user opts to exit

The user is thanked for visiting. 


## helpers.py description

The helper functions in helpers.py are there to make session.queries and create, update, read, or delete records from the database. 

### retrieve_reservation()

Returns a reservation with the same reference_code that the user input if it exists; if it doesn't exist, it returns None. A side effect of this function is populating the reservation_dict with the reference_code, passenger, and flight. The reservation_dict is later used by other functions for ease of access to relevant data.

### view_my_info()

Prints the value of reservation_dict's passenger key.

### edit_my_info()

Updates the passenger's record with new data given by the user. Returns the new passenger record.

###  cancel_reservation()

The reservation record with the matching reference_code will be deleted from the database.

### fetch_flights()

Returns flight records that depart from the given departure city. 

### book_flight()

If a record for the passenger currently exists, a new reservation record will be created. The new reservation will be returned. 

If a record for the passenger doesn't exist, a new passenger record and a new reservation record will be created. The new reservation will be returned.

### change_flight()

Updates the reservation record with the given reference_code to reflect the newly chosen flight. Returns the updated reservation.

## models.py description

### Reservation data model

The Reservation data model is a join of the Flight data model and the Passenger data model. 
The reservations table has columns for id, reference_code, passenger_id, and flight_id.

The passenger_id and flight_id are both foreign keys. 

### Flight data model

The flights table has columns for id, departure_city, arrival_city, plane_type, and cost.

The relationship() method is used to set up a relationship with reservations.
The relationship with passengers is set up using an association_proxy, relating passengers to a flight via the reservations table.

### Passenger data model

The passengers table has columns for id, name, age, and budget.

The relationship() method is used to set up a relationship with reservations.
The relationship with flights is set up using an association_proxy, relating flights to a passenger via the reservations table.

## seed.py description

Seed.py has three functions: delete_records(), create_records(), and relate_records().

### delete_records()

Ensures that no duplicate records are made and that when python seed.py is run, old records are deleted.

### create_records()

Creates records in each table. 

### relate_records()

Sets up the relationships between tables. 

## debug.py description

Debug.py is executed by running python debug.py and uses ipdb to create a sandbox to test code in. 

## GitHub URL

https://github.com/laurenhalpert/air-python

## Contributing

Not open to contributions at this time.