import tkinter as tk
import random 

with open("randomJokes.txt", "r") as file: 
    jokes = file.readlines() #this opens the jokes text file and reads all the jokes into a list