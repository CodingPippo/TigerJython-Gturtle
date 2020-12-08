from gturtle import *

x=0

makeTurtle()
ht()
repeat 10:
    if x==5:
        setPenColor("red")
    fd(10)
    rt(90)
    fd(10)
    lt(90)
    x=x+1
    