
import logging

#Initialize log directory
logging.basicConfig(level = logging.INFO,filename="interpreter/logs/logs.txt")

# The function to execute GraphicalBF programs
def gbfExec(prgm: str, input: str):
  # Set up variables pre-execution
  stack = [0] * 30000
  stackPtr = 0
  prgmPtr = 0
  # Print the program to let the user know what is running
  print(prgm)
  # Loop to read each character and execute each one
  #appropriatelly
  while prgmPtr < len(prgm):
    match prgm[prgmPtr]:
      # Move the pointer one cell to the right
      case ">":
         stackPtr += 1
      # Move the pointer one cell to the left
      case "<":
         stackPtr -= 1
      # Increment the cell value at the pointer by 1
      case "+":
         stack[stackPtr] += 1
      # Decrement the cell value at the pointer by 1
      case "-":
        stack[stackPtr] -= 1
      # Start a loop by checking if the current cell
      #value is 0, and if it is, skipping the loop
      case "[":
        if stack[stackPtr] == 0:
          prgmPtr = prgm.index("]", prgmPtr)
          prgmPtr += 1
      # Ending a loop by checking for a 0 value in the
      # current cell, and if it isn't, going back to the
      # start of the loop
      case "]":
         if stack[stackPtr] != 0:
           prgmPtr = prgm.index("[", 0)
      # Print the value at the current cell
      # (Eventually use C type printing for alphanumeric
      # vs number printing? Also print to screen as
      # turtle text?)
      case ".":
         print(stack[stackPtr])
      case ",":
         pass
      # Draw a frame to the screen (See the gbfPush func.)
      case "*":
         gbfPush()
      case _:
        logging.info(f"invalid charater {prgm[prgmPtr]}")
    prgmPtr += 1
  return(0)

# Useless function, disregard
def gbfDegraphic(prgm):
  return("Hello World")


# Function to draw a frame to the screen based on the contents of various stack cells
def gbfPush():
#  for pixel in range(69):
#    color = bin(pixel)
#    rgbValues = {
#      "red": int(),
#      "green": int(),
#      "blue": int(slice(color, 2, 4))
#    }
    # turtle.color()  
  return(0)

# Don't remember what this function does
def gbfCheckInput():
  return("Hello World")

def testfunc3():
  return("Hello World")
  