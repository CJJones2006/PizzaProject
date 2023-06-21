from enum import Enum
import sqlite3

connection = sqlite3.connect("pizzacompany.db")
cursor = connection.cursor()

class Variety(Enum):
    Margherita = 0
    Pepperoni = 1
    Pineapple = 2
    Meaty = 3
    HamMushroom = 4
    Garlic = 5

class Pizza:
    def __init__(self, sizeInInches, variety):
        self.sizeInInches = sizeInInches
        self.variety = variety
        
        if self.variety == Variety.Margherita:
            self.ingredients = ["Pizza dough", "Tomato Sauce", "Mozzerella", "Basil"]
        elif self.variety == Variety.Pepperoni:
            self.ingredients = ["Pizza dough", "Tomato Sauce", "Mozzerella", "Pepperoni"]
        elif self.variety == Variety.Pineapple:
            self.ingredients = ["Pizza dough", "Tomato Sauce", "Mozzerella", "Pineapple"]
        elif self.variety == Variety.Meaty:
            self.ingredients = ["Pizza dough", "Tomato Sauce", "Mozzerella", "Chicken", "Ham", "Beef"]
        elif self.variety == Variety.HamMushroom:
            self.ingredients = ["Pizza dough", "Tomato Sauce", "Mozzerella", "Ham", "Mushrooms"]
        elif self.variety == Variety.Garlic:
            self.ingredients = ["Pizza dough", "Mozzerella", "Garlic"]

class CustomerOrders:
    def __init__(self, customer, orderNumber, pizzas):
        self.orderNumber = orderNumber
        self.pizzas = pizzas

class Customer():
    def __init__(self, firstName, lastName, email):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

def DisplayCustomers():
    cursor.execute("SELECT * FROM customers")
    return cursor.fetchall()

def AddCustomer():
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    email = input("Email Address: ")

    statement = '''INSERT INTO customers(firstName, lastName, email)
                   VALUES(?, ?, ?)'''
    values = (firstName, lastName, email)
    cursor.execute(statement, values)
    connection.commit()
    print(f"Updated table:\n{DisplayCustomers()}")

def DeleteLastCustomer():
    statement = '''DELETE FROM customers
                   WHERE ID=(SELECT MAX(id) FROM customers)'''
    cursor.execute(statement)
    connection.commit()
    print(f"Updated table:\n{DisplayCustomers()}")

print("1: Add Customer")
print("2: Delete Last Customer")

menu = int(input("> "))
if menu == 1:
    AddCustomer()
elif menu == 2:
    DeleteLastCustomer()