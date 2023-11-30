"""
https://docs.python.org/3/library/turtle.html
"""
import turtle
import sys

sys.path.append('./interpreter')
from GraphicalBF import myfunctions as gbf

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Begin!
t = turtle.Turtle()

gbf.gbfExec("+++[>+++<-].*", "41")

for c in ['red', 'green', 'blue', 'yellow']:
  t.color(c)
  t.forward(75)
  t.left(90)
