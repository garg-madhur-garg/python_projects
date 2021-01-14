from tkinter import *

root = Tk()
root.geometry("200x100")


def getval():
    print("values submitted")
    print(f"Username: {uservalue.get()}")
    print(f"Password: {passvalue.get()}")


Label(root, text="Username").grid(row=0, column=0)
Label(root, text="Password").grid(row=1, column=0)
uservalue = StringVar()
passvalue = StringVar()

Entry(root, textvariable=uservalue).grid(row=0, column=1)
Entry(root, textvariable=passvalue).grid(row=1, column=1)
b1 = Button(root, command=getval, text="Submit").grid(row=3, column=0, columnspan=2)

root.mainloop()