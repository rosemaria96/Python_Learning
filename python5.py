class Hotel:
    def __init__(self):
        self.rooms = {101: None, 102: None, 103: None, 104: None, 105: None}

    def display_rooms(self):
        print("\nRoom Status:")
        for room, customer in self.rooms.items():
            status = "Available" if customer is None else f"Booked by {customer['name']}"
            print(f"Room {room}: {status}")

    def book_room(self):
        try:
            room_number = int(input("Enter room number to book: "))
            if room_number in self.rooms:
                if self.rooms[room_number] is None:
                    name = input("Enter customer name: ")
                    phone = input("Enter phone number: ")
                    self.rooms[room_number] = {'name': name, 'phone': phone}
                    print(f"Room {room_number} successfully booked for {name}.")
                else:
                    print("Room already booked.")
            else:
                print("Invalid room number.")
        except ValueError:
            print("Invalid input. Please enter a valid room number.")

    def view_customer(self):
        try:
            room_number = int(input("Enter room number to view customer details: "))
            customer = self.rooms.get(room_number)
            if customer:
                print(f"\nRoom {room_number} is booked by:")
                print(f"Name: {customer['name']}")
                print(f"Phone: {customer['phone']}")
            else:
                print("Room is not booked.")
        except ValueError:
            print("Invalid input. Please enter a valid room number.")

    def checkout(self):
        try:
            room_number = int(input("Enter room number to check out: "))
            if room_number in self.rooms and self.rooms[room_number] is not None:
                print(f"{self.rooms[room_number]['name']} has checked out from Room {room_number}.")
                self.rooms[room_number] = None
            else:
                print("Room is already vacant or invalid.")
        except ValueError:
            print("Invalid input.")

def main():
    hotel = Hotel()
    while True:
        print("\n--- Hotel Management Menu ---")
        print("1. Display Room Status")
        print("2. Book a Room")
        print("3. View Customer Details")
        print("4. Check-out")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            hotel.display_rooms()
        elif choice == '2':
            hotel.book_room()
        elif choice == '3':
            hotel.view_customer()
        elif choice == '4':
            hotel.checkout()
        elif choice == '5':
            print("Thank you for using Hotel Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
