from gturtle import *

from gturtle import * 

def pentagon(sidelength, color): 
   setPenColor(color) 
   repeat 5: 
      forward(sidelength) 
      left(72)

makeTurtle() 
pentagon(100, "red") 
left(120) 
pentagon(80, "green") 
left(120) 
pentagon(60, "violet")