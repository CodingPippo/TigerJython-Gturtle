from gturtle import *

def Flag(angle):
    setPenColor("black")
    dot(20)
    right(angle)
    heading_ = heading()
    fd(100)
    setPenColor("red")
    setFillColor("red")
    startPath()
    fd(50)
    right(90)
    fd(60)
    right(90)
    fd(50)
    fillPath()
    right(90)
    fd(60)
    home()
    
    
def move(start, end, step):
    for a in range(start, end, step):
        clear("lightSkyBlue")  
        Flag(a)
        repaint()
        delay(50)
   
makeTurtle()
ht()

setLineWidth(5)
enableRepaint(False)

while True:
    move(45, 90, 2)
    move(90, 45, -2)

    
