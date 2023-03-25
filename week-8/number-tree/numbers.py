import string
from sys import stdin

inps = next(stdin).split()
h = int(inps[0]) + 1
n = (2**h)-1

def calc_index(command: string):
    index = 1
    for c in command:
        if c == "L":
            index = index*2
        else:
            index = (index*2)+1

    return index - 1

if len(inps) > 1:
    index = calc_index(inps[1])
    print(n-index)
else:
    print(n)