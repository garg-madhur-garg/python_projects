from tkinter import *


def click(event):
    text = event.widget.cget("text")
    print(text)
    


root = Tk()
root.geometry("400x300")
root.title("Calculator2")

scvalue = StringVar()
entry = Entry(root, textvariable=scvalue).pack()

for i in range(1, 10):
    f1 = Frame(root)

    b1 = Button(f1, text=f"{i}", font="lucida 10 bold")
    b1.pack()
    b1.bind("<Button-1>", click)

    f1.pack()


root.mainloop()