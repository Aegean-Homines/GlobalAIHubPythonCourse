import tkinter as tk

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
    homeworkSelectionMenu.add_command(label="First Homework")
    homeworkSelectionMenu.add_separator()
    mainMenu.add_cascade(label="Homework Selection", menu=homeworkSelectionMenu)
    
    window.config(menu=mainMenu)
    
    
    #main render loop
    window.mainloop()