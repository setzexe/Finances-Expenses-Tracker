import sqlite3 # Sqlite3 is a bridge module that allows you to talk to an SQLite database file. Essential uses SQL to access local database files
from datetime import datetime # Imports the datetime class from the datetime module. Use this whenever current data & time needed

connector = sqlite3.connect("finance_tracker.db") # Connector type. Connector connects to the file in quotes. If that file does not exist, it is created.
cursor = connector.cursor() # Cursor for doing SQL queries. Practically our cursor from python's code to accessible SQL data

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS assets ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    date_added TEXT NOT NULL
)
""") # Allows us to execute queries to Sqlite3. Note, due to IF NOT EXISTS, this query will only create the tables if have not already been created.
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    amount REAL NOT NULL,
    date_added TEXT NOT NULL
)
""")

connector.commit() # Saves the two queries above

password = input("Enter password: ")  
if password != "SetzFP":
    print("Wrong Password!")
    quit() 
else: 
    print("Welcome, User.")

while True: 
    print("1: View Assets")
    print("2: Add Expenses / Assets")
    print("3: Add New Asset Type")
    print("4: View Past Expenses")
    print("5: Exit\n")

    try: 
        choice = int(input("Enter option: "))
    except:
        print("Invalid input. Please enter a number (1-5).")
        continue #

    match choice: 
        case 1: 
            print("Coming soon...\n") 
        case 2:
            print("Coming soon...\n")
        case 3:
            print("Coming soon...\n")
        case 4:
            print("Coming soon...\n")
        case 5:
            print("See you soon!")
            break
        case _:  
            print("Invalid option. Try again.")
