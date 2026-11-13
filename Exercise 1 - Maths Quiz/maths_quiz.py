"""
This is my Maths Quiz program where I will be using Tkinter
to create a graphical window for the quiz.
"""
import tkinter as tk

window =tk.Tk() #this creates the main window of the program
window.title("Maths Quiz") #this sets the title at the top of the window
window.geometry("500x400") #this controls the size of the window

welcome_label = tk.Label(window, text="Welcome to the Maths Quiz!") #this displays the welcome message at the top of the window
welcome_label.pack(pady=20) #this places the welcome message inside the window

#these buttons let the player choose the difficulty of the quiz
def chooseEasy(): #this function runs when the player clicks Easy
    print("Easy mode selected.") 
easy_button = tk.Button(window, text="Easy", command=chooseEasy)
easy_button.pack(pady=5)

def chooseModerate(): #this function runs when the player clicks Moderate
    print("Moderate mode selected.")
moderate_button = tk.Button(window, text="Moderate", command=chooseModerate)
moderate_button.pack(pady=5)

def chooseAdvanced(): #this function runs when the player clicks Advanced
    print("Advanced mode selected.")
advanced_button = tk.Button(window, text="Advanced", command=chooseAdvanced)
advanced_button.pack(pady=5)

window.mainloop() #this keeps the window open so the user can interact with it