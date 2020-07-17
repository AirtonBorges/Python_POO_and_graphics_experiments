import pygame
from random import randint
pygame.init()

# Create canvas and set title
win = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("squares")


# square Class
class Square:
    listofsquares = list()  # a list to store squares
    numb = 0  # simple counter
    lenc = 0  # to store the initial amount of squares on the list.

    def __init__(self, color, x, y, width, height):  # squares
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height


# Adds to a list and goes return every single square provided once at a time
def cicle(squares):
    if Square.numb > Square.lenc - 1:  # resets counter
        Square.numb = 0

    if Square.numb == 0:  # resets list of squares
        Square.listofsquares.clear()
        print('- Cicle complete')

        for c in squares:
            Square.listofsquares.append(c)
        Square.lenc = len(Square.listofsquares)

    value = Square.listofsquares[Square.numb]
    Square.numb += 1

    return value


def getlosasquares(number):  # get randomly generated squares
    lotsasquares = list()

    for i in range(0, number):
        random_square = Square(
            color=(randint(0, 255), randint(0, 255), randint(0, 255)),
            x=randint(- 20, win.get_width()), y=randint(- 20, win.get_height()),
            height=randint(1, 5), width=randint(1, 500))

        lotsasquares.append(random_square)

    return lotsasquares


# Drawing stuff
run = True
while run:
    pygame.time.delay(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    square = cicle(getlosasquares(1))

    pygame.draw.rect(win, square.color, (square.x, square.y, square.height, square.width))
    pygame.display.update()

pygame.quit()
