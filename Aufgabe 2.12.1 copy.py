from gturtle import *

def Fan():
    repeat 2:
        startPath()
        forward(57)
        right(60)
        forward(57)
        right(120)
        forward(57)
        right(60)
        forward(57)
        left(60)
        fillPath()

def circle():
    setHeading(0)
    repeat 360:
        fd(2)
        rt(1)
    
        
makeTurtle()
ht()
enableRepaint(False)



while True:    
    clear()
    setPos(-100,0)
    #circle()
    setPos(0,0)
    Fan()
    repaint()
    delay(100)
    right(20)
    
    

  
