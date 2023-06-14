from enum import Enum
import sqlite3

#connection = sqlite3.connect("tutorial.db")
#cursor = connection.cursor()
#
##cursor.execute("CREATE TABLE movie(title, year, score)")
#
#cursor.execute("""
#    INSERT INTO movie VALUES
#        ('Monty Python and the Holy Grail', 1975, 8.2),
#        ('Interstellar', 2014, 8.7)
#""")
#
#connection.commit()

class Variety(Enum):
    Margherita = 0
    Pepperoni = 1
    Pineapple = 2


class Pizza:
    def __init__(self, sizeInInches, variety):
        self.sizeInInches = sizeInInches
        self.variety = variety

        if self.variety == Variety.Margherita:
            self.ingredients = ["Tomato Sauce", "Mozzerella", "Basil"]

class Customer:
    def __init__(self, customerID, firstName, lastName, email, mobileNumber):
        self.customerID = customerID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.mobileNumber = mobileNumber

class CustomerOrders:
    def __init__(self, orderNumber, cost, pizzas):
        self.orderNumber = orderNumber
        self.cost = cost
        self.pizzas = pizzas

margheritaPizza = Pizza(12, Variety.Margherita)

print(margheritaPizza.ingredients)
