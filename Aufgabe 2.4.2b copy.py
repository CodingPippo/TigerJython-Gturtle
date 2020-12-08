from gturtle import *

def square():
    repeat 4: 
        forward(50)
        left(90)
        

makeTurtle()
hideTurtle()
right(135)
startPath()
setFillColor("blue")
square()
fillPath()
penUp()
setPenColor("red")
setFillColor("red")
left(45)
forward(70)
right(45)
startPath()
penDown()
square()
fillPath()

setPenColor("green")
setFillColor("green")
penUp()
left(45)
forward(70)
penDown()
startPath()
right(45)
square()
fillPath()

setPenColor("black")
setFillColor("black")
penUp()
left(45)
forward(70)
penDown()
startPath()
right(45)
square()
fillPath()

