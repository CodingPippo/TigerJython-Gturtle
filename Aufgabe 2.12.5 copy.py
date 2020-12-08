from gturtle import *
import time

makeTurtle()
ht()
penUp()
wrap()
enableRepaint(False)

left(90)
i = 0
while True:
    startTime = time.time()
    clear("white")
    drawImage("sprites/pony_" + str(i) + ".gif")
    repaint()
    fd(10)
    i += 1
    if i == 5:
        i = 0
    while (time.time() - startTime)  < 0.1:
        delay(1)    