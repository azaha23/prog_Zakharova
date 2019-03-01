import pygame
import random


class Ball(object):

    def __init__(self, x, y, vx, vy, r, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = r
        self.color = color

    def go(self):
        if (self.x + self.r > 800) or (self.x - self.r < 0):
            self.vx *= -1
        elif (self.y + self.r > 600) or (self.y - self.r < 0):
            self.vy *= -1

        self.x += self.vx
        self.y += self.vy


def create_ball():
    r = random.randrange(10, 70)
    x = random.randrange(r, 600 - r)
    y = random.randrange(r, 320 - r)
    vx = random.randrange(-5, 5)
    vy = random.randrange(-5, 5)
    color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    ball = Ball(x, y, vx, vy, r, color)

    return ball


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    background = pygame.Surface(screen.get_size())
    background_color = (255, 255, 204)
    background.fill(background_color)
    screen.blit(background, (0, 0))
    clock = pygame.time.Clock()
    amount_balls = 10
    mainloop = True
    balls = []

    for i in range(amount_balls):
        ball = create_ball()
        balls.append(ball)

    while mainloop:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainloop = False

        for ball in balls:
            pygame.draw.circle(screen, background_color, [ball.x, ball.y], ball.r)
            ball.go()
            pygame.draw.circle(screen, ball.color, [ball.x, ball.y], ball.r)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
