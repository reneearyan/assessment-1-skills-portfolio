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
window.geometry("500x500")
window.config(bg="#FFF4CC")

#this creates the title label, joke label, and punchline label
title_label = tk.Label(window, text="Welcome to the Joke Assistant!", font=("Arial", 18, "bold"), bg="#FFF4CC", fg="#8A6D3B")
title_label.pack(pady=20)

#this creates the joke label that will display the joke setup
joke_label = tk.Label(window, text="Click the button to hear a joke!", font=("Arial", 13), bg="#FFFDF5",fg="#5C5142", wraplength=380, width=38, height=4)
joke_label.pack(pady=15, padx=20)

#this creates the label where the punchline will appear
punchline_label = tk.Label(window, text="", font=("Arial", 12, "italic"),bg="#FFFDF5",fg="#A078A0", wraplength=380, width=38, height=3)
punchline_label.pack(pady=10, padx=20)

#this creates the button that displays a random joke
joke_button = tk.Button(window, text="Alexa tell me a Joke", command=randomJoke, font=("Arial", 11, "bold"), bg="#E8D5F2", fg="#5C456B", activebackground="#D8BCE8", relief="flat", padx=15, pady=8, cursor="hand2")
joke_button.pack(pady=8)

#notes:
#activebackground is the color when the button is clicked
#relief="flat" removes the traditional button border
#cursor="hand2" changes the cursor to a hand when hovering over the button

#this creates the button that displays the punchline
punchline_button = tk.Button(window, text="Show Punchline", command=showPunchline, font=("Arial", 11, "bold"), bg="#F7DDE8", fg="#754B60", activebackground="#EFC5D8", relief="flat", padx=15, pady=8, cursor="hand2")
punchline_button.pack(pady=8)

#this creates the button to get another random joke
next_button = tk.Button(window, text="Next Joke", command=randomJoke, font=("Arial", 11, "bold"), bg="#DDEBDD", fg="#496849", activebackground="#C5DCC5", relief="flat", padx=15, pady=8, cursor="hand2")
next_button.pack(pady=5)

#this creates the button to quit the application
quit_button = tk.Button(window,text="Quit", command=quitApp, font=("Arial", 10, "bold"), bg="#F5D6CC", fg="#804F43", activebackground="#EABFB2", relief="flat", padx=15, pady=7, cursor="hand2")
quit_button.pack(pady=8)

current_punchline = "" #this stores the punchline before a joke is selected

window.mainloop() #this keeps the application window running