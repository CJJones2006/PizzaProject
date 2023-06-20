from enum import Enum
from tkinter.tix import Select
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
import os.path

db = SQLAlchemy()
app = Flask(__name__)
db_name = "pizzacompany.db"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, db_name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

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

class CustomerOrders:
    def __init__(self, customer, orderNumber, pizzas):
        self.orderNumber = orderNumber
        self.pizzas = pizzas

class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String)
    lastName = db.Column(db.String)
    email = db.Column(db.String)
    mobileNumber = db.Column(db.String)

    def __init__(self, firstName, lastName, email, mobileNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.mobileNumber = mobileNumber

@app.route('/')
def index():
    try:
        customers = db.session.execute(db.select(Customer)).scalars()

        customer_text = '<ul>'
        for customer in customers:
            customer_text += '<li>' + customer.name + ', ' + customer.color + '</li>'
        customer_text += '</ul>'
        return customer_text
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

print(db.session.execute(select(Customer)))