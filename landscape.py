import graphics as gr
from random import *

window = gr.GraphWin("Landscape", 500, 500)
window.setBackground("#191970")


def draw_surface():
    surface = gr.Line(gr.Point(0, 400), gr.Point(500, 400))
    surface.setWidth(200)
    surface.setFill("#AFEEEE")
    surface.setOutline("#AFEEEE")
    surface.draw(window)


def create_circle(x, y, r, internal_color, external_color):
    circle = gr.Circle(gr.Point(x, y), r)
    circle.setFill(internal_color)
    circle.setOutline(external_color)
    circle.draw(window)
    return circle


def draw_moon():
    sun_color = "#FFFF99"
    create_circle(150, 100, 60, sun_color, sun_color)


def draw_cloud(x, y):
    cloud_color = "#4169E1"
    circle_centers = [(x-20, y-20), (x, y-15), (x+30, y-5), (x+45, y-15)]
    for x, y in circle_centers:
        create_circle(x, y, 20, cloud_color, cloud_color)


def draw_tree(i, j, q, k):
    trunk = gr.Line(gr.Point(i, j), gr.Point(i, q))
    trunk.setWidth(10)
    trunk.setOutline("#CD853F")
    trunk.draw(window)
    leaf_color = "#7FFFD4"
    color_line = "#87CEFA"
    leaf_centers = [(i - 30, k), (i + 30, k), (i - 20, k - 50), (i + 20, k - 50),
                    (i, k - 5), (i - 25, k - 30), (i + 25, k - 30)]
    for i, k in leaf_centers:
        create_circle(i, k, 30, leaf_color, color_line)


def draw_snow(m, n):
    for l in range(10):
        dx1 = randint(-15, 15)
        dy1 = randint(-15, 15)
        dx2 = randint(-15, 15)
        dy2 = randint(-15, 15)
        leaf = gr.Polygon(gr.Point(m, n), gr.Point(m + dx1, n + dy1),
                          gr.Point(m + dx2, n + dy2))
        leaf.setOutline('#E0FFFF')
        leaf.setFill('#E0FFFF')
        leaf.draw(window)


def draw_landscape():
    draw_surface()
    draw_moon()
    draw_cloud(300, 100)
    draw_cloud(100, 150)
    draw_cloud(270, 200)
    draw_cloud(400, 190)
    draw_tree(370, 250, 450, 300)
    draw_tree(120, 200, 400, 250)
    for b in range(70):
        draw_snow(randint(10, 490), randint(20, 470))


draw_landscape()

window.getMouse()

window.close()
