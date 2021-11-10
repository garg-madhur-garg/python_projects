from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("Login Form")


def form_loop():
    def b1stuff():
        # print(f"name: {nameinp.get()}")
        # print(f"Age: {ageinp.get()}")
        # print(f"Email ID: {emailinp.get()}")
        with open("Dance_class_members.txt", "a")as f:
            f.write(f"Name: {nameinp.get()}\nAge: {ageinp.get()}\nEmail: {emailinp.get()}\n\n")

    nameinp = StringVar()
    ageinp = IntVar()
    emailinp = StringVar()

    frame = Frame(root)

    Label(frame, text="This is dance class form:", font="comicsansms 18 bold", fg="red").grid(row=0, column=0, columnspan=2)
    Label(frame, text="Enter your details", font="comicsansms 10 bold").grid(row=1, column=0, columnspan=2)

    Label(frame, text="Name").grid(row=2, column=0, pady=7)
    Label(frame, text="Age").grid(row=3, column=0)
    Label(frame, text="Email ID").grid(row=4, column=0, pady=7)

    Entry(frame, textvariable=nameinp).grid(row=2, column=1)
    Entry(frame, textvariable=ageinp).grid(row=3, column=1)
    Entry(frame, textvariable=emailinp).grid(row=4, column=1)

    Button(frame, text="Submit", fg="black", command=b1stuff).grid(row=5, column=0, columnspan=2, pady=7, )

    frame.pack(expand=TRUE)


form_loop()
root.mainloop()
