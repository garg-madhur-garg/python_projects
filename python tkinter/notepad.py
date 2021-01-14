from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def new_file():
    global file
    root.title("Untitled - notepad")
    file = None
    textfield.delete(1.0, END)


def open_file():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textfield.delete(1.0, END)
        with open(file)as f:
            textfield.insert(1.0, f.read())


def save_file():
    global file

    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", filetypes=[("All Files", "*.*"), ("Documents", "*.txt")])
        if file == "":
            file = None
        else:
            with open(file, "w")as f:
                f.write(textfield.get(1.0, END))
            root.title(os.path.basename(file) + " - Notepad")
    else:
        with open(file, "w")as f:
            f.write(textfield.get(1.0, END))


def exit_file():
    root.destroy()


def cut():
    textfield.event_generate("<<Cut>>")


def copy():
    textfield.event_generate("<<Copy>>")


def paste():
    textfield.event_generate("<<Paste>>")


def help():
    showinfo("Help", "This Notepad is created by Madhur Garg")


if __name__ == '__main__':

    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("644x567")

    # Adding scrollbar
    scroll = Scrollbar(root)
    scroll.pack(side=RIGHT, fill=Y)

    # Creating Textfield
    textfield = Text(root, font="lucida, 13", yscrollcommand=scroll.set)
    textfield.pack(expand=TRUE, fill=BOTH)
    file = None
    # Creating menubar
    menubar = Menu(root)

    # Filemenu starts
    filemenu = Menu(menubar, tearoff=FALSE)
    filemenu.add_command(label="New", command=new_file)
    filemenu.add_command(label="Open", command=open_file)
    filemenu.add_command(label="Save", command=save_file)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=exit_file)
    menubar.add_cascade(label="File", menu=filemenu)
    # Filemenu ends

    # Editmenu starts
    editmenu = Menu(menubar, tearoff=FALSE)
    editmenu.add_command(label="Cut", command=cut)
    editmenu.add_command(label="Copy", command=copy)
    editmenu.add_command(label="Paste", command=paste)
    menubar.add_cascade(label="Edit", menu=editmenu)
    # Editmenu ends

    # Helpmenu starts
    helpmenu = Menu(menubar, tearoff=FALSE)
    helpmenu.add_command(label="About", command=help)
    menubar.add_cascade(label="Help", menu=helpmenu)
    # Helpmenu ends

    root.config(menu=menubar)
    scroll.config(command=textfield.yview)

    root.mainloop()