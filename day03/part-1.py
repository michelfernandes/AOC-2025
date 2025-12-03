
input = open("input.txt").read().split("\n")

count = 0

for line in input:
    first = line[0]
    second = line[1]
    for i,number in enumerate(line):
        isLast = i == len(line) - 1
        isFirst = i == 0
        shouldCheckSecond = 1
        if int(number) > int(first) and not isLast:
            first = number
            second = line[i + 1]
            shouldCheckSecond = 0
        
        if int(number) > int(second) and shouldCheckSecond and not isFirst:
            second = number

    biggestOfLine = int(str(first) + str(second))      

    count += biggestOfLine

print(count)        
        
    
    


