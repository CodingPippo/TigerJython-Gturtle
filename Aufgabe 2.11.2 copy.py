from gturtle import *

def circle(mami):
    repeat 360:
        mami.fd(2)
        mami.lt(1)
        direction(child)

        
def direction(child):
    child.setHeading(child.towards(mami))
    child.fd(1)

tf=TurtleFrame()

mami = Turtle(tf)
mami.setColor("red")
mami.speed(-1)

child = Turtle(tf)
child.setPos(-200,200)
child.speed(-1)

circle(mami)
direction(child)