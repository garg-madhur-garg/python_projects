from tkinter import *

root = Tk()
root.title("Menu in GUI")

mainmenu = Menu(root)
m1 = Menu(mainmenu)
m1.add_command(label="Save")
m1.add_command(label="Save As")
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu)
m2.add_command(label="Open")
m2.add_command(label="Close")
mainmenu.add_cascade(label="View", menu=m2)

m3 = Menu(mainmenu)
m3.add_command(label="Exit")
mainmenu.add_cascade(label="Exit", menu=m3)

root.config(menu=mainmenu)

root.mainloop()