import sys

nGames = int(input())

def solve():
    return 0

for _ in range(nGames):
    
    board = [False] * 12
    for idx, c in enumerate(input()):
        if c == 'o':
            board[idx] = True
            
