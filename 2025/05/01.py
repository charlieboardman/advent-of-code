with open('input.txt') as f:
    lines = f.read().splitlines()

fresh_ranges = []
ingredients = []

for line in lines:
    if '-' in line: #add ranges
        [start,stop] = [int(x) for x in line.split('-')]
        fresh_ranges.append(range(start,stop+1))
        
    if '-' not in line and line != '': #add nums
        ingredients.append(int(line))

total = 0
for ingredient in ingredients:
    for r in fresh_ranges:
        if ingredient in r:
            total += 1
            break
        
print(total)