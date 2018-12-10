from tkinter import *
from random import *

size = 600

root = Tk()
canv = Canvas(root, width=size, height=size, bg='#ffffff')
canv.pack(fill=BOTH, expand=1)

score = 0
score_string = canv.create_text(400, 300, text='Счёт: {}'.format(score), font='Arial 20')
count_click = 0


def draw_ball():
    global x, y, r, score_string, count_click
    count_click = 0
    root.after(1000, draw_ball)
    canv.delete(ALL)
    x = randint(1, size)
    y = randint(1, size)
    r = randint(1, size/6)
    colors = choice(['#FF0000', '#FFA500', '#008000', '#1E90FF', '#DDA0DD', '#FFFF00'])
    canv.create_oval(x - r, y + r, x + r, y - r, fill=colors)
    score_string = canv.create_text(300, 60, text='Счёт: {}'.format(score), font='Arial 25')


def left_click(event):
    global x, y, r, score, score_string, count_click
    if ((event.x - x) ** 2 + (event.y - y) ** 2) ** 0.5 <= r and count_click == 0:
        score = score + 1
    count_click += 1


canv.bind('<Button-1>', left_click)


root.after_idle(draw_ball)
root.mainloop()
