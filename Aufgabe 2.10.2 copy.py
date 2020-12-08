"""Du kannst die Turtle dazu verwenden, ein Programm zum Freihandzeichen zu erstellen. 
Dabei wird der Zeichenstift mit mit dem Press-Event gesetzt mit dem Drag-Event bewegt."""


from gturtle import *

def onMouseDragged(x,y):
    moveTo(x,y)
    
    
def onMousePressed(x,y):
    setPos(x,y)
    

    
makeTurtle(mouseDragged = onMouseDragged, mousePressed = onMousePressed)

ht()
speed(-1)
    