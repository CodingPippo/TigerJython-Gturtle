"""Die Turtle befindet sich an der Position (250, 200). 
Mit Schritten der Länge 10 bewegt sie sich auf einer Geraden zur Homeposition bis der Abstand kleiner als 1 ist.


Verwende die Befehle towards() und heading(degrees)"""

from gturtle import*

def zuruck():
    towards(0,0)
    heading(towards(0,0))
    while getX()>=1:
        fd(10)
    
    





makeTurtle()
setPos(250,200)
zuruck()