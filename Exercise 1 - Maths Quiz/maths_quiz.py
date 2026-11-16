"""
This is my Maths Quiz program where I will be using Tkinter
to create a graphical window for the quiz.
"""
import tkinter as tk
import random # this is to use python's random number tools

window =tk.Tk() #this creates the main window of the program
window.title("Maths Quiz") #this sets the title at the top of the window
window.geometry("500x400") #this controls the size of the window

difficulty = "" #this stores the difficulty selected by the player

correct_answer = 0 #this creates a variable that will store the correct answer for the next question

welcome_label = tk.Label(window, text="Welcome to the Maths Quiz!") #this displays the welcome message at the top of the window
welcome_label.pack(pady=20) #this places the welcome message inside the window

number_label = tk.Label(window, text="") #this label displays the random number for the quiz 
number_label.pack(pady=10)

answer_entry = tk.Entry(window) #this creates a box where the player can type their answer
answer_entry.pack(pady=10)

def getAnswer(): #this function retrieves the answer by the player 
    player_answer = answer_entry.get()

    if player_answer.isdigit(): #this checks whether the input contains digits
        player_answer = int(player_answer) #this converts the text into a whole number
        if player_answer == correct_answer:
            print("Correct! Good job!")
        else:
            print("Sorry, please try again.")
    else:
        print("Please enter a valid whole number.")

    print("Your answer:", player_answer)

submit_button = tk.Button(window, text="Submit Answer", command = getAnswer) #this button allows the player to submit their answer and calls getAnswer() when the player clicks it
submit_button.pack(pady=10)

def randomInt(): #this function generates a random number based on the difficulty chosen
    if difficulty == "Easy":
        return random.randint(1,9)
    elif difficulty == "Moderate":
        return random.randint(10,99)
    elif difficulty == "Advanced":
        return random.randint(1000,9999)

def decideOperation(): #this function randomly chooses addition or subtraction
    operation = random.choice(["+", "-"])
    return operation

#these buttons let the player choose the difficulty of the quiz
def chooseEasy(): #this function runs when the player clicks Easy
    global difficulty #this is to change the variable created outside the function
    difficulty ="Easy"
    global correct_answer

    number = randomInt() #this function calls another function, randomInt() 
    number2 = randomInt() #this generates a second number for the question
    operation = decideOperation()

    if operation == "+": 
        correct_answer = number + number2
    else:
        correct_answer = number - number2
    
    question = f"{number} {operation} {number2} = ?"
    number_label.config(text=question) #this updates the label to show the question in the window

    print("First number:", number)
    print("Second number:", number2)
    print("Maths question:", question)
    print("Selected operation:", operation) #this randomly selects an operation for the math question
    print("Easy mode selected.") 
    print("Selected mode:", difficulty)
easy_button = tk.Button(window, text="Easy", command=chooseEasy)
easy_button.pack(pady=5)

def chooseModerate(): #this function runs when the player clicks Moderate
    global difficulty
    difficulty = "Moderate"
    global correct_answer

    number = randomInt()
    number2 = randomInt()
    operation = decideOperation()

    if operation == "+": 
        correct_answer = number + number2
    else:
        correct_answer = number - number2
        
    question = f"{number} {operation} {number2} = ?"
    number_label.config(text=question)
    
    print("First number:", number)
    print("Second number:", number2)
    print("Maths question:", question)
    print("Selected operation:", operation)
    print("Moderate mode selected.")
    print("Selected mode:", difficulty)
moderate_button = tk.Button(window, text="Moderate", command=chooseModerate)
moderate_button.pack(pady=5)

def chooseAdvanced(): #this function runs when the player clicks Advanced
    global difficulty
    difficulty = "Advanced"
    global correct_answer

    number = randomInt()
    number2 = randomInt()
    operation = decideOperation()

    if operation =="+":
        correct_answer = number + number2
    else:
        correct_answer = number - number2
    
    question = f"{number} {operation} {number2} = ?"
    number_label.config(text=question)

    print("First number:", number)
    print("Second number:", number2)
    print("Maths question:", question)
    print("Selected operation:", operation)
    print("Advanced mode selected.")
    print("Selected mode:", difficulty)
advanced_button = tk.Button(window, text="Advanced", command=chooseAdvanced)
advanced_button.pack(pady=5)

window.mainloop() #this keeps the window open so the user can interact with it