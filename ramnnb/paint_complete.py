from tkinter import *
from tkinter.colorchooser import askcolor


def use_pen():
    pass


def use_brush():
    pass


def use_color():
    pass


def use_eraser():
    pass


if __name__ == '__main__':

    root = Tk()
    root.title("Paint")
    root.configure(background="grey")

    pen_button = Button(root, text="Pen", command=use_pen)
    pen_button.grid(row=0, column=0)

    brush_button = Button(root, text="Brush", command=use_brush)
    brush_button.grid(row=0, column=1)

    color_button = Button(root, text="Color", command=use_color)
    color_button.grid(row=0, column=2)

    eraser_button = Button(root, text="Eraser", command=use_eraser)
    eraser_button.grid(row=0, column=3)

    slider = Scale(root, from_=1, to=10, orient=HORIZONTAL, bg="grey")
    slider.grid(row=0, column=4)

    canvas = Canvas(root, width=600, height=500, bg="white")
    canvas.grid(row=1, columnspan=5)

    root.mainloop()