import turtle

turtle.speed('slowest')
turtle.speed('fastest')


def draw(length, n):
    if n != 1:
        turtle.left(45)
        draw(length, n - 1)
        turtle.right(90)
        draw(length, n - 1)
        turtle.left(45)
    else:
        turtle.forward(length)


draw(20, 10)
