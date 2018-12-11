import math
from tkinter import *
from random import *

root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg="#ffffff")
canv.pack(fill=BOTH, expand=1)

g = 9.8  # Ускорение свободного падения для снаряда.

score = 0
score_string = canv.create_text(400, 50, text='Счёт:{} '.format(score), font='Arial 20')
shells = []
balls = []
n = randint(1, 10)
for m in range(n):
    balls.append(0)
timer = 0


class Cannon:
    max_velocity = 100

    def __init__(self, x, y, canvas):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.shell_num = None
        self.direction = math.pi/4
        self.power = 0

        self.line_length = 100
        self.line = canv.create_line(x + 70, y - 50, 160, 480, width=30, fill="black")
        self.oval = canv.create_oval(x, y, 140, 500, outline="black", fill="black")

    def aim(self, x, y):
        """
        Меняет направление direction так, чтобы он из точки
        (self.x, self.y) указывал в точку (x, y).
        :param x: координата x, в которую целимся
        :param y: координата y, в которую целимся
        :return: None
        """

        self.direction = math.atan((self.y - y)/(self.x - x))
        self.draw()

    def fire(self):
        """
        Создаёт объект снаряда (если ещё не потрачены все снаряды)
        летящий в направлении угла direction
        со скоростью, зависящей от длительности клика мышки
        :return: экземпляр снаряда типа Shell
        """

        click_time = self.finish_time - self.start_time
        self.power = click_time
        shell = Shell(self.x + 70 + self.line_length*math.cos(self.direction),
                      self.y - 50 + self.line_length*math.sin(self.direction),
                      self.power/2, self.power/2, self.canvas, self.direction)

        shells.append(shell)

    def draw(self):
        self.canvas.delete(self.line)

        self.line = self.canvas.create_line(self.x + 70, self.y - 50,
                                            self.x + 70 + self.line_length*math.cos(self.direction),
                                            self.y - 50 + self.line_length*math.sin(self.direction),
                                            width=30, fill="black")


class Shell:
    global standard_radius
    standard_radius = 15

    def __init__(self, x, y, Vx, Vy, canvas, direction):
        self.x, self.y = x, y
        self.Vx, self.Vy = Vx, Vy
        self.r = standard_radius
        self.canvas = canvas
        self.direction = direction
        self.dx = 0
        self.dy = 0

        self.oval = self.canvas.create_oval(x - self.r, y - self.r, x + self.r,
                                            y + self.r, fill="red", outline="red")

    def go(self, dt):
        """
        Сдвигает снаряд исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        :param dt:
        :return:
        """

        ax, ay = 0, g
        self.dx = self.Vx * dt * math.cos(self.direction) + ax*(dt ** 2) / 2
        self.dy = self.Vy * dt * math.sin(self.direction) + ay*(dt ** 2) / 2
        self.Vx += ax * dt
        self.Vy += - ay * dt
        self.x += self.dx
        self.y += self.dy

        self.draw()

        if self.x > 800 or self.x < 0:
            self.Vx = - self.Vx
        if self.y > 600 or self.y < 0:
            self.canvas.delete(self.oval)

    def draw(self):
        self.canvas.move(self.oval, self.dx, self.dy)

    def detect_collision(self, ball):
        """
        Проверяет факт соприкосновения снаряда и мишени
        :param ball: объект, который должен иметь поля x, y, r
        :return: логическое значение типа bool
        """

        length = ((self.x - ball.x) ** 2 + (self.y - ball.y) ** 2) ** 0.5
        return length <= self.r + ball.r


class Target:

    def __init__(self, x, y, Vx, Vy, r):
        self.x, self.y = x, y
        self.Vx, self.Vy = Vx, Vy
        self.r = r
        colors = choice(['#FF0000', '#FFA500', '#008000', '#1E90FF', '#DDA0DD', '#FFFF00'])
        self.oval = canv.create_oval(x - self.r, y - self.r, x + self.r,
                                     y + self.r, fill=colors)

    def go(self):
        """
        Сдвигает шарик-мишень исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        :param
        :return:
        """
        if (self.x + self.r > 800) or (self.x - self.r < 0):
            self.Vx *= -1
        elif (self.y + self.r > 600) or (self.y - self.r < 0):
            self.Vy *= -1
        canv.move(self.oval, self.Vx, self.Vy)
        self.x += self.Vx
        self.y += self.Vy

    def collide(self, other):
        """
        Расчёт абсолютно упругого соударения
        :param other:
        :return:
        """
        pass


cannon = Cannon(70, 550, canv)


def mouse_move_handler(event):
    cannon.aim(event.x, event.y)


def game_step():
    global score, timer, score_string, shells
    timer += 1

    for i in range(n):
        if balls[i] == 0:
            balls[i] = Target(randint(200, 600), randint(100, 400), randint(-2, 2),
                              randint(-2, 2), randint(15, 100))

    for b in range(n):
        balls[b].go()

    for k in range(len(shells)):
        if shells[k] != 0:
            shells[k].go(0.1)
            for i in range(len(balls)):
                if shells[k].detect_collision(balls[i]):
                    canv.delete(balls[i].oval)
                    canv.delete(shells[k].oval)
                    balls[i] = 0
                    shells[k] = 0
                    score += 1
                    canv.delete(score_string)
                    score_string = canv.create_text(400, 50, text='Счёт: {} '.format(score), font='Arial 20')

    root.after(10, game_step)


def time_start(event):
    global timer
    cannon.start_time = timer


def time_finish(event):
    global timer
    cannon.finish_time = timer
    cannon.fire()
    timer = 0


canv.bind('<Motion>', mouse_move_handler)
canv.bind("<ButtonPress-1>", time_start)
canv.bind("<ButtonRelease-1>", time_finish)


game_step()

mainloop()
