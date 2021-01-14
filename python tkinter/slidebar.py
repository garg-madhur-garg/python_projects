from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("300x200")
root.title("Slidebar Tutorial")


def getrate():
    with open("feedback.txt", "a")as f:
        f.write(f"{nameinp.get()}: {slider.get()} points\n")
    tmsg.showinfo("Feedback form", f"Thanks for giving us {slider.get()} points.")


lable_top = Label(root, text="Feedback Form", fg="black", font="comicsansms 14 bold").pack()
lable_middle = Label(root, text="Please rate us with points", font="lucida 8 bold").pack()

slider = Scale(root, from_=0, to=10, orient=HORIZONTAL)
slider.set(5)
slider.pack()

nameinp = StringVar()
nameinp.set("Enter your name")

entry = Entry(root, textvariable=nameinp).pack(pady=7)
button = Button(root, text="Submit", command=getrate)
button.pack(pady=5)

root.mainloop()