import graphics as gr

window = gr.GraphWin("Landscape", 500, 500)
window.setBackground("#ADD8E6")

def draw_surface():
    surface = gr.Line(gr.Point(0, 400), gr.Point(500, 400))
    surface.setWidth(200)
    surface.setFill("#008000")
    surface.setOutline("#008000")
    surface.draw(window)

def draw_sun():
    sun = gr.Circle(gr.Point(150, 100), 60)
    sun.setFill("#FFD700")
    sun.setOutline("#FFD700")
    sun.draw(window)

def draw_cloud(x, y):
    cloud_color = "#FFDAB9"
    circle_centers = [(x-20, y-20), (x, y-15), (x+30, y-5), (x+45, y-15)]
    for x, y in circle_centers:
        circle = gr.Circle(gr.Point(x, y), 20)
        circle.setFill(cloud_color)
        circle.setOutline(cloud_color)
        circle.draw(window)

def draw_tree(i, j ,q, k):
    trunk = gr.Line(gr.Point(i, j), gr.Point(i, q))
    trunk.setWidth(10)
    trunk.setOutline("#A0522D")
    trunk.draw(window)
    leaf_color = "#ADFF2F"
    color_line = "#228B22"
    leaf_centers = [(i - 30, k), (i + 30, k), (i - 20, k - 50), (i + 20, k - 50), (i, k - 5), (i - 25, k - 30), (i + 25, k - 30)]
    for i, k in leaf_centers:
        circle = gr.Circle(gr.Point(i, k), 30)
        circle.setFill(leaf_color)
        circle.setOutline(color_line)
        circle.draw(window)

def draw_bush(x, y):
    bush_color = "#9ACD32"
    color_line = "#228B22"
    bush_centers = [(x - 30, y), (x, y - 30), (x + 30, y), (x, y + 20), (x + 20, y + 20), (x - 20, y + 20), (x + 20, y - 20), (x - 20, y - 20), (x, y)]
    for x, y in bush_centers:
        circle = gr.Circle(gr.Point(x, y), 20)
        circle.setFill(bush_color)
        circle.setOutline(color_line)
        circle.draw(window)



def draw_landscape():
    draw_surface()
    draw_sun()
    draw_cloud(300, 100)
    draw_cloud(100, 150)
    draw_cloud(270, 200)
    draw_cloud(400, 190)
    draw_tree(370, 250, 450, 300)
    draw_tree(120, 200, 400, 250)
    draw_bush(100, 400)

draw_landscape()

window.getMouse()

window.close()
