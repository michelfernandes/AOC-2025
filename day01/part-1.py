
lines = open("input.txt").read().splitlines()

dial = 50
count = 0

for line in lines:
    direction = line[0]
    rotation = int(line[1:])

    if  direction == "L":
        dial -= rotation
        while dial < 0:
            dial += 100

    
    if direction == "R":
        dial += rotation
        while dial > 99:
            dial -= 100


    if dial == 0:
        count += 1

print(count)
