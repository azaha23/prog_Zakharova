from tkinter import *
from random import *


root = Tk()
fr = Frame(root)
root.geometry('800x600')
canvas = Canvas(root, bg='#ffffff')
canvas.pack(fill=BOTH, expand=1)

balls = []


class Ball:
    def __init__(self, x, y, Vx, Vy, r):
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.r = r
        colors = choice(['#FF0000', '#FFA500', '#008000', '#1E90FF', '#DDA0DD', '#FFFF00'])
        self.oval = canvas.create_oval(x - r, y - r, x + r, y + r, fill=colors)

    def go(self):
        if (self.x + self.r > 800) or (self.x - self.r < 0):
            self.Vx *= -1
        elif (self.y + self.r > 600) or (self.y - self.r < 0):
            self.Vy *= -1
        canvas.move(self.oval, self.Vx, self.Vy)
        self.x += self.Vx
        self.y += self.Vy


for i in range(10):
    r = randint(5, 100)
    x = randint(100, 500)
    y = randint(100, 500)
    Vx = randint(-5, 5)
    Vy = randint(-5, 5)
    ball = Ball(x, y, Vx, Vy, r)
    balls.append(ball)


def tick():
    for j in range(10):
        balls[j].go()
    root.after(10, tick)


tick()

root.mainloop()
