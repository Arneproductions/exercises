# Performs the scaling algorithm described very shortly in the book
# https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
import sys
from sys import stdin
from collections import defaultdict
import math

graph = defaultdict(lambda: defaultdict(int))
edge_cap_used = dict() 

# Calculates the delta for the scaling algorithm
def get_delta(max):
    a = int(math.log2(max))
    res = 2**a
    if res > max:
        return 2**(a-1)

    return res

# Performs that algorithm called "The Scaling" in order to find the maximum flow
def flow(source, sink, maxNodeCap):
    delta = get_delta(maxNodeCap)
    used_edges = set()
    max_flow = 0

    while delta != 0:
        is_path, path, min_cap = find_path(graph, source, sink, delta)

        if not is_path:
            delta = delta / 2
            continue
        else:
            max_flow += min_cap
            for u, v in path:
                edge = (u, v)
                used_edges.add(edge)
                edge_cap_used[edge] += min_cap # Update how much capacity is used
                graph[u][v] = graph[u][v] - min_cap # Update capacity left for that edge

    return used_edges, max_flow
    
        
# This gives a list sorted by the capacity from low to high
# Returns: a sorted list of tuples where the tuple is (capacity, nodeId)
def get_next_nodes(adj_nodes, delta):
    nodes = []
    for v, c in adj_nodes.items():
        if c >= delta:
            nodes.append((c, v))
    
    return nodes # Sorts by capacity first, if they are equal, then node number

def find_path(graph, source, sink, delta):

    path = []
    is_path_found = False
    next_node_stack = []

    # Start from source
    next_nodes = get_next_nodes(graph[source], delta)
    for _, v in next_nodes:
        next_node_stack.append((source, v))

    # Do DFS through the graph
    while next_node_stack and not is_path_found:
        edge = next_node_stack.pop() 
        current = edge[1]
        path.append(edge)

        # If we reach the source then a path has been found
        if current == sink:
            is_path_found = True
            continue

        next_nodes = get_next_nodes(graph[current], delta)

        if not next_nodes: 
            path.pop() # Since the current cannot continue the path
            continue

        for _, v in next_nodes:
            next_node_stack.append((current, v))

    # Find the min capacity size in the path 
    min_cap = sys.maxsize
    for u,v in path:
        min_cap = min(min_cap, graph[u][v])

    return (is_path_found, path, min_cap)


# n is the number of nodes in the graph, m is the number of edges, s is the source, t is the sink
n, m, s, t = map(int, next(stdin).split())

max_node_cap = 0 

# read the m lines containing information about the edges and their capacity
for _ in range(m):
    u, v, c = map(int, next(stdin).split())
    graph[u][v] = c
    edge_cap_used[(u,v)] = 0
    max_node_cap = max(max_node_cap, c)

used_edges, max_flow = flow(s, t, max_node_cap)

print(n, max_flow, len(used_edges))
for u,v in used_edges:
    print(u, v, edge_cap_used[(u,v)])