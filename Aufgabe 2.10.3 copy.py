from gturtle import *

def onMouseDragged(x,y):
    moveTo(x,y)
    
def onMousePressed(x,y):
    setPos(x,y)
    
def onMouseClicked(x,y):
    fill(x,y)
    
makeTurtle(mouseDragged = onMouseDragged, mousePressed = onMousePressed, mouseClicked = onMouseClicked)

if isRightMouseButton():
    onMouseClicked(x,y)

ht()
speed(-1)


