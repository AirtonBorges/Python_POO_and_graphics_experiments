import turtle
import math
bob = turtle.Turtle()

roberto = turtle.Turtle()
roberto.hideturtle()
roberto.up()

turtle.screensize(10000, 10000)
roberto.speed(0)
bob.speed(0)


# Calculating Points and lines:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def reset():
    roberto.setpos(0, 0)


class Line:
    #  Store a Line object with some information, most importantly the beginning and a end
    def __init__(self, beg: Point, _end: Point = None, angle=None, size=None, stroke=1, color='black'):
        self.beginning = beg
        self.end = _end
        self.angle = angle
        if angle == 0:
            self.angle = 360

        self.size = size
        self.stroke = stroke
        self.color = color

        # If is provided just an angle and a size, the end will be calculated automatically
        # Not perfect, but it works (sometimes) (mostly).
        try:
            if not self.angle:
                beg = self.beginning
                roberto.setpos(beg.x, beg.y)
                roberto.setheading(roberto.towards(self.end.x, self.end.y))
                self.angle = roberto.heading()
                reset()

            if not self.size:

                calc = math.sqrt(((beg.x - self.end.x) ** 2) + ((beg.y - self.end.y) ** 2))
                self.size = calc

            if not self.end:
                self.go_to_beggining()
                roberto.setheading(self.angle)
                roberto.forward(self.size)
                self.end = Point(roberto.position()[0], roberto.position()[1])
                reset()

        except Exception as ex:
            print("You have to provide a Size and an Angle ")
            print(ex)

    def go_to_beggining(self):
        roberto.setheading(self.angle)
        beg = self.beginning
        roberto.setpos(beg.x, beg.y)

    # Must use these functions to rotate add add some length to a line
    # Changing a line size or angle after declaring it wont do much, because the ending will
    # not change. Need to add getters and setters. (which I don't know yet)
    def rotate(self, angle):
        self.go_to_beggining()
        roberto.setheading(self.angle)
        roberto.right(angle)
        roberto.forward(self.size)
        self.end = Point(roberto.position()[0], roberto.position()[1])
        self.angle = roberto.heading()
        reset()

    def modify_size(self, size):  # size = negative or positive boolean
        self.go_to_beggining()
        if size <= 0:
            size = 0

        roberto.forward(size)

        self.size = 0
        self.end = Point(roberto.position()[0], roberto.position()[0])
        reset()


# Draws a line using turtle based on a start point and a end point
def draw_line(line: Line):
    bob.color(line.color)
    bob.pensize(line.stroke)

    bob.up()
    bob.setpos(line.beginning.x, line.beginning.y)
    bob.setheading(bob.towards(line.end.x, line.end.y))
    bob.down()

    distance = bob.distance(line.end.x, line.end.y)
    bob.forward(distance)


# Class with class variables to store information about the tree
class Tree:
    branches = list()
    size = 0
    max_size = 100  # number of iterations


# This is basically a line that has a function that adds two more lines at the end of itself
class Branch:
    def __init__(self, info: Line):
        self.branch = info

    def add_branch(self):
        # change this function and it's variables to modify the two added branches
        colors = ('brown', 'green')
        color = colors[0]

        b = self

        if len(Tree.branches) >= 30:
            color = colors[1]

        angle = 30

        new_branchr = Line(b.branch.end,
                           size=b.branch.size * 0.67,
                           angle=b.branch.angle,
                           color=color,
                           stroke=(math.floor(self.branch.stroke * 0.90)))

        new_branchr.rotate(angle)
        new_branchr = Branch(new_branchr)

        new_branchl = Line(b.branch.end, size=b.branch.size * 0.67,
                           angle=b.branch.angle,
                           color=color,
                           stroke=(math.floor(self.branch.stroke * 0.90)))

        new_branchl.rotate(-angle)
        new_branchl = Branch(new_branchl)

        Tree.branches.append(new_branchl)
        Tree.branches.append(new_branchr)


def draw_all_branches():
    for b in Tree.branches:
        draw_line(b.branch)


beginning = Point(0, 0)
Tree.branches.append(Branch(Line(beginning, stroke=10, size=200, color='brown', angle=90)))

# Finally draw the tree, adding two new branches to each branch on the tree.
while True:
    branch = None
    # Have to put this here because of a weird bug. Every line facing right
    # at exactly 0 degrees, causes a bug that don't let new branches be generated on them.
    # I'll revisit this and try to fix it.
    # Seems to see something with the way I'm calculating and/or drawing angles.
    # It looks like the bug stopped magically. wtf?
    # Not really, if yo draw the first line at 0 degrees left, the bug still occurs. Such
    # A weird bug.
    # Got it. There's no 0 degrees. It's just 360.

    try:
        branch = Tree.branches[Tree.size]
        branch.add_branch()

    except Exception as e:
        print(e)
        print(f"Tree end{Tree.branches[-1].branch.end}")

    draw_line(branch.branch)
    Tree.size += 1
