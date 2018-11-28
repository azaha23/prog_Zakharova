from tkinter import *
from random import *

root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg="#ffffff")
canv.pack(fill=BOTH, expand=1)


def left_click(event):
    colors = choice(['#FF0000', '#FFA500', '#008000', '#1E90FF', '#DDA0DD', '#FFFF00'])
    canv.create_oval(event.x - r, event.y + r, event.x + r, event.y - r, fill=colors)


def right_click(event):
    canv.delete(ALL)


canv.bind('<Button-1>', left_click)


canv.bind('<Button-3>', right_click)

x = y = 300
r = 130

mainloop()
