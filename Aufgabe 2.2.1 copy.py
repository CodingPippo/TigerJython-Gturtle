from gturtle import *

makeTurtle()
setLineWidth(5)
repeat 6:
    print getRandomX11Color() 
    setPenColor(getRandomX11Color())
    forward(100)
    left(60)
