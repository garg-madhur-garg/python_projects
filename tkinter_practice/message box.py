from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("70x100")

# Functions
def error():
    tmsg.showerror("Error", "This is error box")


def info():
    tmsg.showinfo("Information", "This is info box")

def warning():
    tmsg.showwarning("Warning", "This is warning box")


b1 = Button(root, text="Error", command=error)
b1.grid(row=0, column=0)

b2 = Button(root, text="Info", command=info)
b2.grid(row=0, column=1)

b3 = Button(root, text="Warning", command=warning)
b3.grid(row=0, column=2)

root.mainloop()