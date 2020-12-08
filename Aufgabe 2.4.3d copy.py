from gturtle import *

def bogen():
    repeat 30: 
        forward(5) 
        right(3) 
        
def blumenblatt():
    repeat 2: 
        bogen()
        right(90)
        
def blume():
    repeat 5: 
        blumenblatt()
        right(72)
        

makeTurtle()
hideTurtle()
setPenColor("red")
setFillColor("red")
startPath()
blume()
fillPath()