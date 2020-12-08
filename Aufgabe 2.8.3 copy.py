"""Die Turtle zeichnet ein Diagonalmuster mit gefüllten roten Kreisen. 
Alle Kreise liegen im Turtlefenster, d.h. dass ihre Distanz vom Mittelpunkt kleiner als 400 ist.

Verwende den Befehl dot(25), um die Kreise zu zeichnen."""





from gturtle import*
setPlaygroundSize(500, 500)

def kette():
    right(45)
    getX()
    while getX()<250:
        dot(25)
        fd(50)

def anderekette():
    left(90)
    getX()
    while getX()>-250:
        dot(25)
        fd(50)





makeTurtle()
setPos(-250,-250)
kette()
setPos(250,-250)
anderekette()