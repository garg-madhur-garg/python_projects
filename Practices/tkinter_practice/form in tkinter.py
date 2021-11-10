from tkinter import *
import tkinter.messagebox as tmsg


def onclick():
    print(f"Full Name: {nameinput.get()}\n"
          f"Email ID: {emalinput.get()}")
    tmsg.showinfo("Registering", "Thank you for register with us.")


root = Tk()
root.geometry("450x200")
root.title("python course form")
f1 = Frame(root, relief=SUNKEN, borderwidth=1, )
l1 = Label(f1, text="Python course form", font="lucida 20 bold", fg="red").grid(row=0, column=0, columnspan=2)
l2 = Label(f1, text="Enter your details", font="lucida 12 bold").grid(row=1, column=0, columnspan=2)
l3 = Label(f1, text="Full Name", font="lucida 9 bold").grid(row=2, column=0, pady=5)
l4 = Label(f1, text="Email ID", font="lucida 9 bold").grid(row=3, column=0, pady=5)

nameinput = StringVar()
emalinput = StringVar()

e1 = Entry(f1, textvariable=nameinput, bd=5).grid(row=2, column=1, pady=5)
e2 = Entry(f1, textvariable=emalinput).grid(row=3, column=1, pady=5)

b1 = Button(f1, text="Submit", command=onclick, font="lucida 10 bold", cursor = "circle").grid(row=4, column=0, columnspan=2, pady=5)
f1.pack(pady=8)

root.mainloop()
