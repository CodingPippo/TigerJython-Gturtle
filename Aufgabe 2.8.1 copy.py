"""Die Turtle bewegt sich um eine Strecke 5 vorwärts, dreht sich um 70° nach rechts und 
vergrössert die Streckenlänge um 0.5.
Diese Schritte wiederholt sie, solange die Streckenlänge kleiner als 150 ist.

Versuche es auch mit dem Drehwinkel 89°!"""


from gturtle import*

def figur(x):
    fd(x)
    rt(70)
    
makeTurtle()
ht()
x = 5

while x<150:
    figur(x)
    x+=0.5