import tkinter as tk

import HW1


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
    questionSelectionMenu.add_command(label="Question 1", command=HW1.question1)
    questionSelectionMenu.add_command(label="Question 2", command=HW1.question2)
    homeworkSelectionMenu.add_cascade(label="First Homework", menu=questionSelectionMenu)
    homeworkSelectionMenu.add_separator()
    mainMenu.add_cascade(label="Homework Selection", menu=homeworkSelectionMenu)
    homeworkSelectionMenu.add_command(label="Second Homework")
    homeworkSelectionMenu.add_separator()
    homeworkSelectionMenu.add_command(label="Third Homework")
    homeworkSelectionMenu.add_separator()
    homeworkSelectionMenu.add_command(label="Final Project")
    
    window.config(menu=mainMenu)
    question2Window = tk.Frame(window)
    l = tk.Label(question2Window, text = "The answer: ")
    l.pack()
    
    # HW1 windows
    outputText = tk.Entry(question2Window)
    outputText.pack()
    outputText.insert(tk.END, "Hey")    
    
    question2Window.pack()
    
    showbutton = tk.Button(window, text = "Show", command = lambda: question2Window.pack())
    hidebutton = tk.Button(window, text = "Hide", command = lambda: question2Window.pack_forget())
    showbutton.pack()
    hidebutton.pack()

    
    inp = outputText.get()
    print(inp)
    
    #main render loop
    window.mainloop()
    
showGUI()