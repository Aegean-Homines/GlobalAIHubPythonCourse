# Steps
"""
GENERAL FLOW:
1. Entry function is main
2. The code explains the rules, then ask 10 questions.
3. Each question then is compared with the correct answer using ==
    Since the rule is to pay attention to the case sensitivity, I'm not using .lower() before comparing them
4. Each correct answer increases score by one
5. After all the questions, I print the score information (and score * 10 since each question is 10 points)
6. Then check if the score is <= 5 to determine whether the user is successful or not

FUN PART:
In general the app is pretty straightforward. However, straightforward is boring.
Since the goal is to learn, I decided to look for any API that maybe generating randomized trivia questions.
And I found one that just does this (link below in the "url" variable)
Since the API returns a url that responds in json format, I decided to try the request library, which apparently handles the html stuff
So I used the url with the library to get the json response, then used the json library to parse it into questions and answers

The reply comes with the correct_answer and wrong_answers fields separated. Because of that, I'm using a randomInt(0,3) to insert
the correct answer into the wrong_answers list to generate an all_answers list, then print that to create the illusion of multiple choice exam
The rest is as described above, kinda anti-climactic

To use the above fun part, Set USE_RANDOM_TRIVIA_GENERATOR = True or launch the program with "True" argument
Setting USE_RANDOM_TRIVIA_GENERATOR = False uses the default base questions. Since I already had the json code in, I copy-pasted one of the json replies from the API
and changed the questions and answers. After that, just used that as a string (in questions.py) to json-parse it and re-used the rest of the code
"""

import json
import sys
import requests # For retrieving trivia questions
import random # for building potential answer list
from html import unescape
import questions # for keeping the default questions as a line



GENERATED_QUESTION_FILENAME = "generatedquestions.json"

# Apparently opentdb generates x number of trivia questions in any specific field
url = "https://opentdb.com/api.php?amount=10&type=multiple"

# Added some Turkish questions, in case the internet is down or something


def main():
    USE_RANDOM_TRIVIA_GENERATOR = True
    # before beginning, check if the program has an argument. If it does, set the trivia behavior to it
    if len(sys.argv) > 1:
        argument = sys.argv[1]
        if(argument.lower() == "true"):
            USE_RANDOM_TRIVIA_GENERATOR = True
        elif(argument.lower() == "false"):
            USE_RANDOM_TRIVIA_GENERATOR = False
            
    # Introduction part explaining the rules
    print("WELCOME TO THE DIFFICULTRIVIA HOSTED BY THE EVIL CORP™!!!")
    print("You will be asked 10 questions.")
    print("If you answer more than questions, you get to keep your lif- I mean you get rewarded with bonuses!")
    print("However if you answer 5 or lesser questions...well let's just say that you'll find out why some of your coworkers quit the job quite suddenly.")
    print("BE CAREFUL! Since evaluating answers to these questions could be automated, and therefor would be cheaper for the Corp™, we automated them.")
    print("As a result, if you answer them without paying attention to their case sensitivity, the machine might register your correct answers as mistakes.")
    print("I don't know about you but if I know one thing, it's that sharks living in the pool under your chair right now only cares about whether you get at least 5 answers right or wrong.")
    print("So each answer counts. Let us BEGIN!!!")
    
    #response will hold the parsed result of json
    response = None
    # Using the Trivia generator API
    if(USE_RANDOM_TRIVIA_GENERATOR):
        # get the json file of the questions
        response = json.loads(requests.get(url).text)
        
        # If we want to pretty-store the json response
        # I'm storing them cause, you know, cheating
        # Let's be honest: testing this without an answer sheet would be hell
        # If anything, I should get extra points for this favor
        jsonFile = open(GENERATED_QUESTION_FILENAME, "w")
        json.dump(response, jsonFile, sort_keys=True, indent = 4)
        jsonFile.close()
    else: # Using default questions (this part is genuinely boring)
        fakeresponse = json.dumps(questions.defaultQuestions)
        response = json.loads(fakeresponse)
        
    score = 0
    # TODO: Apparently, there's something called object_hook that works with json.loads to automatically
    # map json objects to python classes, like Java Spring beans
    # However, I don't know the details, if I have some time left, let's check this out
    # instead of manually doing this
    for entry in response["results"]:
        # Parse the entry fields into their own parameters
        question = unescape(entry["question"])
        correctAnswer = unescape(entry["correct_answer"])
        potentialAnswers = unescape(entry["incorrect_answers"])
    
        # get a random int to insert the correct answer to
        potentialAnswers.insert(random.randint(0, 3), correctAnswer)
        
        # The asking part
        print(f"\nQuestion: {question}")
        print("Answers: ")
        for choice in potentialAnswers:
            print(choice.ljust(5))
            
        answer = input("What is your answer?\n")
        score += 1 if answer == correctAnswer else 0
        
    # Result
    print(f"\nThe competition is over! Your answered {score} questions correctly!")
    score *= 10
    print(f"Which means you got {score} points in total!!")
    if(score <= 5):
        print("The result: YOU LOSE")
        print("Ooof just short of 5! Well, it looks like you're going on a holiday after your colleagues. Good for the sharks I guess...")
    else:
        print("The result: YOU WIN")
        print("Ooooh boi! Someone has a 200 IQ big brain! Well, you win I guess. What are you waiting for, a prize? Your employment is prize enough in itself, GET BACK TO WORK!")

main()
