from tkinter import *

root = Tk()
root.title("Dropdown menu")
root.geometry("300x200")
un = StringVar()
drop = OptionMenu(root, un, "Apple", "2", "3", "4")
drop.pack()

root.mainloop()