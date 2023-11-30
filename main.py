"""
https://docs.python.org/3/library/turtle.html
"""

# Import libraries turtle for drawing and sys for sys.path.append
import turtle
import sys

# Change the path to look for modules and import the library
sys.path.append('./interpreter')
from GraphicalBF import myfunctions as gbf

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Begin!
t = turtle.Turtle()

# Call gbfExec from the gbf module to execute the program
# with argument program, input as a string, each
# character is one input
gbf.gbfExec("+++[>+++++<-]>.*", "4")

# Not important code
for c in ['red', 'green', 'blue', 'yellow']:
  t.color(c)
  t.forward(75)
  t.left(90)
