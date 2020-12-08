"""Du wirst einen Baum zeichnen, der schon fast wie ein echter Baum aussieht. 
Definiere dazu die rekursive Funktion treeFractal(s), mit der "Stammlänge" s,  die wie folgt aufgebaut ist:

Verankere die Rekursion bei einer Stammlänge kleiner als 5.

Speichere dir zuerst mit getX() und getY() die aktuelle x- und y-Koordinaten der Turtle, 
sowie mit heading() ihre Blickrichtung, damit du einfach zurückkehren kannst

Jetzt fährst du um s/3 nach vorne, drehst dich um 30 Grad nach links 
und zeichnest den Baum mit der Stammlänge 2*s/3

Du drehst dich um 30 Grad nach rechts, fährst s/6 nach vorn, drehst 25 Grad nach rechts 
und zeichnest den Baum mit der Stammlänge s/2

Du drehst dich um weitere 25 Grad nach rechts, fährst um s/3 nach vorn, 
drehst um 25 Grad nach rechts und zeichnest den Baum noch einmal mit der Stammlänge s/2

Du kehrst mit setPos() und heading()  wieder in die Anfangslage mit der Anfangsposition zurück"""

from gturtle import*
def treeFractal(s):
    if s<2:
        return
    x=getX()
    y=getY()
    h=heading()
    fd(s/3)
    left(30)
    treeFractal(2*s/3)
    right(60)
    fd(s/6)
    right(25)
    treeFractal(s/2)
    right(25)
    fd(s/3)
    rt(25)
    treeFractal(s/2)
    setPos(x,y)
    heading(h)
    
makeTurtle()
ht()
treeFractal(200)

