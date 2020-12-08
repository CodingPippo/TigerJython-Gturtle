from gturtle import *

s = 300
w = 151


def segment(s, w):
   forward(s)
   right(w) 
   
makeTurtle()
hideTurtle()
setPos(-200,-200)
repeat 92:
    segment(s,w)