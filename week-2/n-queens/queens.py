#
# This solution is for the Holey N-Queens Problem.
# https://itu.kattis.com/courses/BAPS/APS23/assignments/tnubpc/problems/holeynqueensbatman
#
import sys

# Determines if the position can be attacked by another placed queen
def can_be_attacked(x, y):
    return(columns[x] or diag1[x+y] or diag2[x-y+size-1])

# Checks if there is a hole or if another queen can attack that position
def can_place_queen(x, y):
    return not((x,y) in holes) and not(can_be_attacked(x, y))

def place_queen(x, y):
    columns[x] = diag1[x+y] = diag2[x-y+size-1] = True

def remove_queen(x, y):
    columns[x] = diag1[x+y] = diag2[x-y+size-1] = False
    
def place_next(row):
    if row == size:
        return 1
    
    count = 0
    for column in range(size):
        if not(can_place_queen(column, row)):
            continue

        place_queen(column, row)
        count += place_next(row+1)
        remove_queen(column, row)

    return count

results = []
size = 0
rules = 0
size, rules = map(int, sys.stdin.readline().split())

while not(size == 0 and rules == 0):
    holes = set() # Contains tuples of all holes
    columns = [False] * (size) # List of all cells with a bool value indicating if the cell has queen placed 
    diag1 = [False] * ((size - 1) + size)
    diag2 = [False] * ((size - 1) + size)

    for i in range(rules):
        x, y = map(int, sys.stdin.readline().split())
        holes.add((x,y))

    results.append(place_next(0))
    size, rules = map(int, sys.stdin.readline().split())

for result in results:
    print(result)