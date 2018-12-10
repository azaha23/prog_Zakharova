import turtle

turtle.speed('slowest')
turtle.speed('fastest')


def draw(length, n):
    x = length / 2
    if n != 1:
        draw(x, n - 1)
        turtle.left(60)
        draw(x, n - 1)
        turtle.right(120)
        draw(x, n - 1)
        turtle.left(60)
        draw(x, n - 1)
    else:
        turtle.forward(x)


draw(100, 4)
