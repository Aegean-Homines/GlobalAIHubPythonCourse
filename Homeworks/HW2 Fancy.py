#Explain your work


import re as regex
from enum import IntFlag, auto

# DATABASE PART = DO IT LATER IF YOU HAVE THE TIME
#import sqlite3 as db
# try to get the saved data from the DB
# def startup(userDict):
#     try:    
#         con = db.connect("login.db")
#     except db.Error as error:
#         errormsg = "Database connection couldn't be established.\n"
#         errormsg += "The error is: \n"
#         errormsg += error.__str__()
#         errormsg += "\nThe cause of the error: \n"
#         errormsg += error.__cause__()
#         errormsg += "\nThe application will use the local file for reference"
#         # DB failed, switch to file reading
#         return False
    
#     # Database worked
    
#     query = "CREATE TABLE USER (id INTEGER, name TEXT, password TEXT);"
#     con.execute(query)
    
#     # Check if this is the first time we're using the db
#     # if so, create new table
#     cursor = con.cursor()

# def storeUserData(username, password):
#     return    


# username rule list
class NamingRules(IntFlag):
    ISALPHA = auto() #[a-zA-Z]
    ISDECIMAL = auto() #[0-9]
    ISSPECIALCHARACTER = auto() #[!-\/:-@\[-`{-~]
    
    
NameruleLookupTable = {
    NamingRules.ISALPHA : "a-zA-Z",
    NamingRules.ISDECIMAL : "0-9",
    NamingRules.ISSPECIALCHARACTER : "!-\/:-@\[-`{-~",
    0 : "" # for when the flag isn't set
    }

def UsernameCheck(username, ruleset):
    regExp = "["
    for rule in NamingRules:
        regExp += NameruleLookupTable[ruleset & rule]
    
    # regExp += "a-zA-Z" if ruleset and NamingRules.ISALPHA else ""
    # regExp += "0-9" if ruleset and NamingRules.ISDECIMAL else ""
    # regExp += "!-\/:-@\[-`{-~" if ruleset and NamingRules.ISSPECIALCHARACTER else ""
    regExp += "]"
    
    # TODO: What's a better way of getting the count?
    result = regex.findall(regExp, username)
    
    return len(result) == len(username)
    
        

# start

while True:
    welcomeMessage = "Welcome to the database of <insert company name here>!\n"
    welcomeMessage += "Please select the operation you want to perform: \n"
    welcomeMessage += "1.\tRegister new user"
    welcomeMessage += "2.\tDelete existing user"
    welcomeMessage += "3.\tList all the users"
    welcomeMessage += "4.\tExit"
    
    chosenOp = input(welcomeMessage)
    if(chosenOp.isdigit() and int(choseOp) < 5)

# Username empty check
if len(username) == 0:
    print("Username cannot be empty")
    
    
if(UsernameCheck(username, NamingRules.ISDECIMAL | NamingRules.ISALPHA)):
    print("Username accepted")

        