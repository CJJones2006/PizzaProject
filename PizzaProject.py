from enum import Enum
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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

    def getCost(self):
        if self.sizeInInches == 7:
            cost = 5.00
        elif self.sizeInInches == 10:
            cost = 7.00
        elif self.sizeInInches == 12:
            cost = 8.00
        elif self.sizeInInches == 14:
            cost = 10.00
        
        if self.variety == Variety.Margherita:
            cost += 0.00
        elif self.variety == Variety.Pepperoni:
            cost += 1.00
        elif self.variety == Variety.Pineapple:
            cost += 1.00
        elif self.variety == Variety.Meaty:
            cost += 2.00
        elif self.variety == Variety.HamMushroom:
            cost += 2.00
        elif self.variety == Variety.Garlic:
            cost += 0.50

        return cost


class Customer:
    def __init__(self, customerID, firstName, lastName, email, mobileNumber):
        self.customerID = customerID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.mobileNumber = mobileNumber

class CustomerOrders:
    def __init__(self, customer, orderNumber, pizzas):
        self.orderNumber = orderNumber
        self.pizzas = pizzas

pizza1 = Pizza(14, Variety.Garlic)

print(pizza1.getCost())
