# This solution is from our lecture, where we tried to solve this together

t = int(input())

def solve(coins, target):
    solutions = {0: 0}
    limit = target + max(coins)
    for coin in coins:
        for price, amount_coins in list(solutions.items()):
            new_price = price + coin
            new_amount = amount_coins + 1
            if new_price > limit:
                continue
            if new_price not in solutions or solutions[new_price] > new_amount:
                solutions[new_price] = new_amount
    return solutions

for _ in range(t):
    target = int(input())
    n = int(input())
    coins = []
    for _ in range(n):
        coins.append(int(input()))

    solutions = solve(coins, target)
    for price in range(target, target + max(coins)):
        if price in solutions:
            print(price, solutions[price])
            break