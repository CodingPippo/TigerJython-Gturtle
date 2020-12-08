"""Zeichne mit einer Wiederholstruktur den nebenstehenden Stern
und fülle ihn mit Mausklicks nach deinem Geschmack aus."""

from gturtle import*

def star(n):
    repeat 9:
        fd(n)
        rt(160)
    
def onMouseHit(x, y):
    fill(x, y)


makeTurtle(mouseHit = onMouseHit)
ht()
star(200)