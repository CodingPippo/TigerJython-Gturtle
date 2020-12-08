from gturtle import *

def bogen():
    repeat 30: 
        forward(5) 
        right(3) 
        
def blumenblatt():
    repeat 2: 
        bogen()
        right(90)
        

makeTurtle()
speed(-1)
blumenblatt()