import pygame
import math

pygame.init()

win_size = (560, 560)
win = pygame.display.set_mode(win_size)


# A class that represents a point
class Point:
    # default attributes for points.
    default_color = (255, 255, 255)
    default_width = 1

    def __init__(self, location: pygame.Vector2, color: tuple = default_color, width=default_width):
        self.color = color
        self.location = location
        self.width = math.floor(width / math.pi)

    def draw(self):
        # In this case, the points are circles, but they can be any geometric shape in thesis
        pygame.draw.circle(win, self.color, (int(self.location.x), int(self.location.y)), self.width)


class Set:
    def __init__(self):
        self.list = []
        for x in range(-Point.default_width, win_size[0] + Point.default_width * 2, Point.default_width):
            self.list.append(list())
            for y in range(-Point.default_width, win_size[1] + Point.default_width * 2, Point.default_width):
                self.list[-1].append(Point(pygame.Vector2(x, y)))

    def draw(self):
        for x in range(0, len(self.list) - 1):
            for y in range(0, len(self.list[x]) - 1):
                self.list[x][y].draw()


# I'll refactor this later, but this will do for now
class Mandelbrot:
    set = Set()
    # the range of the complex plane to be calculated
    max_r_x = -2
    max_r_y = 2


for x in Mandelbrot.set.list:
    for y in x:
        y.color = 0, 0, 0

Mandelbrot.set.draw()


# Math stuff
def rule_of_three(valor_base, max_base, q):
    return float(valor_base * q / max_base)


def tales_theorem(val, max_a, min_a, max_b, min_b):
    # A worse version of the map function in Processing
    a = ((val - max_a) * (min_b - max_b) / (min_a - max_a)) + max_b
    return a


# All the calculations will be done here for now, but I'll implement a function on the
# Set class that permits me move in the complex plane, or maybe implement a class that deals
# with all complex plane stuff.
def mand_set():
    max_itt = 17

    # based on coding train's video.
    for c in range(0, len(Mandelbrot.set.list) - 1):
        for r in range(0, len(Mandelbrot.set.list[c]) - 1):

            # print(Mandelbrot.max_r_x, Mandelbrot.max_r_y)

            a = tales_theorem(c, 0, len(Mandelbrot.set.list), Mandelbrot.max_r_x, Mandelbrot.max_r_y)
            b = tales_theorem(r, 0, len(Mandelbrot.set.list[c]), Mandelbrot.max_r_x, Mandelbrot.max_r_y)

            orig_a = a
            orig_b = b

            n = 0
            for i in range(0, max_itt):
                aa = a * a - b * b
                bb = 2 * a * b

                a = aa + orig_a
                b = bb + orig_b

                if math.fabs(a + b) >= 16:
                    n = i
                    break

            bright = math.floor(tales_theorem(n, 0, max_itt, 0, 100))

            Mandelbrot.set.list[c][r].color = bright, bright, bright

    print('Done')

    Mandelbrot.set.draw()


mand_set()


# Normal pygame stuff
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
