import robot
r = robot.rmap()
r.lm('task5')


def task():
    for i in range(3):
        for x in range(8):
            r.paint()
            r.right(2)
        r.down()
        r.left()
        for x in range(3):
            r.paint()
            r.left(4)
        r.paint()
        r.down(2)
        r.left()


r.start(task)
