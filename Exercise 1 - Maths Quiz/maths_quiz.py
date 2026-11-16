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

attempts = 0 #this will count the player's attempts

score = 0 #this keeps track of the player's points

question_count = 0 #this counts how many questions the player has answered 

welcome_label = tk.Label(window, text="Welcome to the Maths Quiz!") #this displays the welcome message at the top of the window
welcome_label.pack(pady=20) #this places the welcome message inside the window

number_label = tk.Label(window, text="") #this label displays the random number for the quiz 
number_label.pack(pady=10)

feedback_label = tk.Label(window, text="")
feedback_label.pack(pady=5)

answer_entry = tk.Entry(window) #this creates a box where the player can type their answer
answer_entry.pack(pady=10)

def isCorrect(player_answer): #this checks if the player's answers matches the correct answer
    return player_answer == correct_answer

def getAnswer(): #this function retrieves the answer by the player 
    global attempts, score #this updates the counter and score created outside the function
    
    player_answer = answer_entry.get()

    if player_answer.lstrip("-").isdigit(): #this allows whole numbers with or without a negative sign
        player_answer = int(player_answer) #this converts the text into a whole number
        attempts+= 1 #increases the cunter by one for each valid answer
        
        if isCorrect(player_answer): #this checks the answer using the isCorrect function
            if attempts == 1: 
                score += 10 #this adds 10 points to the score
                feedback_label.config(text="Correct! You earned 10 points!")
            else:
                score += 5
                feedback_label.config(text="Correct! You earned 5 points.")

            submit_button.config(state="disabled") #this stops the player from submitting another answer
            window.after(1000, displayProblem) #this waits for 1 second before running the next section
        elif attempts == 1:
            feedback_label.config(text="Sorry, please try again. You have one more attempt left.")
        else:
            feedback_label.config(text=f"Sorry, both attempts were incorrect. The correct answer was: {correct_answer}")
            submit_button.config(state="disabled")
            window.after(1500, displayProblem)
    else:
        feedback_label.config(text="Please enter a valid whole number.")

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


def displayResults(): #this checks the score range and assign the correct grade
    number_label.config(text="Quiz Completed!")
    feedback_label.config(text=f"Your final score is {score}/100")

    if score > 90: 
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    feedback_label.config(text=f"Your final score is {score}/100. Your grade is {grade}.")

def replay():
    global score, question_count, difficulty 

    score = 0 #this resets the player's score
    question_count = 0 #this resets the question counter
    difficulty = ""
    
    answer_entry.delete(0, tk.END) #this clears the answer box
    feedback_label.config(text="Choose a difficulty to play again.")
    number_label.config(text="Welcome back!")
    submit_button.config(state="normal")

def displayProblem():
    global correct_answer
    global attempts
    global question_count

    if question_count== 10:
        displayResults() 
        return

    question_count += 1
    attempts = 0

    answer_entry.delete(0,tk.END) #this clears the previous answer
    submit_button.config(state="normal") #this enables the submit button again

    number = randomInt()
    number2 = randomInt()
    operation = decideOperation()

    if operation == "+": 
        correct_answer = number + number2
    else:
        correct_answer = number - number2
        
    question = f"Question {question_count}/10: {number} {operation} {number2} = ?"
    number_label.config(text=question)
    feedback_label.config(text="" )

def displayMenu(): #this displays the instructions for choosing a quiz difficulty
    menu_label = tk.Label(window, text="Choose your difficulty:")
    menu_label.pack(pady=10)

#these buttons let the player choose the difficulty of the quiz
def chooseEasy(): #this function runs when the player clicks Easy
    global difficulty, score, question_count

    difficulty = "Easy"
    score = 0
    question_count = 0

    displayProblem() #this generates and displays a new question

    print("Easy mode selected.") 
    print("Selected mode:", difficulty)

def chooseModerate(): #this function runs when the player clicks Moderate
    global difficulty, score, question_count
    
    difficulty = "Moderate"
    score = 0
    question_count = 0

    displayProblem()

    print("Moderate mode selected.")
    print("Selected mode:", difficulty)

def chooseAdvanced(): #this function runs when the player clicks Advanced
    global difficulty, score, question_count
    
    difficulty = "Advanced"
    score = 0
    question_count = 0

    displayProblem() 

    print("Advanced mode selected.")
    print("Selected mode:", difficulty)

displayMenu()

easy_button = tk.Button(window, text="Easy", command=chooseEasy)
easy_button.pack(pady=5)

moderate_button = tk.Button(window, text="Moderate", command=chooseModerate)
moderate_button.pack(pady=5)

advanced_button = tk.Button(window, text="Advanced", command=chooseAdvanced)
advanced_button.pack(pady=5)

replay_button = tk.Button(window, text="Play Again", command = replay) #this creates a button to restart the quiz
replay_button.pack(pady=5)

window.mainloop() #this keeps the window open so the user can interact with it