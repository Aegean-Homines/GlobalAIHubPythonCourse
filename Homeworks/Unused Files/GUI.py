import tkinter as tk

import Final_Project_GUI as quiz


def showGUI():

    window = tk.Tk()
    
    # window title
    window.title("Super Awesome Homework Selection Tool™")
    
    # window size
    window.geometry("1000x800")
    
    # window color scheme
    #window["bg"] = "black"
    
    #create menu
    mainMenu = tk.Menu(window)
    homeworkSelectionMenu = tk.Menu(mainMenu, tearoff=0)
    questionSelectionMenu = tk.Menu(homeworkSelectionMenu, tearoff=0)
    questionSelectionMenu.add_command(label="Question 1")
    questionSelectionMenu.add_command(label="Question 2")
    homeworkSelectionMenu.add_cascade(label="First Homework", menu=questionSelectionMenu)
    homeworkSelectionMenu.add_separator()
    mainMenu.add_cascade(label="Homework Selection", menu=homeworkSelectionMenu)
    homeworkSelectionMenu.add_command(label="Second Homework")
    homeworkSelectionMenu.add_separator()
    homeworkSelectionMenu.add_command(label="Third Homework")
    homeworkSelectionMenu.add_separator()
    homeworkSelectionMenu.add_command(label="Final Project")
    
    window.config(menu=mainMenu)
    
    # Get questions
    questions = quiz.main()
        
    quizWindow = tk.Frame(window, height = 20, width = 200)
    quizWindow.grid(row = 3, column=2)
    
    quizWindow.pack()
    
    question = tk.Label(quizWindow, text = "quest").grid(row = 0, column = 0)
    answers = tk.Label(quizWindow, text = "ans").grid(row = 1, column = 1)
    
    # HW1 windows
    outputText = tk.Entry(quizWindow, width = 50).grid(row = 2, column = 1)
    
    showbutton = tk.Button(quizWindow, text = "Next", width = 25)
    hidebutton = tk.Button(quizWindow, text = "Prev", width = 25)
    showbutton.grid(row = 3, column = 2)
    hidebutton.grid(row = 3, column = 0)

    isDone = False
    counter = 0
    while not isDone:
        anan = questions[counter]
        question["text"] = anan
        
    
    #main render loop
    window.mainloop()
    
showGUI()