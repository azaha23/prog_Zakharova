import robot
r = robot.rmap()
r.lm('task4')


def task():
    while r.freeRight():
        r.right()
    while r.freeUp():
        r.up()
    for i in range(3):
        for k in range(5):
            r.down()
            r.left()
            r.paint()
        for k in range(3):
            r.right()
            r.up()
        r.right(2)


r.start(task)
