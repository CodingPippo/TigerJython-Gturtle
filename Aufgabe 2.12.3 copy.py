from gturtle import*

makeTurtle("sprites/ball.gif")
speed(-1)
setRandomHeading()

while True:
    
    if getX() >= 400 or getX() <= -400:
        setHeading(-heading())
        forward(10)
    if getY() >= 300 or getY() <= -300:
        setHeading(180 - heading())
    fd(10)