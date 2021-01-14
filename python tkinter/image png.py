from tkinter import *
# tkinter not suport jpg formate
root = Tk()
root.geometry("1200x988")
photo = PhotoImage(file = "apun.png")
lable = Label(image = photo)
lable.pack()
root.mainloop()