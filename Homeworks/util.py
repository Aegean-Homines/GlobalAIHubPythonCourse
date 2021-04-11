# CONSTANTS
DatabaseFileName = "userdb.json"

# Menu print functions (HW2_Simplified)
def buildSimplifiedMainMenuString():
    menuStringList = []

    menuStringList.append("\t\"Nec Dei, Nec Reges. Solummodo homines.\"\n")
    menuStringList.append("\t\t      -The Evil Corp™          \n\n")
    menuStringList.append("\t\t              ▄▀▄               \n")
    menuStringList.append("\t\t            ▄▀   ▀▄             \n")
    menuStringList.append("\t\t          ▄▀  ▄▄▄  ▀▄           \n")
    menuStringList.append("\t\t        ▄▀  ▄▀ ▄ ▀▄  ▀▄         \n")
    menuStringList.append("\t\t      ▄▀     ▀▄▄▄▀     ▀▄       \n")
    menuStringList.append("\t\t    ▄▀                   ▀▄     \n")
    menuStringList.append("\t\t    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀     \n\n\n\n")  
    menuStringList.append("Welcome to the Amazing User Interface™ developed by The Evil Corp™\n")
    menuStringList.append("Please select the option you want to proceed with: \n")
    menuStringList.append("\t1. Create Account\n")
    menuStringList.append("\t2. Login\n")
    menuStringList.append("\t3. Exit app\n")
    
    return ''.join(menuStringList)

def buildSimplifiedRegistrationMenu():
    registrationMenuStringList = []
    registrationMenuStringList.append("Welcome to the User Registration Menu™\n")
    registrationMenuStringList.append("Please select an operation: \n")
    registrationMenuStringList.append("\t1. Create new user\n")
    registrationMenuStringList.append("\t2. Return back to the menu\n")
    
    return ''.join(registrationMenuStringList)

def buildSimplifiedLoginMenu():
    loginMenuStringList = []
    loginMenuStringList.append("Welcome to the Login Menu™\n")
    loginMenuStringList.append("Please login with your username and password.\n")
    loginMenuStringList.append("Please select an operation:.\n")
    loginMenuStringList.append("\t1. Login\n")
    loginMenuStringList.append("\t2. Return back to the menu\n")   
    return ''.join(loginMenuStringList)

def buildSimplifiedLoginRewardAscii():
    loginRewardStringList = []
    loginRewardStringList.append("░░░░░░░░▄▄▄▀▀▀▄▄███▄░░░░░░░░░░░░░░\n")
    loginRewardStringList.append("░░░░░▄▀▀░░░░░░░▐░▀██▌░░░░░░░░░░░░░\n")
    loginRewardStringList.append("░░░▄▀░░░░▄▄███░▌▀▀░▀█░░░░░░░░░░░░░\n")
    loginRewardStringList.append("░░▄█░░▄▀▀▒▒▒▒▒▄▐░░░░█▌░░░░░░░░░░░░\n")
    loginRewardStringList.append("░▐█▀▄▀▄▄▄▄▀▀▀▀▌░░░░░▐█▄░░░░░░░░░░░\n")
    loginRewardStringList.append("░▌▄▄▀▀░░░░░░░░▌░░░░▄███████▄░░░░░░\n")
    loginRewardStringList.append("░░░░░░░░░░░░░▐░░░░▐███████████▄░░░\n")
    loginRewardStringList.append("░░░░░le░░░░░░░▐░░░░▐█████████████▄\n")
    loginRewardStringList.append("░░░░toucan░░░░░░▀▄░░░▐█████████████▄\n")
    loginRewardStringList.append("░░░░░░has░░░░░░░░▀▄▄███████████████\n")
    loginRewardStringList.append("░░░░░arrived░░░░░░░░░░░░█▀██████░░\n")
 
    return ''.join(loginRewardStringList)
    
