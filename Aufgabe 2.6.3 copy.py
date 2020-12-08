from gturtle import *

def square(sidelength):
    repeat 4:
        forward(sidelength)
        right(90)
        
sidelength=8

makeTurtle()
repeat 10:
    square(sidelength)
    sidelength=sidelength+10
