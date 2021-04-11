import random # for generating list content
import math # for ceil

# HOW TO RUN:
# I created two functions for each question
# The main app is a function array. Takes input from the user then uses that as an index
# to run the question code
# If this is a bother then you can just call the functions questionX()
# The input-taking works in a while loop so you can test it with different inputs for each question
# type Exit (not case sensitive, I'm lower casing the input string) or Ctrl+C to quit the loop

#Explain your work
# First question is basically index based swapping
# I tried a few approaches, explained in detail in comments

# For the second question, the main question focuses on single digit positive integers
# The code itself works for any number and I didn't limit it
# However, I did put code blocks as comments to describe how to test single digit and/or positive integer
# inputs. The remaining code, however, works with any value (positive, negative, single or multi digit integers)
# The main logic is simple: %2 for even check, add numbers to a list for better looking formatting
# We could print numbers directly to the output as well (or to a string) but adding them to a list resulted in
# a few other interesting ways to implement the solution


"""
Steps:
    First question:
    Create a list
        std::generate with randomly generated values
        find the python version of this
        if not, create in a loop with incremental values
        or something
    Swap the second half
        C++ has std::swap_range, look for python equivalent
        if not, loop through and swap (a,b = b,a)
    Print the list
    
    Second question:
    n = input
        check if n is integer
            maybe casting throws an exception?
            if not, check to see if it's an integer
            in an endless loop
        check for empty inputs
    print out all the even numbers from 0 to n (including n)
        negative numbers? integer can be negative in this case
        do n to 0
        assume n is integer sized
        

    
"""

# FUNCTIONS FOR THE SWAP OPERATION IN THE FIRST QUESTION
# swap by looping through the list regularly
def basicswap(inlist):
    
    # get the size of the list
    size = len(inlist)
    
    # half index is ceiled for handling the odd number of elements case
    halfIndex = math.ceil(size / 2.0)
    forwardIter = 0
    
    # loop until halfIndex reaches the length
    while(halfIndex < len(inlist)):
        inlist[forwardIter], inlist[halfIndex] = inlist[halfIndex], inlist[forwardIter]
        # increment loop invariant and the index operator
        halfIndex+=1
        forwardIter+=1


# swap by using slice and step functionality:
# logic: https://stackoverflow.com/questions/39167057/better-way-to-swap-elements-in-a-list
# a[start:end:step] start through not past end, by step
def sliceswap(inlist):
    
    # get the size of the list
    size = len(inlist)
    
    # half index becomes the beginning index of the second half
    halfIndex = math.ceil(size / 2.0)

    # end of loop index condition for the forward iterator
    # floored to define the mid index 
    endIndex = math.floor(size / 2.0)    

    inlist[0:endIndex:1], inlist[halfIndex::1] = inlist[halfIndex::1], inlist[0:endIndex:1]

# Question 1
def question1():
    # Create a list:
    # list size
    size = random.randint(1, 10)
    
    """
    generating the list by looping:
        
    # create the list
    mylist = []
        
    # append a random number from 1 to 100, for 1 to 10 times
    for i in range(size):
        mylist.append(random.randint(1,100))
    """
    
    # generating the list by using random.sample (apparently this is a thing)
    mylist = random.sample(range(1,100), size)
    
    print(f"List before swapping: {mylist}")
    basicswap(mylist) # sliceswap also works but basicswap feels more natural to me
    print(f"List after swapping: {mylist}")