# Menu print functions (HW2_FullApp)
def buildMainMenuString():
    
    # Apparently, list of strings is way faster than concatting strings one by one:
    # https://waymoot.org/home/python_string/
    menuStringList = []

    menuStringList.append("\t\"Nec Dei, Nec Reges. Solummodo homines.\"\n")
    menuStringList.append("\t\t      -The Evil Corp™          \n\n")
    menuStringList.append("\t\t              ▄▀▄               \n")
    menuStringList.append("\t\t            ▄▀   ▀▄             \n")
    menuStringList.append("\t\t          ▄▀  ▄▄▄  ▀▄           \n")
    menuStringList.append("\t\t        ▄▀  ▄▀ ▄ ▀▄  ▀▄         \n")
    menuStringList.append("\t\t      ▄▀     ▀▄▄▄▀     ▀▄       \n")
    menuStringList.append("\t\t    ▄▀                   ▀▄     \n")
    menuStringList.append("\t\t    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀     \n\n\n\n")  
    menuStringList.append("Welcome to the Amazing User Interface™ developed by The Evil Corp™\n")
    menuStringList.append("Please select the option you want to proceed with: \n")
    menuStringList.append("\t1. Register or Update Account\n")
    menuStringList.append("\t2. Delete Account\n")
    menuStringList.append("\t3. List Account\n")
    menuStringList.append("\t4. Login\n")
    menuStringList.append("\t5. Exit app\n")
    
    return ''.join(menuStringList)

def buildRegistrationMenu():
    registrationMenuStringList = []
    registrationMenuStringList.append("Welcome to the User Registration Menu™\n")
    registrationMenuStringList.append("Please select an operation: \n")
    registrationMenuStringList.append("\t1. Create new user\n")
    registrationMenuStringList.append("\t2. Update existing user\n")
    registrationMenuStringList.append("\t3. Return back to the menu\n")
    
    return ''.join(registrationMenuStringList)

def buildDeleteAccountMenu():
    deleteAccountMenuStringList = []
    deleteAccountMenuStringList.append("Welcome to the Account Deletion Menu™\n")
    deleteAccountMenuStringList.append("Please select an operation: \n")
    deleteAccountMenuStringList.append("\t1. Delete an account\n")
    deleteAccountMenuStringList.append("\t2. Return back to the menu\n")   
    
    return ''.join(deleteAccountMenuStringList)

def buildListAccountMenu():
    
    listAccountMenuStringList = []
    listAccountMenuStringList.append("Welcome to the List Account Info Menu™\n")
    listAccountMenuStringList.append("Please login with your admin credentials to list all the accounts.\n")
    listAccountMenuStringList.append("Please note that if you fail to login three times with the admin credentials\n")
    listAccountMenuStringList.append("our team of professionals will come to your location to help you remind your login info.\n\n")
    listAccountMenuStringList.append("Please select an operation:.\n")
    listAccountMenuStringList.append("\t1. List all accounts\n")
    listAccountMenuStringList.append("\t2. Return back to the menu\n")   
    return ''.join(listAccountMenuStringList)

def buildLoginMenu():
    loginMenuStringList = []
    loginMenuStringList.append("Welcome to the Login Menu™\n")
    loginMenuStringList.append("Please login with your username and password.\n")
    loginMenuStringList.append("Please note that if you fail to login three times with your credentials\n")
    loginMenuStringList.append("our team of professionals will come to your location to help you remind your login info.\n")
    loginMenuStringList.append("by Any. Means. Necessary.\n\n")
    loginMenuStringList.append("Please select an operation:.\n")
    loginMenuStringList.append("\t1. Login\n")
    loginMenuStringList.append("\t2. Return back to the menu\n")   
    return ''.join(loginMenuStringList)

