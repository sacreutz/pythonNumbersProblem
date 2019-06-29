import sys
import re

var1, var2 = sys.argv[1], int(sys.argv[2])

def zero_pad(string, num_to_fill):
  split = re.findall(r'\d+', string)

  if len(split):

    for element in split:
      element2 = element.zfill(num_to_fill)
    string = string.replace(element, element2)
    print(string)
  else:
    print(string)


zero_pad(var1, var2)
