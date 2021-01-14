"""This is translator which convert from any language to any language"""

from tkinter import *
from googletrans import Translator

root = Tk()
root.geometry("200x100")
root.title("Translator")

# Function
def translation():
    text = entry.get()
    translator = Translator(service_urls=["translate.google.com"])
    translation1 = translator.translate(text, dest="hindi")
    label1 = Label(root, text=f"Translated in russian: {translation1.text}", bg="yellow")
    label1.grid(row=2, column=0)


# Creating Label
label = Label(root, text="Enter word:")
label.grid(row=0, column=0)

# Creating Entry Box
entry = Entry(root)
entry.grid(row=1, column=0)

# Creating Button
button = Button(root, text="Translate", command=translation)
button.grid(row=1, column=1)

root.mainloop()