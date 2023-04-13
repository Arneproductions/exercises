
doors = ['A', 'B', 'C']

for i in range(1000):
    index = i % 3
    choice = doors[index]
    choicesLeft = set(doors)

    choicesLeft.remove(choice)
    print(choice)

    door, bottle = input().split()
    hasBottle = bottle == '1'
    
    if hasBottle:
        print(door)
    else:
        choicesLeft.remove(door)
        print(choicesLeft.pop())

    rightAnswer = input() 
    
exit()