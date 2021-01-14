from tkinter import *
from gtts import gTTS
from playsound import playsound
root = Tk()
root.title("Text to Speech")
root.geometry("200x70")

# Function
def text_to_speech():
    text = entry.get()
    speech = gTTS(text=text, lang='en')
    speech.save(r'C:\Users\MADHUR\Desktop\speech.mp3')
    playsound(r'C:\Users\MADHUR\Desktop\speech.mp3')


# create label
label = Label(root, text="Enter Here: ")
label.grid(row=0, column=0)

# create Entry Box
entry = Entry(root)
entry.grid(row=1, column=0)

# create button
button = Button(root, text="Go", command=text_to_speech)
button.grid(row=1, column=1, padx=10)


root.mainloop()