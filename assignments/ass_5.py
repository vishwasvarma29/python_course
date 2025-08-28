from abc import ABC, abstractmethod

# Base Abstract Class
class Person(ABC):
    """Abstract base class representing a Blinkit customer (common attributes)."""

    def __init__(self, name, age, gender, contact_info, customer_id):
        self.name = name
        self.age = age
        self.gender = gender
        self.__contact_info = contact_info   # Private (Encapsulation)
        self.customer_id = customer_id

    def update_contact_info(self, new_contact):
        self.__contact_info = new_contact

    def get_contact_info(self):
        return self.__contact_info

    @abstractmethod
    def display_info(self):
        pass

# Customer Subclass
class Customer(Person):
    """Represents a Blinkit customer."""

    def __init__(self, name, age, gender, contact_info, customer_id, address, wallet_balance=0.0):
        super().__init__(name, age, gender, contact_info, customer_id)
        self.address = address
        self.wallet_balance = wallet_balance
        self.orders = []

    def add_balance(self, amount):
        self.wallet_balance += amount

    def place_order(self, order):
        if order.total_price <= self.wallet_balance:
            self.wallet_balance -= order.total_price
            self.orders.append(order)
            return f"Order placed successfully! Remaining balance: ₹{self.wallet_balance}"
        else:
            return "Insufficient balance to place this order."

    def display_info(self):
        return (f"[Customer] Name: {self.name}, Age: {self.age}, Gender: {self.gender}, "
                f"Contact: {self.get_contact_info()}, ID: {self.customer_id}, "
                f"Address: {self.address}, Wallet: ₹{self.wallet_balance}, Orders: {len(self.orders)}")

# Order Class
class Order:
    """Represents a Blinkit order."""

    def __init__(self, order_id, items, total_price):
        self.order_id = order_id
        self.items = items
        self.total_price = total_price

    def display_order(self):
        return f"Order ID: {self.order_id} | Items: {', '.join(self.items)} | Total: ₹{self.total_price}"

# Blinkit Management System
class BlinkitManagement:
    customers = []

    @classmethod
    def register_customer(cls, customer):
        if any(c.customer_id == customer.customer_id for c in cls.customers):
            print(f"Customer ID {customer.customer_id} already exists!")
            return
        cls.customers.append(customer)

    @classmethod
    def list_all_customers(cls):
        if not cls.customers:
            print("No customers registered.")
        else:
            for c in cls.customers:
                print(c.display_info())

    @classmethod
    def find_customer_by_id(cls, cust_id):
        for c in cls.customers:
            if c.customer_id == cust_id:
                return c
        return None

    @staticmethod
    def generate_report():
        return f"Total Customers: {len(BlinkitManagement.customers)}"

# CLI Interface
def main():
    # Preloaded customers
    default_customers = [
        Customer("vishwas", 22, "Male", "9876543210", "C001", "Delhi", 500),
        Customer("vaishnavi", 20, "Female", "8765432109", "C002", "Mumbai", 1000),
        Customer("nikhil", 23, "Male", "7654321098", "C003", "Bangalore", 300),
    ]

    for cust in default_customers:
        BlinkitManagement.register_customer(cust)

    # CLI Menu
    while True:
        print("\n========= Blinkit Customer Management =========")
        print("1. Register New Customer")
        print("2. List All Customers")
        print("3. Find Customer by ID")
        print("4. Place an Order")
        print("5. Generate System Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            contact = input("Enter contact info: ")
            customer_id = input("Enter customer ID: ")
            address = input("Enter address: ")
            balance = float(input("Enter initial wallet balance: "))
            new_customer = Customer(name, age, gender, contact, customer_id, address, balance)
            BlinkitManagement.register_customer(new_customer)

        elif choice == "2":
            BlinkitManagement.list_all_customers()

        elif choice == "3":
            cust_id = input("Enter Customer ID: ")
            customer = BlinkitManagement.find_customer_by_id(cust_id)
            if customer:
                print(customer.display_info())
            else:
                print("Customer not found.")

        elif choice == "4":
            cust_id = input("Enter Customer ID: ")
            customer = BlinkitManagement.find_customer_by_id(cust_id)
            if customer:
                items = input("Enter items (comma separated): ").split(',')
                total_price = float(input("Enter total price: "))
                order_id = f"O{len(customer.orders)+1:03d}"
                order = Order(order_id, [item.strip() for item in items], total_price)
                print(customer.place_order(order))
            else:
                print("Customer not found.")

        elif choice == "5":
            print(BlinkitManagement.generate_report())

        elif choice == "6":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the CLI
if __name__ == "__main__":
    main()