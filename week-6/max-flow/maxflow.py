# Performs the scaling algorithm described very shortly in the book
# https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
import sys
from sys import stdin
from collections import defaultdict, deque

graph = defaultdict(lambda: defaultdict(int))
edge_cap_used = dict() 

# Performs that algorithm called "The Scaling" in order to find the maximum flow
def flow(source, sink, node_count):
    used_edges = set()
    max_flow = 0
    while True:
        is_path, path, min_cap = find_path(graph, source, sink, node_count)

        if not is_path:
            break
        else:
            max_flow += min_cap
            parent = sink
            current = path[parent][1]

            while current != -1:
                edge = (current, parent)
                used_edges.add(edge)
                edge_cap_used[edge] += min_cap
                graph[current][parent] -= min_cap

                # get next node
                parent = current
                current = path[parent][1]

    return used_edges, max_flow
    
def find_path(graph, source, sink, node_count):

    path = [(0, -1)] * node_count
    is_path_found = False
    next_node_stack = deque()

    # Start from source
    for v, c in graph[source].items():
        if c > 0:
            path[v] = (c, source)
            next_node_stack.append((source, v))

            if v == sink:
                is_path_found = True

    # Do BFS through the graph
    while next_node_stack and not is_path_found:
        current = next_node_stack.popleft()[1]

        # Get adjacent nodes
        for v, c in graph[current].items():
            if c > 0 and path[v][1] == -1:
                path[v] = (c, current)
                next_node_stack.append((current, v))
            
                if v == sink:
                    is_path_found = True
                    break


    # Find the min capacity size in the path 
    min_cap = sys.maxsize
    cost, current = path[sink]
    while current != -1:
        min_cap = min(min_cap, cost)
        cost, current = path[current]

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

used_edges, max_flow = flow(s, t, n)

print(n, max_flow, len(used_edges))
for u,v in used_edges:
    print(u, v, edge_cap_used[(u,v)])