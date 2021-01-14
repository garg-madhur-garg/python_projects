from tkinter import *
root = Tk()
root.geometry("800x500")
root.title("Working buttons")


def b1stuff():
    print("So now i learn buttons")


def b2stuff():
    print("Receive")


def b3stuff():
    print("Sending")


def b4stuff():
    print("Updating")


f1 = Frame(root, bg="grey", borderwidth=8, relief=SUNKEN)
f1.pack(side=TOP)

b1 = Button(f1, text="Printing Something", fg="red", padx=20, command=b1stuff).pack(side=LEFT, padx=20)
b2 = Button(f1, text="Receiving Something", fg="red", padx=20, command=b2stuff).pack(side=LEFT, padx=20)
b3 = Button(f1, text="Sending Something", fg="red", padx=20, command=b3stuff).pack(side=LEFT, padx=20)
b4 = Button(f1, text="Updating Something", fg="red", padx=20, command=b4stuff).pack(side=LEFT, padx=20)

root.mainloop()