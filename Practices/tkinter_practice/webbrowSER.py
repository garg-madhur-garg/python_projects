""" Make your own webbrowser using python(GUI)"""

from tkinter import *
import webbrowser

root = Tk()
root.geometry("400x300")
root.title("Webbrowser")


# Functions
def google():
    webbrowser.open("www.google.com")


def facebook():
    webbrowser.open("www.facebook.com")


def amazon():
    webbrowser.open("www.amazon.com")


def youtube():
    webbrowser.open("www.youtube.com")


igoogle = PhotoImage(file="google.png")
google = Button(root, image=igoogle, command=google)
google.grid(row=0, column=0)

ifacebook = PhotoImage(file="facebook.png")
facebook = Button(root, image=ifacebook, command=facebook, height=400, width=400)
facebook.grid(row=0, column=1)

iamazon = PhotoImage(file="amazon.png")
amazon = Button(root, image=iamazon, command=amazon)
amazon.grid(row=1, column=0)

iyoutube = PhotoImage(file="youtube.png")
youtube = Button(root, image=iyoutube, command=youtube)
youtube.grid(row=1, column=1)

root.mainloop()
