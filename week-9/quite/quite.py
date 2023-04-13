from sys import stdin

for line in stdin:
    if "PROBLEM" in line.upper():
        print("yes")
    else:
        print("no")