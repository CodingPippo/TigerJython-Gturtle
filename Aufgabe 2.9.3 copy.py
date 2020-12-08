"""Zeichne die nebenstehende Sternfigur. 
Definiere dazu die rekursive Funktion star(s), 
welche die Turtle einen  Stern mit der "Dimension" s zeichnen lässt 
(s ist die Distanz vom Zentrum der Sternfigur zum Zentrum in der nächsten Generation). 
s wird von Generation zu Generation auf 1/3 reduziert. 
Rufe stern(180) auf und verankere die Rekursion, dass sie bei s < 20 abbricht. 
Wenn du hideTurtle() verwendest, wird die Turtle viel schneller zeichnen."""


from gturtle import*


def star(s):
    if s<20:
        return
    repeat 6:
        fd(s)
        star(s/3)
        back(s)
        lt(60)
    

makeTurtle()
ht()
star(180)
