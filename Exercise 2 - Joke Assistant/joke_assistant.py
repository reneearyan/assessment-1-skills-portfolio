import tkinter as tk
import random 

with open("randomJokes.txt", "r") as file: 
    jokes = file.readlines() #this opens the jokes text file and reads all the jokes into a list

def randomJoke(): #this selects a random joke from the list and displays it in the joke_label
    global current_punchline

    joke = random.choice(jokes).strip() #this selects a random joke and removes whitespace from the beginning and end of the joke
    parts = joke.split("?", 1) #this splits the joke into two at the first question mark 

    setup = parts[0] + "?" #this adds the question mark back to the setup
    current_punchline = parts [1]

    joke_label.config(text=setup)
    punchline_label.config(text="") #this clears the punchline label so that it doesn't show the previous punchline

def showPunchline(): #this displays the punchline of the joke
    punchline_label.config(text=current_punchline) #this puts the punchline into the punchline label

def quitApp(): #this closes the application
    window.destroy()

#this creates the main application window
window = tk.Tk() 
window.title("Joke Assistant")
window.geometry("400x200")
window.config(bg="lightblue")

#this creates the title label, joke label, and punchline label
title_label = tk.Label(window, text="Welcome to the Joke Assistant!", font=("Arial", 16, "bold"), bg="lightblue")
title_label.pack(pady=15)

#this creates the joke label that will display the joke setup
joke_label = tk.Label(window, text="Click the button to hear a joke!", font=("Arial", 12), bg="lightblue", wraplength=400)
joke_label.pack(pady=15)

#this creates the label where the punchline will appear
punchline_label = tk.Label(window, text="", font=("Arial", 12, "italic"),bg="lightblue",wraplength=400)
punchline_label.pack(pady=10)

#this creates the button that displays a random joke
joke_button = tk.Button(window, text="Alexa tell me a Joke", command=randomJoke)
joke_button.pack(pady=5)

#this creates the button that displays the punchline
punchline_button = tk.Button(window, text="Show Punchline", command=showPunchline)
punchline_button.pack(pady=8)

#this creates the button to get another random joke
next_button = tk.Button(window, text="Next Joke", command=randomJoke)
next_button.pack(pady=5)

#this creates the button to quit the application
quit_button = tk.Button(window,text="Quit", command=quitApp)
quit_button.pack(pady=8)

current_punchline = "" #this stores the punchline before a joke is selected

window.mainloop() #this keeps the application window running