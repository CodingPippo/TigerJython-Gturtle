from gturtle import *

def vieleck(sidelength):    
    repeat ecken: 
        forward(sidelength) 
        right(360/ecken)
      
makeTurtle()
ecken= inputInt("Gib die Anzahl Ecken ein")
sidelength=(100)
vieleck(sidelength)