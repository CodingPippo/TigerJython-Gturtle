from gturtle import *

def triangle(color):
    setPenColor(color)
    repeat 3:
        forward(100)
        left(120)
    left(90)
makeTurtle()
triangle("red")

triangle("green")

triangle("blue")

triangle("violet")