# ----------------------------------------------------------------------------------------------------
# Question 2
def question2():
    # Get the input and store it in a variable as integer
    """
    NOTE: So python apparently has this weird thing:
        if I get a string and try to convert it to an integer, if the string has decimals
        then it throws a ValueError instead of implicitly casting it to an integer
        I call shenanigans on this honestly. However, float doesn't create any problems
        So I'm casting to float then cast it to an integer. Feels hack-y but that's life
    """
    
    #convert to float
    while True:
        try:
            value = float(input("Please enter a single digit integer: "))
            break
        except ValueError: # Will catch if the input is NaN
            print("The input is incorrect")
            
    # cast to int
    value = int(value)
    
    """
    # SINGLE DIGIT CHECK!!
    # Check if the input is not single digit
    valueToCheck = abs(value)
    if int(valueToCheck / 10) > 0: # check if it's not single digit
        raise ValueError("The input must be a single digit number!")
        
    """
    
    """
    # NEGATIVE VALUE CHECK
    if(value < 0):
        raise ValueError("The input must be a positive number!")
    """
        
    # find the lower and upper bounds for the loop
    # since it'll be from min to max indices
    firstIndex = min(value, 0)
    lastIndex = max(value, 0)
    
    # THE FOLLOWING IF BLOCK IS PREMATURE OPTIMIZATION
    # We can skip this if we're following single-step algorithms below
    # Or if we're filtering the input by positives in the code block in line 139
    
    # I'm checking if the first value is odd. This is a case scenario if the input is negative.
    # if it is, then I can shift it to the nearest even number and then step two by two in the loop
    # if it's [0, value] then I always start at an odd number so I can just
    # skip to stepping two by two without incrementing
    if(firstIndex % 2 != 0): # odd number
        firstIndex += 1
    
    
    # LOOP VERSION WITH SINGLE STEP:
    # Loop through all elements, check if each is divisible by two
    # Found a compact way of doing the if statement (check the SO link)
    # We can also push all the values to a list then use the filter as explained in the link
    # But that's filling a list then removing elements, which will most certainly do some element shifting
    # We can also just not use a list and print the values normally but where's the fun in that?
    # However, modular operation is expensive so single step is not good
    # Also, since lists are dynamic arrays, creating a list with just firstIndex then doing += must be introducing some cost
    # for the initial allocation of memory
    """
    evenList = []
    while not firstIndex > lastIndex:
        evenList += [firstIndex] if firstIndex % 2 == 0 else [] # https://stackoverflow.com/questions/8826521/python-avoiding-if-condition-for-this-code
        firstIndex += 1
        
    """
    
    # LOOP VERSION WITH MULTI STEP:
    # If I do the initial firstIndex check above, I can just keep adding to the list two by two
    # starting from firstIndex to lastIndex
    # Why? Because division is more expensive than multiplication for CPUs and mod operand is quite expensive
    # This way, we don't do '%2' operation in every step of the loop. We do it once, filter out the data then skip odd numbers
    # by stepping twice
    """
    evenList = []
    while not firstIndex > lastIndex:
        evenList.append(firstIndex)
        firstIndex += 2
    
    print(evenList)
    """
    
    # SINGLE-STEP SLIGHTLY LESS FUN ALGORITHM WITH THE COOL NEW TECHNOLOGY CALLED LIST COMPREHENSION™
    # Slightly less fun due to using single step
    # Mod is expensive, doing mod at every iteration is bad
    # In the class we're told that this method was cool. And it did look cool.
    # If something is told to be cool and then also looks cool then it must be cool
    # So I'm doing that. Partially cause I did that and it feels quite satisfying to do the whole thing in one line
    # evenlist = [number for number in range(firstIndex, lastIndex + 1) if number % 2 == 0]
    
    # MULTI-STEP GENUINELY FUN ALGORITHM WITH THE COOL NEW TECHNOLOGY CALLED LIST COMPREHENSION™
    # Genuinely Fun™
    # It's basically the idea above, however this time I'm combining that with the odd number shifting I did above with the firstIndex
    # This way I can skip the second if part in comprehension and just create the list by range(firstIndex, lastIndex, stepValue)
	# That if is gonna run 50% of the time. Skipping that if means skipping a whole bunch of cache misses so in theory this should be quite useful
	# for larger datasets
    
    evenlist = [number for number in range(firstIndex, lastIndex + 1, 2)]
    print(evenlist)


# Main app

def main():
    Tests = [question1, question2]
    
    welcomeLine = "Please enter the question you want to test (1 for question 1, 2 for question 2 etc)\n"
    welcomeLine += "If you want to exit the app, please type \"Exit\" or \"Ctrl+C\": "
    while True:
        
        option = input(welcomeLine)
        
        if(option.lower() == "exit"):
            print("See ya!")
            break
        else:
            try:
                option = int(option)
            except ValueError:
                print("Invalid value\n")
                continue
            
        if(option > 2 or option < 1):
            print("Please enter the correct numeric value as input.")
            continue
        
        Tests[option-1]()

try:
    print("nothing")
    #main()
except KeyboardInterrupt:
    print("\nGoodbye!")