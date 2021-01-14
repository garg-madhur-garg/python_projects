from tkinter import *

root = Tk()

canvas_width = 500
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Canvas widget")

canvas = Canvas(root, width=canvas_width, height=canvas_height)
# line  x1, y1 to x2, y2
canvas.create_line(0, 0 , 500, 400, fill="green")
canvas.create_arc(0, 0, 500, 400, fill="red")
canvas.create_bitmap(400, 300, bitmap="warning", foreground="black")

canvas.pack()

root.mainloop()