from gturtle import *

def figur(sidelength):    
    repeat 30: 
        forward(sidelength) 
        left(winkel)
      
makeTurtle()
hideTurtle()
winkel= inputInt("Enter the side angle")
sidelength=100
figur(sidelength)