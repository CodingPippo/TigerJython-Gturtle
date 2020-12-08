"""Ein bekannter Graf ist der vollständige binäre Baum. 
Er sieht für eine bestimmte Rekursionstiefe wie nebenstehend gezeigt aus. 
Schreibe eine rekursive Funktion tree(s), die den Baum mit der "Stammlänge" s zeichnet."""

from gturtle import *



def baum(s):
    if s<5:
        return
    forward(s)
    left(45)
    baum(s/2)
    right(90)
    baum(s/2)
    left(45)
    back(s)
    
    
    
makeTurtle()
ht()
setPos(0,-200)
baum(200)