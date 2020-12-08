from gturtle import*

def square(zeichner):
    repeat 4:
        zeichner.fd(50)
        zeichner.rt(90)
    zeichner.penUp()
    zeichner.fd(60)
    zeichner.penDown()
        
def fullen(fuller):
    fuller.setFillColor("green")
    x=fuller.getX()
    y=fuller.getY()
    fuller.fill(x,y)
    fuller.setPos(x,y+60)
        
tf = TurtleFrame()

maya = Turtle(tf, "sprites/beetle.gif")
pepe = Turtle(tf, "sprites/cuteturtle.gif")
fuller = pepe
zeichner = maya
fuller.setPos(10,10)

repeat 5:
    square(zeichner)
    fullen(fuller)