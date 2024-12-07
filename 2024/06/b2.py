labmap = [line.strip('\n') for line in open('input')]

#Find start
def find_origin(labmap):
    for i in range(len(labmap)):
        for j in range(len(labmap[0])):
            if labmap[i][j] in '<>^v':
                return (i,j,labmap[i][j])

origin = find_origin(labmap)

def traverse_map(labmap,origin):
    #Build empty map, preallocating zeros
    path = []
    visited = [[0 for x in y] for y in labmap]
    [i,j,d] = [x for x in origin]
    while 0 <= i < len(labmap) and 0 <= j < len(labmap[0]):
        if (i,j,d) in path:
            return 'loop',path,visited
        path.append((i,j,d))
        visited[i][j] = 1
        #Look ahead
        if d == '^':
            if i == 0:
                break
            if labmap[i-1][j] == '#':
                d = '>'
                continue
            else:
                i = i-1
                continue
        elif d == '>':
            if j+1 == len(labmap[0]):
                j += 1
                continue
            if labmap[i][j+1] == '#':
                d = 'v'
                continue
            else:
                j = j+1
        elif d == 'v':
            if i+1 == len(labmap):
                i += 1
                continue
            if labmap[i+1][j] == '#':
                d = '<'
                continue
            else:
                i = i+1
        elif d == '<':
            if j == 0:
                break
            if labmap[i][j-1] == '#':
                d = '^'
                continue
            else:
                j = j-1
    return 'no loop',path,visited

result, og_path, visited = traverse_map(labmap,origin)

total = sum([sum(row) for row in visited])
#total is the answer to part a. Now start placing obstacles

blocking_locations = []

forbidden_locations = [(og_path[0][0],og_path[0][1])] #Guard starting location

for n,step in enumerate(og_path):
    i = step[0]
    j = step[1]
    if (i,j) in forbidden_locations: #Skip guard's starting location
        continue
    tempmap = [[x for x in y] for y in labmap]
    tempmap[i][j] = '#' #An obstacle will only go on a spot that was on the original path
    obstacle_coords = (i,j)
    test_result, test_path, test_visited = traverse_map(tempmap, origin)
    print(f'{n+1}/{len(og_path)}')
    #print(f'coords: {(i,j)}, result: {test_result}, step: {n}')
    if test_result == 'loop' and (i,j) not in blocking_locations:
        blocking_locations.append((i,j))
        

print(len(blocking_locations))
