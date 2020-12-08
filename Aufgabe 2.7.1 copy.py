from gturtle import *



def square(sidelength):
    
    repeat 4:
        forward(sidelength)
        left(90)
 
makeTurtle()



sidelength = inputInt("wie lang?")
if sidelength <50:
        setPenColor("red")
        square(sidelength)
else:
        setPenColor("green")
        square(sidelength)
   