#Explain your work
"""
Program flow:
1. There's the main function all the way down below. That's the starting point
2. The main function implementation is right above it. I divided each operation into their own functions
so should be easy to check out what each function does
    a. Register/Update account
    b. Delete account
    c. List accounts
    NOTE: 
    To list all accounts, you need the admin access information
    username: admin
    password :admin
3. Each function should also have a javadoc style description above it (might not be, lets see if I'll have time)
4. Don't let the file size scary you, it's mostly print statements.
If I have time in the end, I'll move them into helper functions but for now 
they're in the code itself (which is ugly but I don't get to be this sloppy in professional life let me have my fun while learning something new)
 
Notes:
1. I wanted to add some returning back functionality but as the menu tree got deeper
the functionality got more and more complex so I had to compromise at some point by making it
go all the way back rather than looping through every submenu with return options
2. The main loop is simple:
    a. The app gets the data from the local file (Was gonna go with DB, if I have some time I will. If not, it's a json file')
    b. All the operations are done on the memory. It doesn't affect the file 
    (cause it's already too complex and I don't wanna check more test case scenarios')
    c. On exit (both normally and in the case of ctrl+c exit) I update the json file with the information
3. All options are in the menu. Each menu item is it's own function.
4. Util import holds all the large print statement bodies and some helper functions
I should probably move ALL string-related stuff there but it didn't help a lot with the file size when I thought about it
so I just have some one or two liner print statements in between the logic
   
Now the underlying stuff:
1. I'm holding the data in a dictionary in "username":"password" format
2. All account operations (insertion, deletion, update and list) happens there
3. (Currently) on exit, I'm saving the data to a json file to keep it between sessions
I chose json cause it's basically THE file format for dictionary. Also, and I didn't know that,
but Python built-in json library returns a dictionary on parsing which is quite cool

"""

import json
import util

"""
MAIN FLOW:
    Roleplay as an evil corp, print some evil corp stuff
    
    If a file exists - get data from the file
    Cache it in a dictionary
    if not open up a new one
    
    Show a menu:
        1-) Register account
        2-) Delete account
        3-) List account
    
    Register:
        1-) Get username - pass
        2-) Store it in the dictionary
    
    Delete:
        1-) Find account in Dict
        2-) Delete it from the Dict
    
    List:
        1-) Iterate over Dict
        2-) Print everything
    
    On exit:
        1-) Store dictionary in a file
        2-) Exit the app
    
    
EXTRAS:
    1-) Change file into db (python apparently has sqlite built in)
    2-) Username - password syntax check (regex or str.issomething() stuff)
"""
    
# ==============================================================

"""Updates user info in the users dictionary

    Parameters
    ----------
    users : Dictionary
        The dictionary holding account information
    username : string
        The username to be updated in the Dictionary. Used as a key
    password : string
        The password to be updated in the Dictionary. Used as a value

    Returns
    -------
    None
    """
def updateUser(users, username="", password=""):
    users[username] = password
    print("Password updated")

"""Saves user info in the database

    Parameters
    ----------
    users : Dictionary
        The dictionary holding account information
    file : File object
        File for the database file

    Returns
    -------
    None
    """
def saveUsers(users, file):
    file.close()
    file = open("userdb.json", "w")
    json.dump(users, file)
    
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
    registrationMenuString = util.buildRegistrationMenu()
    
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
                choice = input("Would you like to update it? y/n\n")
                if choice == "y":
                    # Update the user info on "y" input
                    updateUser(users, username, password)
                elif choice == "n":
                    # Go back to the menu on "n" input
                    print("Not updating the user info and going back to the account menu...")
                    continue
                else:
                    # Wrong input, go back to the menu anyway
                    print("Wrong input. Going back to the main menu without any action")
                    continue
            else:
                #If it's not in the DB, add it to the DB
                users[username] = password
                print(f"Username {username} is successfully created!")
        # Choice 2 = Update an existing user
        elif(choice == "2"):
            #get user and password
            username, password, isSuccessfullyRetreived = util.receiveAccountInfoFromUser()
            if(not isSuccessfullyRetreived):
                continue
            
            #Check if the username exists in the DB
            if(username in users):
                updateUser(users, username, password)
            else:
                # If username's not in the DB, ask if it should be created
                print(f"Username {username} doesn't exist in the database.")
                choice = input("Would you like to create a new entry? y/n\n")
                if choice == "y":
                    users[username] = password
                elif choice == "n":
                    # Go back to the menu on "n" input
                    print("Not creating a new user entry and going back to the account menu...")
                    continue
                else:
                    # Wrong input, go back to the menu anyway
                    print("Wrong input. Going back to the main menu without any action")
                    continue
        # Choice 3 = go back to the main menu
        elif(choice == "3"):
            print("Going back to the main menu...")
            break
        else:
            print("Undefined menu entry. Please try again.")
            continue
    
