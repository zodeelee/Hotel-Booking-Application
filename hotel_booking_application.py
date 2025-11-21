class Booking:  # one booking record
    def __init__(self):
        self.r_id = ""
        self.r_name = ""
        self.customer_id = ""
        self.customer_name = ""
        self.customer_email = ""
        self.customer_address = ""
        self.customer_phone = ""

    def add_customer(self):
        self.r_id = input("Enter room ID: ")
        self.r_name = input("Enter room name[Standard,Deluxe,Suite]: ")
        self.customer_id = input("Enter your customer ID: ")
        self.customer_name = input("Enter your customer name: ")
        self.customer_email = input("Enter your customer email: ")
        self.customer_address = input("Enter your customer address: ")
        self.customer_phone = input("Enter your customer number: ")


class BookingSystem:  #all bookings will be stored here
    def __init__(self):
        self.bookings = []

    def add_booking(self, booking):
        self.bookings.append(booking)

    def view_all_bookings(self):
        if not self.bookings:
            print("\nNo bookings found.")
            return

        print("\n=== All Bookings ===")
        for i, b in enumerate(self.bookings, 1):
            print(f"\nBooking {i}:")
            print(f" Room ID: {b.r_id}")
            print(f" Room Name: {b.r_name}")
            print(f" Customer ID: {b.customer_id}")
            print(f" Customer Name: {b.customer_name}")
            print(f" Email: {b.customer_email}")
            print(f" Address: {b.customer_address}")
            print(f" Phone: {b.customer_phone}")


# =======================================================
# storing system
system = BookingSystem()



# =======================================================
# MAIN MENU

while True:
    print("\n------------------------------------")
    print("Hotel Booking Application")
    print("1. [Add a new booking]")
    print("2. [View all bookings]")
    print("3. [Exit]")
    print("------------------------------------")

    option = int(input("Enter your choice: "))

    if option == 1:
        booking = Booking()
        booking.add_customer()
        system.add_booking(booking)
        print("Booking adduced successfully!")

    if option == 2:
        system.view_all_bookings()
        print("All booking's viewed succesfully!")

    if option == 3:
        print("You've stopped the program!")
        break


#streamlit page

    #import streamlit as st
    from PIL import Image

    #col1, col2 = st.columns(2)


