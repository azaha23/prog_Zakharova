import turtle

turtle.speed('slowest')
turtle.speed('fastest')


def draw(length, n, x, y):
    turtle.forward(length)
    if n != 0:

        turtle.penup()
        turtle.goto(x, y - 10)
        turtle.pendown()
        draw(length / 3, n - 1, x, y - 10)

        if n != 1:
            turtle.penup()
            turtle.goto(x + 2*length/3, y - 10)
            turtle.pendown()

            draw(length / 3, n - 1, x + 2*length/3, y - 10)
    else:
        turtle.penup()
        turtle.forward(length)
        turtle.pendown()
        turtle.forward(length)


draw(243, 4, 0, 0)
