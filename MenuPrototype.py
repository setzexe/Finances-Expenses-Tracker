password = input("Enter password: ") # Asks for password. This is very beginner level right now, as it is just hardwired into the code. Will have it so it's not just hardwired later
if password != "SetzFP": # Password validation
    print("Wrong Password!")
    quit() # Quits script if this branch goes off
else:
    print("Welcome, User.") # Success 

while True: # Menu. This only ends if an error occurs, or if a break occurs
    print("Select your option")
    print("1: View Assets")
    print("2: Add Expenses")
    print("3: View Past Expenses")
    print("4: Add new expense / asset")
    print("5: Exit\n")

    try: # try to code below, and continue except on ValueError type
        choice = int(input("Enter option: "))
    except ValueError: # If input is not of value type Int
        print("Invalid input. Please enter a number (1-5).")
        continue # Goes to the start of the loop

    match choice: # Python's equivilent to Switch-Case's. Check's if choice is 1-5, and branches to the _ branch if otherwise.
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
        case _:  # Default case, similar to else
            print("Invalid option. Try again.")
