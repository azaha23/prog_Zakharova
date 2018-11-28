from tkinter import *
from random import *

size = 600

root = Tk()
canv = Canvas(root, width=size, height=size, bg='#ffffff')
canv.pack(fill=BOTH, expand=1)


def tick():
    global x, y, r
    root.after(1000, tick)
    canv.delete(ALL)
    x = randint(1, size)
    y = randint(1, size)
    r = randint(1, size/6)
    colors = choice(['#FF0000', '#FFA500', '#008000', '#1E90FF', '#DDA0DD', '#FFFF00'])
    canv.create_oval(x - r, y + r, x + r, y - r, fill=colors)


score = 0


def left_click(event):
    global x, y, r, score
    if event.x < x + r and event.x > x - r and event.y < y + r and event.y > y - r:
        score = score + 1

        canv.create_text(400, 300, text=score, font='Arial 25')
    else:
        None
        canv.create_text(400, 300, text=score, font='Arial 25')


canv.bind('<Button-1>', left_click)


root.after_idle(tick)
root.mainloop()
