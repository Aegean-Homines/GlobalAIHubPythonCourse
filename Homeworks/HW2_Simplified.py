#Explain your work
"""
Pretty simple flow:
    1. Main menu renders
    2. Choosing 1 gets you to creating a new user info
    New user info then is pushed to the users hashmap
    3. Choosing 2 gets you to the login screen
    It uses the same hashmap from the first option so
    it checks if the username key value exists in the dictionary
    then checks if the input password matches it. Then logs in.
    4. Choosing 3 exist the app
    
The same going back etc flow also happens in the sub menus to go back to the main menu
"""
import util # Contains printing functions

"""Registers or updates a user into the "users" dictionary

Parameters
----------
users : Dictionary
    The dictionary holding account information

Returns
-------
None
"""
def registerAccount(users):
    # Build the menu string to print it for input guidance
    registrationMenuString = util.buildSimplifiedRegistrationMenu()
    
    while True:
        # Get the input for the menu choice
        choice = input(registrationMenuString)
        
        # switch over choices
        # Choice 1 = Create a new user
        if(choice == "1"):
            #get user and password
            username, password, isSuccessfullyRetreived = util.receiveAccountInfoFromUser()
            if(not isSuccessfullyRetreived):
                continue

            #Check if the username exists in the DB
            if(username in users):
                # If username's in the DB, ask if it should be updated
                print(f"Username {username} already exists in the database.")
            else:
                #If it's not in the DB, add it to the DB
                users[username] = password
                print(f"Username {username} is successfully created!")
        # Choice 3 = go back to the main menu
        elif(choice == "2"):
            print("Going back to the main menu...")
            break
        else:
            print("Undefined menu entry. Please try again.")
            continue
        
"""Login to the system

Parameters
----------
users : Dictionary
    The dictionary holding account information

Returns
-------
None

"""
def login(users):
    isLoggedInSuccessfully = False
    
    loginMenuString = util.buildSimplifiedLoginMenu()
    loginRewardString = util.buildSimplifiedLoginRewardAscii()

    while True:
         # Users successfully logging in get to enjoy the arrival of the Le Toucan 
        if(isLoggedInSuccessfully):
            print("\n")
            print(loginRewardString)
            print("\n")
        
        # Get the input for the menu choice
        choice = input(loginMenuString)
        
        # switch over choices
        # Choice 1 = Login
        if(choice == "1"):
            #get user and password
            username, password, isSuccessfullyRetrieved = util.receiveAccountInfoFromUser()
            
            if(not isSuccessfullyRetrieved):
                continue
            
            if(username in users):
                if(users[username] == password):
                    print(f"Correct credentials! Welcome {username}.")
                    isLoggedInSuccessfully = True
                    continue
                else:
                    print(f"The password for {username} is invalid. Please use the password registered to your account.")
                    isLoggedInSuccessfully = False
            else:
                print(f"Username {username} not found. Please check your username again.")
        elif(choice == "2"):
            print("Please wait while we're returning you to the main menu.")
            break
        else:
            print("Invalid input. Please try again.")
            continue
                

def main():
  
    users = {} # Hashmap to hold the user information
    try:  
        # Build the menu string to print it for input guidance
        mainMenuString = util.buildSimplifiedMainMenuString()
        
        while True:
            # Menu input
            choice = input(mainMenuString)
                
            #switch over the input
            if choice == "1":
                registerAccount(users)
            elif choice == "2":
                login(users)
            elif choice == "3":
                break
            else:
                print("Invalid input!")
                continue
        
        print("Thank you for choosing Amazing User Interface™!")
        print("Hope you had a pleasant experience!")

    except KeyboardInterrupt:
        print("Application is interrupted by the user. Quiting the app...")
    finally:
        print("Exiting the app now...")


main()
    
    
    