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
    
def onKeyPressed(key):
    global x,y
    if key == spacebar:
        fill(x,y)
        fill(-x,-y)
        fill(x,-y)
        fill(-x,y)
    
spacebar = 32

makeTurtle(mousePressed = onMousePressed, mouseDragged = onMouseDragged, keyPressed = onKeyPressed)
speed(-1)
hideTurtle()