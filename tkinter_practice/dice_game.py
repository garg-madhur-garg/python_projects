from tkinter import *
import random
import tkinter.messagebox as tmsg

root = Tk()


def play():
    random_number = random.randint(1, 6)
    number.config(text=f"Number is : {random_number}")
    if random_number == 6:
        tmsg.showinfo("Congratulations", "You Won !!")


number = Label(root)
number.pack(pady=10)

play = Button(root, text="Play", command=play)
play.pack(padx=50)
root.mainloop()