def buildLoginRewardAscii():
    loginRewardStringList = []
    loginRewardStringList.append("░░░░░░░░▄▄▄▀▀▀▄▄███▄░░░░░░░░░░░░░░\n")
    loginRewardStringList.append("░░░░░▄▀▀░░░░░░░▐░▀██▌░░░░░░░░░░░░░\n")
    loginRewardStringList.append("░░░▄▀░░░░▄▄███░▌▀▀░▀█░░░░░░░░░░░░░\n")
    loginRewardStringList.append("░░▄█░░▄▀▀▒▒▒▒▒▄▐░░░░█▌░░░░░░░░░░░░\n")
    loginRewardStringList.append("░▐█▀▄▀▄▄▄▄▀▀▀▀▌░░░░░▐█▄░░░░░░░░░░░\n")
    loginRewardStringList.append("░▌▄▄▀▀░░░░░░░░▌░░░░▄███████▄░░░░░░\n")
    loginRewardStringList.append("░░░░░░░░░░░░░▐░░░░▐███████████▄░░░\n")
    loginRewardStringList.append("░░░░░le░░░░░░░▐░░░░▐█████████████▄\n")
    loginRewardStringList.append("░░░░toucan░░░░░░▀▄░░░▐█████████████▄\n")
    loginRewardStringList.append("░░░░░░has░░░░░░░░▀▄▄███████████████\n")
    loginRewardStringList.append("░░░░░arrived░░░░░░░░░░░░█▀██████░░\n")
 
    return ''.join(loginRewardStringList)

def printDeleteAccountInfoText():
    print("You tried to login three times. For security purposes your session is terminated.")
    print("Please remain seated while our forces are coming to join with you. Have a pleasant day! :)")
    
    # ETHICS RUINING MY FUN EXPLANATION BELOW!!:
    print("BREAKING THE FOURTH WALL EXPLANATION: ")
    print("I (Egemen) actually added a portion of a code here using ipinfo library that would print the ip information of the machine running the code")
    print(" as well as other stuff (postal, city, country, region, geographical coordinates) as a joke")
    print(", however I'm told by my more sensible friends that this might a bit...uncomfortable. I added the code snippet to the source anyway for you to check!")
    
    # The code to do that:
    """
    import ipinfo
    
    ip_address = None # Insert IP address here to get info on a specific one, if empty returns the host machine ip
    access_token = "The token you get when you register a free account with the service goes in here"
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)
    
    print(f"IP: {details.ip}")
    print(f"postal: {details.postal}")
    print(f"city: {details.city}")
    print(f"region: {details.region}")
    print(f"country: {details.country}")
    print(f"loc: {details.loc}")
    print(f"org: {details.org}")
    print(f"postal: {details.postal}")
    print(f"timezone: {details.timezone}")
    """
    
def printDeleteAccountTrialInfoText(trial):
    print("For your security, The Evil Corp™ requires your login information for this operation.")
    print(f"You have {trial} chances to enter the correct credentials.")
    print("In the event of not providing the correct information, please remain seated wherever you are")
    print("until the security forces join you for interrogation.")
    print("Please remember: There is nowhere to hide from The Evil Corp™. :)")
    
# UTILITY FUNCTIONS (HW2)


"""Checks the validity of the username

Parameters
----------
username : String
    Username info to check

Returns
-------
Bool -> Whether the username is acceptable or not
"""
def checkUsername(username):
    #TODO: I probably should set up some limitations for the username - password stuff
    #ex: character type, length etc
    
    if (len(username) == 0) or (username.isspace()):
        print("Username must have at least a single character that isn't a whitespace character!")
        print("Returning to the previous Menu...\n")
        return False
    
    return True
    
"""Checks the validity of the password

Parameters
----------
password : String
    Password info to check

Returns
-------
Bool -> Whether the password is acceptable or not
"""
def checkPassword(password):
    #TODO: I probably should set up some limitations for the username - password stuff
    #ex: character type, length etc
    
    if (len(password) == 0):
        print("Password must have at least a single character!")
        print("Returning to the previous Menu...\n")
        return False
    
    return True

"""For receiving the user input for username / password

Parameters
----------
None

Returns
-------
String, String, Bool -> "username, password" pair and whether there was a problem with the input or not
"""
def receiveAccountInfoFromUser():
    password = "Invalid"
    username = input("Please enter your username: ")
    if(not checkUsername(username)):
        return username, password, False
    
    password = input("Please enter your password: ")
    if(not checkPassword(password)):
        return username, password, False
    
    return username, password, True