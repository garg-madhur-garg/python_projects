from tkinter import *

root = Tk()
root.geometry("500x400")
root.title("Scrollbar tutorial")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
label = Text(root, yscrollcommand=scrollbar.set)

scrollbar.config(command=label.yview)

label.pack(fill=BOTH)


root.mainloop()