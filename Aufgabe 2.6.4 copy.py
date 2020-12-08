from gturtle import *

def square(sidelength):
    repeat 4:
        forward(sidelength)
        right(90)
        
sidelength=inputInt("wie lang ist das grösste Quadrat?")

makeTurtle()

repeat 20:
    square(sidelength)
    left(10)
    sidelength= sidelength * 0.9

