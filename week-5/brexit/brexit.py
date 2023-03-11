from sys import stdin
from collections import deque

# Build graph. C is the amount of countries, P is the number of trading partners, X is the id of the home country, L is the ID of the country leaving
C, P, X, L = map(int, next(stdin).split())

# -1 beacuse we want to use the first index in the array
L = L-1
X = X-1

countries = [set() for _ in range(C)]
good_countries_left = [0] * C
bad_countries = set()
q = deque()

# Add the first bad partner to the set and set visited to true
bad_countries.add(L)

# Add trading partners
for _ in range(P):
    x, y = map(int, next(stdin).split())

    # Add trading partners both directions, because it is a partnership
    c1 = x-1
    c2 = y-1
    good_countries_left[c1] = good_countries_left[c1] + 1
    good_countries_left[c2] = good_countries_left[c2] + 1
    countries[c1].add(c2)
    countries[c2].add(c1)

def is_bad_country(node_id):
    good_countries = good_countries_left[node_id]

    return good_countries <= (len(countries[node_id])/2)


for partner in countries[L]:
    q.append(partner)
    good_countries_left[partner] = good_countries_left[partner] - 1

# Search the graph for "bad" nodes
while q and X not in bad_countries:
    current = q.popleft()

    if current in bad_countries:
        continue

    is_bad = is_bad_country(current)

    if is_bad:
        bad_countries.add(current)

        for partner in countries[current]:
            if partner not in bad_countries:
                good_countries_left[partner] = good_countries_left[partner] - 1 
                q.append(partner)


if X in bad_countries:
    print("leave")
else:
    print("stay")

# NOTE: Remember that we should not do it recursively. Use the Stack(i.e. list in python) datastructure to create your own stack