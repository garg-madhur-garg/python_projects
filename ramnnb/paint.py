from tkinter import *
from tkinter.colorchooser import askcolor

class Paint(object):
    default_pen_size = 5.0
    default_color = "black"

    def __init__(self):
        self.root = Tk()

        self.pen_button = Button(self.root, text="pen")
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.root, text="brush")
        self.brush_button.grid(row=0, column=1)

        self.color_button = Button(self.root, text="color")
        self.color_button.grid(row=0, column=2)

        self.eraser_button = Button(self.root, text="eraser")
        self.eraser_button.grid(row=0, column=3)

        self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=4)

        self.c = Canvas(self.root, bg="white", width=600, height=600)
        self.c.grid(row=1, columnspan=5)

        # self.setup()
        self.root.mainloop()

if __name__ == '__main__':
    Paint()