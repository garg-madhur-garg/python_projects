from tkinter import *
root = Tk()
root.geometry("800x500")

def getvals():
    print(f"username: {userinp.get()}")
    print(f"password: {passwordinp.get()}")

l1 = Label(root, text="This is dance class form:", font="comicsansms 18 bold", fg="red")
l2 = Label(root, text="Please enter your details", font="default 10 bold")
l1.grid(row=0, rowspan=2, columnspan=2)
l2.grid(row=5, rowspan=2, columnspan=2)

userinp = StringVar()
passwordinp = StringVar()

userentry = Entry(root, textvariable=userinp)
userentry.grid(row=8, column=1)
passentry = Entry(root, textvariable=passwordinp)
passentry.grid(row=14, column=1)


l3 = Label(root, text="Username").grid(row=8, column=0)
l4 = Label(root, text="Password").grid(row=14, column=0)
b1 = Button(root, text="Submit", command=getvals).grid(pady=10, row=18, column=0)
root.mainloop()
