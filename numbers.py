import sys
import re

var1, var2 = sys.argv[1], int(sys.argv[2])

def zeroPad(string, numToFill):
  #replaced = string
  split = re.findall(r'\d+', string)

  print(split, "split")

  if len(split):

    for element in split:
      element2 = element.zfill(numToFill)
      print(element2, "element2")
      replaced = string.replace(element, element2)
      print(replaced)
  else:
    print(string)


zeroPad(var1, var2)
