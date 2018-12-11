import robot
r = robot.rmap()
r.lm('task2')


def task():
    for x in range(5):
        r.up()
        r.paint()
        r.up()
        r.right()
        r.paint()
        r.down()
        r.down()
        r.down()
        r.paint()
        r.right()
        r.up()
        r.paint()
        r.right()
        r.down()


r.start(task)
