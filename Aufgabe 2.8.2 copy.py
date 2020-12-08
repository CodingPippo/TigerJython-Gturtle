"""Wie du sicher gemerkt hast, beträgt die Drehung an der Spitze bei einem 5-er Stern 144°. 
Verändere diesen Drehwinkel ganz wenig, z. B. 143° und vergrössere die Anzahl der Wiederholungen. 
Dann erhältst du eine neue Figur."""

from gturtle import *

def figur():
    repeat 5:
        fd(200)
        rt(143)
        
makeTurtle()
ht()
repeat 10:
    figur()