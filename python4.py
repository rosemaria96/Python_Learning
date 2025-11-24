class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class CoffeeShop:
    def __init__(self):
        self.menu = [
            Coffee("Espresso", 100),
            Coffee("Latte", 120),
            Coffee("Cappuccino", 140),
            Coffee("Americano", 110)
        ]
        self.order = []

    def show_menu(self):
        print("Welcome to Python Coffee Shop!")
        print("Menu:")
        for idx, coffee in enumerate(self.menu, start=1):
            print(f"{idx}. {coffee.name} - ₹{coffee.price}")

    def take_order(self):
        while True:
            self.show_menu()
            choice = input("Enter the number of the coffee to order (or 'q' to finish): ")
            if choice.lower() == 'q':
                break
            if choice.isdigit() and 1 <= int(choice) <= len(self.menu):
                self.order.append(self.menu[int(choice) - 1])
                print(f"{self.menu[int(choice) - 1].name} added to your order.\n")
            else:
                print("Invalid choice. Please try again.\n")

    def print_bill(self):
        if not self.order:
            print("No items ordered.")
            return
        print("\nYour Order:")
        total = 0
        for coffee in self.order:
            print(f"- {coffee.name} ₹{coffee.price}")
            total += coffee.price
        print(f"Total: ₹{total}")

# Run the app
shop = CoffeeShop()
shop.take_order()
shop.print_bill()