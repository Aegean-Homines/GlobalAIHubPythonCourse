#Explain your work
"""
NOTES:
1. I used students.json file to test, easier that way
Set "USE_FILE = True" if that's the preferred way
Set to False by default for hand input

FLOW:
    1. Created a student class to hold the fields and calculate passing grade
    2. I create an instance for each entry, then store them in a map "StudentName" : "StudentClass"
        a. This could also be done without a class by mapping "StudentName" : List of grades
        Check students.json, that's the format I'm storing them in anyway
        It's actually smarter to go that way cause storing student name doesn't really serve any purpose as a field in the class
        Since I'm also using the name for map keys, it just wastes memory. 
        Then why did I do that? Basically to retain the name information when I add them to the list. (Explanation below)
        b. I think the better way of going with classes would be to insert them into a set instead of a map.
        Key value is worthless and just wastes memory as explained before
        Since I'm storing the names inside the class, I could just retrieve them when I'm printing them (which is the only time to use them anyway)
    3. After that, I insert each student instance from the map to the list in order
    4. Finally I use reverse sort by using the passing grade as the comparison function to sort them from highest to lowest
    5. After that, I just print the list to show that they're in different order now
"""


import json # For testing purposes and easier use
import sys # for cmd arguments

STUDENT_FILE_NAME = "students.json"

class Student:
    def __init__(self, name, midtermGrade = 0.0, projectGrade = 0.0, finalGrade = 0.0):
        self.name = name
        self.midtermGrade = midtermGrade
        self.projectGrade = projectGrade
        self.finalGrade = finalGrade
        
    def calculatePassingGrade(self):
        return self.midtermGrade * (0.3) + self.projectGrade * (0.3) + self.finalGrade * (0.4)
        
# Helper func
def registerStudent(studentTable, studentName, midterm, project, final):
    student = Student(studentName, midterm, project, final)
    studentTable[studentName] = student
        
def main():
    # Empty table to hold students
    studentTable = {}
    studentCount = 5

    USE_FILE = False # For testing
    #Input check to see if I should update use_file
    #the second part shouldn't explode in my face if Python is a decent language
    #TODO: Double check that
    if(len(sys.argv) > 1 and sys.argv[1].lower() == "true"):
        USE_FILE = True
    
    # If use file is true, then it reads it from the .json file
    # Mainly cause it was easier for me instead of entering all 5 by hand
    if(USE_FILE):
        studentFile = open(STUDENT_FILE_NAME, "r")
        jsonTable = json.load(studentFile)
        for entry in jsonTable:
            studentName = entry
            midtermGrade = jsonTable[entry][0]
            projectGrade = jsonTable[entry][1]
            finalGrade = jsonTable[entry][2]
            
            registerStudent(studentTable, studentName, midtermGrade, projectGrade, finalGrade)
    else: # If not using the file, then enter 5 student info by hand...
        print(f"Please enter {studentCount} students' information below: ")
        while studentCount > 0:
            studentName = input("StudentName: ")
            midtermGrade = float(input("Student's midterm grade: "))
            projectGrade = float(input("Student's project grade: "))
            finalGrade = float(input("Student's final grade: "))
            
            registerStudent(studentTable, studentName, midtermGrade, projectGrade, finalGrade)
            studentCount -= 1
    
    # TODO: Is there a range.insert for hashmap to list in Python?
    studentList = [] # Holds 5 student objects, inserting one by one
    # Would be smarter to just insert the passing grades then sort them but this way, I keep the names sorted as well
    # So I'm inserting the objects instead. I think it has a better "OOP" flow
    for entry in studentTable:
        studentList.append(studentTable[entry])
        
    # Sort list by passingGrade function
    passingGradeOrdering = Student.calculatePassingGrade
    studentList.sort(reverse = True, key = passingGradeOrdering)
    for entry in studentList:
        print(entry.name.ljust(20, "-") + str(entry.calculatePassingGrade()))
    
    
main()
