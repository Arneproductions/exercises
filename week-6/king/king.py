# This is the solution for the king of the north problem
from collections import defaultdict
from itertools import product
from flow import flow

graph = defaultdict(lambda: defaultdict(int))
# vertex -> (vertex -> capacity), by default capacity is 0

# vertices are (row,col,0/1) where 0 is out and 1 is in, so the original edge is from 0 to 1
R,C = map(int,input().split())
inp = [[0]*C for _ in range(R)] # ] *R #
maxcapacity = 0
for row in range(R):
    for col,capacity in enumerate(map(int,input().split())):
        maxcapacity += capacity
        graph[(row,col,0)][(row,col,1)] = capacity
        inp[row][col] = capacity

# all edges have infinite capacity, so parallel is irrelevant (and impossible with our graph)
for row,col in product(range(R),range(C)):
    this = (row,col,0)
    for rn,cn in product([-1,0,1],[-1,0,1]): # these are too many, but hey
        if abs(rn)+abs(cn) == 1:
            src = (row+rn,col+cn,1)
            if min(src)<0 or src[0]>=R or src[1]>=C: # beyond the boundary
                src = (-1,-1,-1)
            graph[src][this] = maxcapacity
            # print(src,this, maxcapacity)
r,c = map(int,input().split())
flowvalue,fg,cut=flow(graph,(-1,-1,-1),(r,c,1))
# print(cut)
# for row in range(R):
#     for col in range(C):
#         if (row,col,0) in cut and (row,col,1) not in cut and inp[row][col] >0 :
#             print( row,col, inp[row][col])
print(flowvalue)