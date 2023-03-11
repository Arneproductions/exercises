from collections import defaultdict

n = int(input())
needed_for = defaultdict(list)
for _ in range(n):
    target,r = input().split(':')
    for ingredient in r.split(' ')[1:]:
        needed_for[ingredient].append(target)
# print(needed_for)
explore=[(input(),True)]
explored = set()
output = []
while(explore):
    item,fresh = explore.pop()
    if fresh:
        if item not in explored:
            explore.append((item,False))
            explored.add(item)
            for dep in needed_for[item]:
                explore.append((dep,True))
    else:
        output.append(item)

print("\n".join(output[::-1]))