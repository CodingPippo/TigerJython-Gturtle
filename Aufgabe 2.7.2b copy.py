from gturtle import *


def stairstep(x):
    forward(x)
    right(90)
    
        
x=10

makeTurtle()
ht()

repeat 100:
    stairstep(x)
    x=x+3
    if x>50:
        setPenColor("red")
    if x>100:
        setPenColor("black")
    if x>200:
        break
    