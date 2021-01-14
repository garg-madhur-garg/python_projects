from tkinter import *

root = Tk()
root.geometry("500x400")


def resize():
    root.geometry(f"{widthvalue.get()}x{heightvalue.get()}")


frame = Frame(root)
l3 = Label(frame, text="Window Resizer", font="comicsansms 18 bold", fg="red").grid(row=0, column=0, columnspan=2)
l1 = Label(frame, text="Width:", font="comicsansms 10 bold").grid(row=1, column=0, pady=5, padx=3)
l2 = Label(frame, text="Height:", font="comicsansms 10 bold").grid(row=2, column=0, padx=3)

widthvalue = IntVar()
heightvalue = IntVar()

Entry(frame, textvariable=widthvalue).grid(row=1, column=1, pady=5)
Entry(frame, textvariable=heightvalue).grid(row=2, column=1)
Button(frame, text="Apply", command=resize).grid(row=3, column=0, columnspan=2, pady=5)

frame.pack(expand=TRUE)
root.mainloop()
