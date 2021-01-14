from tkinter import *

root = Tk()
root.geometry("500x400")
root.title("Frames")

f1 = Frame(root, bg="grey", borderwidth=7, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root, bg="grey", borderwidth=7, relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l1 = Label(f1, text="this is text in frame 1", bg="grey", fg="white", font="comicsansms 18 bold")
l1.pack(pady=370)
l2 = Label(f2, text="this is text in frame 2", bg="grey", fg="white", font="comicsansms 18 bold")
l2.pack(pady=10)

root.mainloop()
