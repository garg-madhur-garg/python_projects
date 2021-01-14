from tkinter import *

root = Tk()


def madhur(event):
    print(f"You clicked at{event.x}, {event.y}")


root.geometry("500x400")
root.title("Event Handling")

b1 = Button(root, text="Click me")
b1.pack()

b1.bind('<Button-1>', madhur)
b1.bind('<Double-1>', quit)
root.mainloop()