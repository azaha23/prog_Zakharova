import robot
r = robot.rmap()
r.lm('task6')


def task():
    width = int(input("Введите ширину: "))
    height = int(input("Введите высоту: "))
    if (width >= 24) or (height >= 24):
        print("Введите высоту меньше 24 и ширину меньше 24")
        width = int(input("Введите ширину: "))
        height = int(input("Введите высоту: "))
    r.right(int((24 - width) / 2))
    for i in range(width - 1):
        r.paint()
        r.right()
    r.paint()
    r.left(int(width / 2))
    for k in range(height - 1):
        r.down()
        r.paint()


r.start(task)
