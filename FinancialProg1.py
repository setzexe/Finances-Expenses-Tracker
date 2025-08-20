import sqlite3 # Sqlite3 is a bridge module that allows you to talk to an SQLite database file. Essential uses SQL to access local database files
from datetime import datetime # Imports the datetime class from the datetime module. Use this whenever current data & time needed

connector = sqlite3.connect("finance_tracker.db") # Connector type. Connector connects to the file in quotes. If that file does not exist, it is created.
cursor = connector.cursor() # Cursor for doing SQL queries. Practically our cursor from python's code to accessible SQL data
# You can imagine cursor like. It's the cursor that goes through and works with sqllite. Like a mouse cursor on an actual database page

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

"""
id Is the primary key / main identifier. AUTOINCREMENT means it goes up by one every time a new row is created.
The attributes below it are descriptors / not a primary key. NOT NULL means They can't be blank, the column needs data to be valid.
SQLite holds 5 different data types: NULL, INT (single number, can be a any amount of digits), REAL (floating value), TEXT (string), and BLOB (purely input)
"""

connector.commit() # Saves the two queries above

def view_assets(cursor): # Runs cursor as our parameter. This function will be option 1
    cursor.execute("SELECT * FROM assets") # Cursor runs the SQL syntax to select all rows of data
    rows = cursor.fetchall() # Fetches all the rows. They all get stored as tuples, which is a collection of data similar to an array with various data types. Rows becomes a list type
    
    print("\n--- Assets ---") 
    print("ID | Name | Type | Amount | Value | Last Updated") # Formatting
    print("-" * 60) # prints a 60 spaced line with -
    
    for row in rows: # For each row in the rows list
        asset_id, name, category, amount, date_added = row # Because row is a tuple, Each variable can be assigned with the respective bit of data in the row
        value = amount  # Until we get the API system set up, value will just be the same as amount
        print(f"{asset_id} | {name} | {category} | {amount} | {value} | {date_added}") # Formatted string

def add_entry(cursor, connector): # 
    while True: # Menu, wont be exited until break
        print("\n--- Add Menu ---")
        print("1: Add Asset")
        print("2: Add Expense")
        print("3: Back to Main Menu") # Formatting

        try: # Go to main menu if input for choice is not of type int
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Please enter 1-3.") 
            continue # Back to main menu

    
        if choice == 1: # Add asset
            name = input("Enter asset name (e.g., XRP, Cash): ") # Asset name
            category = input("Enter category (Cash or Investment): ") # Will have to fix this later on so we can not add duplicates. Same with data as a whole
            amount = float(input("Enter amount: "))

            date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Date_added uses the datetime.now() command. Strftime means String Format Time. The parenthesis next to it formats that
            # (%Year-%month- and so on)

            cursor.execute("""
                INSERT INTO assets (name, category, amount, date_added)
                VALUES (?, ?, ?, ?)
            """, (name, category, amount, date_added)) # The ?'s are placeholders for the query. The parenthesis after the quotes is what actually inputs info
            # Execute is just inserting our info to the database. It does not display any info
            
            connector.commit() # Saves changes to the database
            print(f"Asset '{name}' added successfully!")

       
        elif choice == 2: # Expenses
            description = input("Enter expense description: ") # "Restaurant, Soda, Etc"
            amount = float(input("Enter amount: "))

            date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # "Year-month-date Hour:Minute:Second"

            cursor.execute("""
                INSERT INTO expenses (description, amount, date_added)
                VALUES (?, ?, ?)
            """, (description, amount, date_added))

            connector.commit() # Practically the same process as assets
            print("Expense recorded successfully!")

        elif choice == 3: # Exit
            print("Returning to main menu...")
            break
        else: # Int input, but not 1-3
            print("Invalid option. Please enter 1-3.")

    
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
            view_assets(cursor) 
        case 2:
            add_entry(cursor, connector)
        case 3:
            print("Coming soon...")
        case 4:
            print("Coming soon...")
        case 5:
            print("See you soon!")
            exit()
        case _:  
            print("Invalid option. Try again.")
