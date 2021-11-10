from tkinter import *


def click(event):
    global entryinp
    text = event.widget.cget("text")
    print(text)

    if text == "=":
        value = eval(entryinp.get())
        entryinp.set(value)
    elif text == "C":
        entryinp.set("")
    else:
        entryinp.set(entryinp.get() + text)

root = Tk()
root.configure(background="powderblue")
root.geometry("500x500")
root.title("Calculator")

entryinp = StringVar()
entry = Entry(root, textvariable=entryinp, font="lucida 16 bold", bg="pink").pack(fill=X, pady=5, ipady=5)

f1 = Frame(root, bg="grey")

b1 = Button(f1, text="1", font="lucida 10 bold", width=6, height=3)
b1.pack(padx=8, side=LEFT, pady=5)
b1.bind("<Button-1>", click)

b2 = Button(f1, text="2", font="lucida 10 bold", width=6, height=3)
b2.pack(padx=8, side=LEFT, pady=5)
b2.bind("<Button-1>", click)

b3 = Button(f1, text="3", font="lucida 10 bold", width=6, height=3)
b3.pack(padx=8, side=LEFT, pady=5)
b3.bind("<Button-1>", click)

f1.pack()

f2 = Frame(root, bg="grey")

b4 = Button(f2, text="4", font="lucida 10 bold", width=6, height=3)
b4.pack(padx=8, side=LEFT, pady=5)
b4.bind("<Button-1>", click)

b5 = Button(f2, text="5", font="lucida 10 bold", width=6, height=3)
b5.pack(padx=8, side=LEFT, pady=5)
b5.bind("<Button-1>", click)

b6 = Button(f2, text="6", font="lucida 10 bold", width=6, height=3)
b6.pack(padx=8, side=LEFT, pady=5)
b6.bind("<Button-1>", click)

f2.pack()

f3 = Frame(root, bg="grey")

b7 = Button(f3, text="7", font="lucida 10 bold", width=6, height=3)
b7.pack(padx=8, side=LEFT, pady=5)
b7.bind("<Button-1>", click)

b8 = Button(f3, text="8", font="lucida 10 bold", width=6, height=3)
b8.pack(padx=8, side=LEFT, pady=5)
b8.bind("<Button-1>", click)

b9 = Button(f3, text="9", font="lucida 10 bold", width=6, height=3)
b9.pack(padx=8, side=LEFT, pady=5)
b9.bind("<Button-1>", click)

f3.pack()

f4 = Frame(root, bg="grey")

bplus = Button(f4, text="+", font="lucida 10 bold", width=6, height=3)
bplus.pack(padx=8, side=LEFT, pady=5)
bplus.bind("<Button-1>", click)

b0 = Button(f4, text="0", font="lucida 10 bold", width=6, height=3)
b0.pack(padx=8, side=LEFT, pady=5)
b0.bind("<Button-1>", click)

bequal = Button(f4, text="=", font="lucida 10 bold", width=6, height=3)
bequal.pack(padx=8, side=LEFT, pady=5)
bequal.bind("<Button-1>", click)

f4.pack()

f5 = Frame(root, bg="grey")

bclear = Button(f5, text="C", font="lucida 10 bold", width=6, height=3)
bclear.pack(padx=8, side=LEFT, pady=5)
bclear.bind("<Button-1>", click)

bsub = Button(f5, text="-", font="lucida 10 bold", width=6, height=3)
bsub.pack(padx=8, side=LEFT, pady=5)
bsub.bind("<Button-1>", click)

bmulti = Button(f5, text="*", font="lucida 10 bold", width=6, height=3)
bmulti.pack(padx=8, side=LEFT, pady=5)
bmulti.bind("<Button-1>", click)

f5.pack()

f6 = Frame(root, bg="grey")

bdiv = Button(f6, text="/", font="lucida 10 bold", width=6, height=3)
bdiv.pack(padx=8, side=LEFT, pady=5)
bdiv.bind("<Button-1>", click)

f6.pack()
root.mainloop()