"""Deletes a user from the "users" dictionary

Parameters
----------
users : Dictionary
    The dictionary holding account information

Returns
-------
None
"""
def deleteAccount(users):
    #build menu to print
    deleteAccountMenuString = util.buildDeleteAccountMenu()
    
    # The user has three chances to enter correct username / password
    trial = 3
    while True:
        # Out of luck
        if(trial == 0):
            util.printDeleteAccountInfoText()
            break

        # Get the input for the menu choice
        choice = input(deleteAccountMenuString)
        
        #Delete account choice
        if(choice == "1"):
            # Print about the extermination condition
            util.printDeleteAccountTrialInfoText(trial)
            
            #get user and password
            username, password, isSuccessfullyRetrieved = util.receiveAccountInfoFromUser()
            
            if(not isSuccessfullyRetrieved):
                continue

            # Check if username exists
            if(username in users):
                print(f"Username {username} is found in the DB.")
                
                #Get the registered password and compare it with the entered info
                oldpassword = users[username]
                
                #Credential check failed
                if(password != oldpassword):
                    trial -= 1
                    print("However, the password entered is not the registered one.")
                    gobackChoice = input("Would you like to try again or would you like to go back to the main menu? y/n \n")
                    if(gobackChoice.lower() == "y"):
                        continue
                    elif(gobackChoice.lower() == "n"):
                        print("Going back to the main menu...")
                        break
                    else:
                        print("Neither of these were the input. Assuming you wanted to say n.")
                        print("Going back to the main menu...")
                        break
                #Credential check succeeded
                else:
                    print("The password is accepted!")
                    deletionChoice = input("Do you really want to delete your account? y/n \n")
                    # Delete account
                    if(deletionChoice.lower() == "y"):
                        users.pop(username)
                        print("The account is deleted. Thank you for working with The Evil Corp™")
                        break
                    elif(deletionChoice.lower() == "n"):
                        print("Going back to the main menu...")
                        break
                    else:
                        print("Neither of these were the input.")
                        print("Going back to the deletion menu...")
                        break    
            else:
                print(f"{username} is not found in the DB. Going back to the deletion menu...")
                continue
            
        # Going back to the menu choice
        elif choice == "2":
            print("Going back to the main menu...")
            break
        else:
            print("Undefined menu entry. Please try again.")
            continue

"""Lists all accounts in the "users" dictionary

Parameters
----------
users : Dictionary
    The dictionary holding account information

Returns
-------
None
"""
def listAccounts(users):
    # Build the menu string to print it for input guidance
    listAccountMenuText = util.buildListAccountMenu()
    
    # How many times to enter the admin information
    trial = 3
    while True:
        if(trial == 0):
            print("\nYou tried to login three times. For security purposes your session is terminated.")
            print("Please remain seated while our forces are coming to join with you. Have a pleasant day! :)")
            
            break
            
        choice = input(listAccountMenuText)
         
        if choice == "1":
            
            username, password, isRetrieved = util.receiveAccountInfoFromUser()
            if(not isRetrieved):
                 continue

            if(username == "admin" and password == "admin"):
                print("Your admin credentials are accepted!")
                print("The accounts registered to this system: ")
                print("Username".center(16, "-") +"Password".center(16,"-"))
                for entry in users:
                    print(f"\t{entry}:\t{users[entry]}")
                continue
            else:
                trial -= 1
                print(f"Your username {username} or your password {password} doesn't match admin credentials\n")
                print("Please enter admin credentials to use to this feature")
                print(f"You have {trial} times left to login")
                continue
        elif choice == "2":
            print("Going back to the main menu...")
            break
        else:

            print("Undefined menu entry. Please try again.")
            continue
    
    
# Main method
def main():
    # Try to open the db file for read
    file = None
    try:
        file = open("userdb.json", "r")
    except IOError:
        print("Unable to access Database. Check the access parameters of the app")
        return
    
    # REALLY dirty solution but I don't know what's the best way to handle
    # json load operation on an empty file
    # the library, for some reason, doesn't return a None object, just throws an exception
    # An alternative would be to have the file filled with something initially but if the users delete it
    # This way, the program wouldn't crash
    users = {}  # users is a dict of "username : password"
    try:
        users = json.load(file)
    except json.JSONDecodeError:
        # Fails if the empty is empty, so I close it an reopen it as readable to insert some dummy value
        # This should happen only on the first time this is initialized
        file.close()
        file = open("userdb.json", "w")
        users = {} #dummy value
        json.dump(users, file)
    finally:
        # Load existing user data into memory from the db  
        file.close()
        file = open("userdb.json", "r")
        users = json.load(file) # users is a dict of "username : password"

    try:  
        # Build the menu string to print it for input guidance
        mainMenuString = util.buildMainMenuString()
        
        while True:
            # Menu input
            choice = input(mainMenuString)
                
            #switch over the input
            if choice == "1":
                registerAccount(users)
            elif choice == "2":
                deleteAccount(users)
            elif choice == "3":
                listAccounts(users)
            elif choice == "4":
                break
            else:
                print("Invalid input!")
                continue
        
        print("Thank you for choosing Amazing User Interface™!")
        print("Hope you had a pleasant experience!")
        
        # Save users on exit
        # Note: In a real life scenario, I actually would've been calling this on every update, insert and delete
        # However, we're already at 300 lines at the time of writing this so I just decided to "update" the database
        # on exit
        saveUsers(users, file)
        file.close()
    except KeyboardInterrupt:
        print("Application is interrupted by the user. Quiting the app...")
    finally:
        print("Exiting the app now...")
        saveUsers(users, file)
        file.close()

# ENTRY POINT
main()


# datalist.append(data)

# json.dump(datalist, file)


    
    
    
    