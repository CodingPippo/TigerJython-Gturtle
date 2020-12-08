"""FigA ist eine last line recursion, da sie erst in der letzten zeile wieder aufgerufen wird. 
FigB ist eine first line recursion, da sie schon auf der ersten zeile aufgerufen wird. 
zudem fängt FigA innen an und ist spiegelverkehrt zu FigB"""


from gturtle import *

def  figA(s):
   if s > 200:
      return
   forward(s)
   right(90)
   figA(s + 10)

makeTurtle()
figA(100)



from gturtle import *

def  figB(s):
   if s > 200:
      return
   figB(s + 10)
   forward(s)
   right(90)

makeTurtle()
figB(100)