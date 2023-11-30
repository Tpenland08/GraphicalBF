
import logging


def gbfExec(prgm: str, input: str):
  stack = [0] * 30000
  stackPtr = 0
  for prgmPtr in range(len(prgm)):
    match prgm[prgmPtr]:
      case ">":
         stackPtr += 1
      case "<":
         stackPtr -= 1
      case "+":
         stack[stackPtr] += 1
      case "-":
        stack[stackPtr] -= 1
      case "[":
        if stack[stackPtr] == 0:
          prgmPtr = prgm.index("]", prgmPtr)
      case "]":
         prgmPtr = prgm.index("[", 0)
      case ".":
         print(stack[stackPtr])
      case ",":
         pass
      case "*":
         gbfPush()
      case _:
        logging.info("invalid charater found")
    prgmPtr += 1
  return(0)

def gbfDegraphic(prgm):
  return("Hello World")

def gbfPush():
  return("Hello World")

def gbfCheckInput():
  return("Hello World")

def testfunc3():
  return("Hello World")
  