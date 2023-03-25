from sys import stdin

n, k = map(int, next(stdin).split())

nums = [0] * (n+1)

def sum(index) :
	s = 0
	while index >= 1: 
		s += nums[index]
		index -= index&-index # index &- index finds the largest power of two that divides index.
                
	return s

def add(index, flip):
	while index <= n:
		nums[index] += flip;
		index += index&-index;

# Read queries
for i in range(k):
    command = next(stdin).split()
    
    if command[0] == "F":
        index = int(command[1])
        if sum(index) - sum(index-1) == 0:
            add(index, 1)
        else:
            add(index, -1)

    elif command[0] == "C":
        startIndex = int(command[1])
        endIndex = int(command[2])
        res = sum(endIndex) - sum(startIndex-1)
        print(res)