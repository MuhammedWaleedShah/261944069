flight = [
    {'Name': 'QatarAirlines', 'Departure': '9:00', 'Arrival': '2:00'},
    {'Name': 'PIA', 'Departure': '6:00', 'Arrival': '10:00'}  #list of dictionaryy that contains the time name of flights
]

seatsPIA = [['O' for _ in range(9)] for _ in range(5)]
seatsQatarAirlines = [['O' for _ in range(9)] for _ in range(5)]

def display_seats(seats):
    print('           A    B    C    D    E    F    G    H    I')
    row_number = 1
    for row in seats:
        print('Row', row_number, end='   ')
        for seat in row:
            print(seat, end='    ')
        print()
        row_number += 1
#this function is used to display seat arrangment and make a formation vsible to user
def display_seats_PIA():
    print("           PIA seats      ")
    display_seats(seatsPIA)

def display_seats_QatarAirlines():
    print("           QatarAirlines seats      ")
    display_seats(seatsQatarAirlines)

def addDictionary(name, departure, arrival):
    new = {'Name': name, 'Departure': departure, 'Arrival': arrival}
    with open("DictionaryFlights.txt", "a") as f:
        f.write(str(new) + "\n")
#adddictionary will allow me to write in the txt file
def load_flight_data():
    try:
        with open("DictionaryFlights.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                flight_data = eval(line.strip()) 
                flight.append(flight_data)
    except FileNotFoundError:
        pass
def book_ticket():
    print('1.PIA\n2.QatarAirways')
    inp2 = input('Choose what you want to do: ')
    
    if inp2 not in '12':
        print('Invalid input')
        return

    if inp2 == '1':
        display_seats_PIA()
        flight_index = 0  
    elif inp2 == '2':
        display_seats_QatarAirlines()
        flight_index = 1  
    else:
        print('Invalid input')
        return

    row = int(input('Enter Row(1,2,3...): '))
    if row not in range(1, 6):
        print('Incorrect Row')
        return

    column = input('Enter Seat Alphabet: ')
    if column not in 'abcdefghiABCDEFGHI':
        print('Invalid Seat')
        return

    if inp2 == '1':
        o = seatsPIA[row - 1]
    elif inp2 == '2':
        o = seatsQatarAirlines[row - 1]

    if o[ord(column.upper()) - ord('A')] == 'X':
        print('Seat already booked')
        return

    o[ord(column.upper()) - ord('A')] = 'X'
    passenger_name = input('Enter Name of passenger: ')

    with open('SEAT_BOOKINGS.txt', 'a') as f:
        f.write(f"{passenger_name} {flight[flight_index]['Name']} Row {row} Seat {column}\n")

    print('Your flight has been booked')

def cancel_booking():
    global flight_index  # Add this line to use the global variable
    print('~~~~~~~~~~~~~~~ Cancel BOOKING ~~~~~~~~~~~~~~')
    print('Available flights:\n1.PIA\n2.QatarAirways\n')

    inp2 = input('Choose what you want to do: ')
    if inp2 not in '12':
        print('Invalid input')
        return

    if inp2 == '1':
        display_seats_PIA()
        flight_index = 0
    elif inp2 == '2':
        display_seats_QatarAirlines()
        flight_index = 1
    else:
        print('Invalid input')
        return

    row = int(input('Enter Row(1,2,3...): '))
    if row not in range(1, 6):
        print('Incorrect Row')
        return

    column = input('Enter Seat Alphabet: ')
    if column not in 'abcdefghiABCDEFGHI':
        print('Invalid Seat')
        return

    if inp2 == '1':
        o = seatsPIA[row - 1]
    elif inp2 == '2':
        o = seatsQatarAirlines[row - 1]

    if o[ord(column.upper()) - ord('A')] == 'O':
        print('Seat is not booked')
        return

    o[ord(column.upper()) - ord('A')] = 'O'
    passenger_name = input('Enter Name of passenger: ')

    with open('SEAT_BOOKINGS.txt', 'r') as f:
        lines = f.readlines()

    with open('SEAT_BOOKINGS.txt', 'w') as f:
        for line in lines:
            if passenger_name not in line or f"{flight[flight_index]['Name']} Row {row} Seat {column}" not in line:
                f.write(line)

    print('Booking has been canceled')

def admin_interface():
    print('You have been verified as an admin')
    print('1.View Flights\n2.Add a flight\n3.Remove a flight\n4.Modify a flight\n5.Main')

    inp1 = input('Choose(1,2,3,4,5)? ')

    if inp1 == '5':
        return

    elif inp1 == '1':
        for f in flight:
            print('Name: ', f['Name'])
            print('Departure: ', f['Departure'])
            print('Arrival: ', f['Arrival'])
            print('==============================================')
        admin_interface()

    elif inp1 == '2':
        add_flight()
        admin_interface()

    elif inp1 == '3':
        remove_flight()
        admin_interface()

    elif inp1 == '4':
        modify_flight()
        admin_interface()

    else:
        print('Invalid Entry')
        admin_interface()

def add_flight():
    name = input('Enter Flight name: ')
    departure = input("Enter the time of departure: ")
    arrival = input('Enter the time of arrival: ')
    
    new_flight = {"Name": name, "Departure": departure, "Arrival": arrival}
    flight.append(new_flight)

    with open('DictionaryFlights.txt', 'a') as f:
        f.write(str(new_flight) + "\n")

    print('Flight has been added')

def remove_flight():
    name = input('Enter Name of flight to remove: ')
    for f in flight:
        if f['Name'] == name:
            flight.remove(f)
    with open('DictionaryFlights.txt', 'r') as f:
        lines = f.readlines()
    with open('DictionaryFlights.txt', 'w') as f:
        for line in lines:
            if name not in line:
                f.write(line)
    print('The flight has been removed')

def modify_flight():
    for i, f in enumerate(flight, 1):
        print(i, '.', f['Name'])

    inp = input('Choose Flight to modify(1,2,3...)? ')
    if inp in '1234567890':
        airplane_index = int(inp) - 1
        selected_flight = flight[airplane_index]
        print('1. Name')
        print('2. Departure Time')
        print('3. Arrival Time')
        print('4. Change Seat Layout')
        choice = input('Choose (1,2,3,4): ')

        if choice == '1':
            new_name = input('Enter new flight name: ')
            selected_flight['Name'] = new_name
            with open('DictionaryFlights.txt', 'r') as f:
                lines = f.readlines()
            with open('DictionaryFlights.txt', 'w') as f:
                for line in lines:
                    if selected_flight['Name'] not in line:
                        f.write(line)
                f.write(str(selected_flight) + '\n')

        elif choice == '2':
            new_departure = input('Enter new departure time: ')
            selected_flight['Departure'] = new_departure
            with open('DictionaryFlights.txt', 'r') as f:
                lines = f.readlines()
            with open('DictionaryFlights.txt', 'w') as f:
                for line in lines:
                    if selected_flight['Name'] not in line:
                        f.write(line)
                f.write(str(selected_flight) + '\n')

        elif choice == '3':
            new_arrival = input('Enter new arrival time: ')
            selected_flight['Arrival'] = new_arrival
            with open('DictionaryFlights.txt', 'r') as f:
                lines = f.readlines()
            with open('DictionaryFlights.txt', 'w') as f:
                for line in lines:
                    if selected_flight['Name'] not in line:
                        f.write(line)
                f.write(str(selected_flight) + '\n')

        elif choice == '4':
            print('Seat Layout:')
            if airplane_index == 0:
                display_seats_PIA()
                update_seat_layout(seatsPIA, airplane_index)
            elif airplane_index == 1:
                display_seats_QatarAirlines()
                update_seat_layout(seatsQatarAirlines, airplane_index)
        else:
            print('Invalid Input')

def update_seat_layout(seats, airplane_index):
    for i in range(len(seats)):
        row_str = input(f'Enter updated seats for Row {i + 1} (O for available, X for booked): ')
        if len(row_str) == 9:
            seats[i] = list(row_str.upper())
        else:
            print('Invalid input. Please enter 9 characters (O for available, X for booked).')
            update_seat_layout(seats, airplane_index)

def user_interface():
    print('------------------------')
    print('1.Show Flights\n2.Book Ticket\n3.Cancel Booking\n4.Back to Login')
    inp1 = input('Choose: ')

    if inp1 == '1':
        for f in flight:
            print('Name: ', f['Name'])
            print('Departure: ', f['Departure'])
            print('Arrival: ', f['Arrival'])
            print('--------------------')

        display_seats_PIA()
        print('-----------------------------')
        display_seats_QatarAirlines()
        user_interface()

    elif inp1 == '2':
        book_ticket()

    elif inp1 == '3':
        cancel_booking()

    elif inp1 == '4':
        main()

def main():
    load_flight_data()
    print('Welcome to Flight Booking System')
    
    while True:
        print('Enter user & password: ')
        inp1 = input('Enter Username: ')
        inp2 = input('Enter Password: ')
        
        if inp1 == 'user' and inp2 == 'user123':
            user_interface()
        elif inp1 == 'admin' and inp2 == 'admin123':
            admin_interface()
        else:
            print('Invalid user or password')

if __name__ == "__main__":
    main()
