from gturtle import *

def star(t):
    repeat 5:
        t.fd(200)
        t.rt(144)
        
tf = TurtleFrame()

maya = Turtle(tf)
maya.setPos(-200,0)
maya.setColor("red")


pepe = Turtle(tf)
pepe.setPos(200,0)
pepe.setColor("green")

igeli = Turtle(tf, "Igeli.gif" )
igeli.setPos(0,0)
       

        
star(maya)
star(pepe)
star(igeli)


