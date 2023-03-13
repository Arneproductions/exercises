# Performs the scaling algorithm described very shortly in the book
# https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
from sys import stdin
from collections import defaultdict 
from flow import flow

graph = defaultdict(lambda: defaultdict(int))

# n is the number of nodes in the graph, m is the number of edges, s is the source, t is the sink
n, m, s, t = map(int, next(stdin).split())

# read the m lines containing information about the edges and their capacity
for _ in range(m):
    u, v, c = map(int, next(stdin).split())
    graph[u][v] = c

max_flow, edges, cut = flow(graph, s, t)

print(n, max_flow, len(edges))
for u,v,c in edges:
    print(u, v, c)