"""This program will give you the weather information of all cities"""
from tkinter import *
import requests
import json

root = Tk()
root.geometry("300x200")
root.title("Weather Details")


# Functions
def weather_details():
    location = entry.get()



# Creating label
label = Label(root, text="Enter City Name Here: ", bg="powderblue", font="lucida 10 bold")
label.grid(row=0, column=0)

# Creating Entry Box
entry = Entry(root)
entry.grid(row=1, column=0)

# Creating Button
button = Button(root, text="Search", command=weather_details)
button.grid(row=1, column=1, padx=10)

root.mainloop()