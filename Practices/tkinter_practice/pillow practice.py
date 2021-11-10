from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Album")
photo1 = PhotoImage(file="amazon.png")
photo2 = PhotoImage(file="facebook.png")
photo3 = PhotoImage(file="google.png")
photo4 = PhotoImage(file="youtube.png")
label1 = Label(root, image=photo1).grid(row=0, column=0)
label2 = Label(root, image=photo2).grid(row=0, column=1)
label3 = Label(root, image=photo3).grid(row=0, column=2)
label4 = Label(root, image=photo4).grid(row=0, column=3)

root.mainloop()