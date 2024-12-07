labmap = [line.strip('\n') for line in open('input')]

#Find start
def find_origin(labmap):
    for i in range(len(labmap)):
        for j in range(len(labmap[0])):
            if labmap[i][j] in '<>^v':
                return (i,j,labmap[i][j])

origin = find_origin(labmap)
[i,j,d] = [x for x in origin]

#Build empty map, preallocating zeros
visited = []
for x in range(len(labmap)):
    visited.append([])
    for y in range(len(labmap[0])):
        visited[x].append(0)


while 0 <= i < len(labmap) and 0 <= j < len(labmap[0]):
    visited[i][j] = 1
    #Look ahead
    if d == '^':
        if labmap[i-1][j] == '#':
            d = '>'
            continue
        else:
            i = i-1
            continue
    if d == '>':
        if j+1 == len(labmap[0]):
            continue
        if labmap[i][j+1] == '#':
            d = 'v'
            continue
        else:
            j = j+1
    if d == 'v':
        if i+1 == len(labmap):
            continue
        if labmap[i+1][j] == '#':
            d = '<'
            continue
        else:
            i = i+1
    if d == '<':
        if labmap[i][j-1] == '#':
            d = '^'
            continue
        else:
            j = j-1


total = sum([sum(row) for row in visited])
    
print(total)