
input = open("input.txt").read().split("\n")

total = 0

for line in input:
    array = [""] * 12
    biggest = line[0]
    indexBiggest = 0
    startIndex = 0
    print(line)
    for counter in range(12):
        for i,number in enumerate(line[startIndex :len(line) - 11+counter], start=startIndex):
            if number > biggest:
                biggest = number
                indexBiggest = i

        array[counter] = biggest
        biggest='0'
        startIndex = indexBiggest + 1

    total += int("".join(array))

print(total)        
        
    
    


