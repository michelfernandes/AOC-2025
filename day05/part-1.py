
parts = open("input.txt").read().strip().split("\n\n")

ranges = parts[0].split("\n")
ids = parts[1].split("\n")

count = 0

for id in ids:
    for range in ranges:
        r1, r2 = range.split("-")
        if (int(id) >= int(r1)) and (int(id) <= int(r2)):
            count += 1
            break


print(count)        
        
    
    


