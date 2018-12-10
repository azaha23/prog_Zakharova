import turtle

turtle.speed('slowest')
turtle.speed('fastest')


def draw(length, n, f):
    x = length

    if n != 1:
        if f == 1:
            turtle.right(45)
            draw(x, n - 1, 1)
            turtle.left(90)
            draw(x, n - 1, 0)
            turtle.right(45)
        if f == 0:
            turtle.left(45)
            draw(x, n - 1, 1)
            turtle.right(90)
            draw(x, n - 1, 0)
            turtle.left(45)
    else:
        turtle.forward(x)


draw(50, 6, 1)
