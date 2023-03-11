from sys import stdin
import math

# n is the number of nodes in the graph, m is the number of edges, s is the source, t is the sink
n, m, s, t = map(int, next(stdin).split())


# read the m lines containing information about the edges and their capacity
for _ in range(m):

    u, v, c = map(int, next(stdin).split())

# Calculates the delta for the scaling algorithm
def get_delta(max):
    a = int(math.log2(max))
    res = 2**a
    if res > max:
        return 2**(a-1)

    return res

# Performs that algorithm called "The Scaling" in order to find the maximum flow
def flow(graph, source, sink maxNodeCap, maximumCap):
    delta = get_delta(maxNodeCap)

def add_next_nodes(stack, nodes):
    

def find_path(graph, source, sink, delta):

    path = []
    isPathFound = False
    next_node_stack = []

    graph[source]









