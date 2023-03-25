import string
from sys import stdin

inps = next(stdin).split()
n = int(inps[0]) + 1

numbers = [i for i in range((2**n)-1, 0, -1)]


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
    print(numbers[index])
else:
    print(numbers[0])