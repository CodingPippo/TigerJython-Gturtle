from gturtle import *


x=0
y=0
    
def onMousePressed(x1,y1):
    global x,y
    setPos(x1,y1)
    x=x1
    y=y1
    
    

def onMouseDragged(x1,y1):
    global x,y
    setPos(x,y)
    moveTo(x1,y1)
    setPos(-x,-y)
    moveTo(-x1,-y1)
    setPos(-x,y)
    moveTo(-x1,y1)
    setPos(x,-y)
    moveTo(x1,-y1)
    x=x1
    y=y1
    
    



makeTurtle(mousePressed = onMousePressed, mouseDragged = onMouseDragged)
speed(-1)
hideTurtle()