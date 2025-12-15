import os
import pickle


class Booking:
    """One booking record"""

    def __init__(self):
        self.room_id = ""
        self.room_name = ""
        self.customer_id = ""
        self.customer_name = ""
        self.customer_email = ""
        self.customer_address = ""
        self.customer_phone = ""

    def add_customer(self):
        self.room_id = input("Enter room ID: ")
        self.room_name = input("Enter room name [Standard, Deluxe, Suite]: ")
        self.customer_id = input("Enter your customer ID: ")
        self.customer_name = input("Enter your customer name: ")
        self.customer_email = input("Enter your customer email: ")
        self.customer_address = input("Enter your customer address: ")
        self.customer_phone = input("Enter your customer phone number: ")


class BookingSystem:
    """Handles all bookings"""

    def view_all_bookings(self, bookings):
        if not bookings:
            print("\nNo bookings found.")
            return

        print("\n=== All Bookings ===")
        for i, b in enumerate(bookings, 1):
            print(f"\nBooking {i}:")
            print(f" Room ID: {b.room_id}")
            print(f" Room Name: {b.room_name}")
            print(f" Customer ID: {b.customer_id}")
            print(f" Customer Name: {b.customer_name}")
            print(f" Email: {b.customer_email}")
            print(f" Address: {b.customer_address}")
            print(f" Phone: {b.customer_phone}")


# =======================================================
# Pickle functions

FILENAME = "pickle_data.pkl"

def save(bookings):
    with open(FILENAME, "wb") as f:
        pickle.dump(bookings, f)

def load():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "rb") as f:
            return pickle.load(f)
    except EOFError:
        return []

# =======================================================
# Load data & initialize system
bookings = load()
system = BookingSystem()

# =======================================================
# MAIN MENU

while True:
    print("\n------------------------------------")
    print("Hotel Booking Application")
    print("1. Add a new booking")
    print("2. View all bookings")
    print("3. Exit")
    print("------------------------------------")

    try:
        option = int(input("Enter your choice: "))
        if option == 1:
            booking = Booking()
            booking.add_customer()
            bookings.append(booking)
            save(bookings)
            print("\nBooking added successfully!")

        elif option == 2:
            system.view_all_bookings(bookings)

        elif option == 3:
            print("You've stopped the program!")
            break

        else:
            print("Invalid option. Please try again.")

    except ValueError:
        print("Please enter a valid number.")
