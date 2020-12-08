from gturtle import *
setPlaygroundSize(1000,1000)

def figur():
    repeat 37:
        forward(77)
        right(140.86)
        forward(310)
        right(112)
        
def doIt():
    figur()
        
makeTurtle()
ht()
setPos(0, 0)
doIt()

printerPlot(doIt)