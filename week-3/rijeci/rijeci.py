n = int(input())

a = 1
b = 0

for _ in range(n):
    tempb = a
    a = b
    b += tempb
    
print(a, b)