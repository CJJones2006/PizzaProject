import sqlite3

connection = sqlite3.connect("tutorial.db")
cursor = connection.cursor()

#cursor.execute("CREATE TABLE movie(title, year, score)")

cursor.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('Interstellar', 2014, 8.7)
""")

connection.commit()

class Pizza:
    def __init__(self, ingredients, sizeInInches, variety):
        self.ingredients = ingredients
        self.sizeInInches = sizeInInches
        self.variety = variety

class Customer:
    def __init__(self, customerID, firstName, lastName, email, mobileNumber):
        self.customerID = customerID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.mobileNumber = mobileNumber
