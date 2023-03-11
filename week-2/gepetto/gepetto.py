import sys

n, m = map(int, sys.stdin.readline().split())
nogo = set()

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    nogo.add((a, b))
    nogo.add((b, a))

def get_pizzas(subset, i):
    if i == n:
        return 1

    pizzas = 0
    pizzas += get_pizzas(subset, i+1)
    
    for s in subset:
        if (s, i) in nogo:
            return pizzas
    
    subset.append(i) 
    pizzas += get_pizzas(subset, i+1)
    subset.pop()

    return pizzas

print(get_pizzas([], 0))