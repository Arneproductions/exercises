N = int(input())

journeys = {}

for _ in range(N):
    country, year = input().split()
    year = int(year)
    if country not in journeys:
        journeys[country] = []
    journeys[country].append(year)

for country in journeys:
    journeys[country].sort()

Q = int(input())

for _ in range(Q):
    country, i = input().split()
    i = int(i)
    print(journeys[country][i - 1])