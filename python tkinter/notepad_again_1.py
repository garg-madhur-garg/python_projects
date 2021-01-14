from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import asksaveasfilename, askopenfilename
import os

root = Tk()
root.title("Untitled - Notepad")
root.geometry("688x630")
file = None


def newfile():
    global file
    textfield.delete(1.0, END)
    root.title("Untitled - Notepad")
    file = None


def openfile():
    global file
    file = askopenfilename(default=".txt", filetype=[("All File", "*.*"), ("Document", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textfield.delete(1.0, END)
        with open(file)as f:
            textfield.insert(1.0, f.read())


def savefile():
    global file

    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", filetype=[("All File", "*.*"), ("Document", "*.txt")])
        if file == "":
            file = None
        else:
            with open(file, "w")as f:
                f.write(textfield.get(1.0, END))
            root.title(os.path.basename(file) + " - Notepad")
    else:
        with open(file, "w")as f:
            f.write(textfield.get(1.0, END))


def exitfile():
    root.destroy()


def cut():
    menubar.event_generate("<<Cut>>")


def copy():
    menubar.event_generate("<<Copy>>")


def paste():
    menubar.event_generate("<<Paste>>")


def about():
    showinfo("Help", "This notepad is created by Madhur Garg")

# Creating Menubar


menubar = Menu(root)
root.configure(menu=menubar)

# Creating Scrollbar
scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

# Creating filemenu
filemenu = Menu(menubar, tearoff=FALSE)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=newfile)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exitfile)

# Creating editmenu
editmenu = Menu(menubar, tearoff=FALSE)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)

# Creating helpmenu
helpmenu = Menu(menubar, tearoff=FALSE)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)

# Creating textfield
textfield = Text(root, yscrollcommand=scroll.set, font="lucida 13")
textfield.pack(expand=TRUE, fill=BOTH)

scroll.config(command=textfield.yview)


root.mainloop()