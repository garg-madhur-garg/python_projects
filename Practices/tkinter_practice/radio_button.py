from tkinter import *

root = Tk()
root.title("Radio Button")

var = IntVar()


r1 = Radiobutton(root, text="india", value=1, variable=var)
r1.pack()

r2 = Radiobutton(root, text="USA", value=2, variable=var)
r2.pack()

r3 = Radiobutton(root, text="UK", value=3, variable=var)
r3.pack()
root.mainloop()