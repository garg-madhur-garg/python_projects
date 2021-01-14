"""Python script for search direct from wikipedia (GUI)"""

import wikipedia
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("wikipedia")
root.geometry("225x80")

# Function
def search_wiki():
    search = entry.get()
    answer = wikipedia.summary(search)
    tmsg.showinfo("Wikipedia Answer", answer)


# creating Label

label = Label(root, text="Wikipedia Search:")
label.grid(row=0, column=0)

# create Entry

entry = Entry(root)
entry.grid(row=1, column=0)

# button

button = Button(root, text="Search", command=search_wiki)
button.grid(row=1, column=1, padx=10)

root.mainloop()