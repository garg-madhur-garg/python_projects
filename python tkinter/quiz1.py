import os
from tkinter import *
os.chdir("C://Users/MADHUR/Desktop/Photos")
content = os.listdir()

root = Tk()
root.geometry("844x540")
root.title("PNG Photos")
photos = []
for i in range(1, 10):
    image = photos.append(PhotoImage(file=f"{i}.png"))
    label = Label(image).pack()
root.mainloop()

