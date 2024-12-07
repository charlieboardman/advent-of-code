'''
We are adding an obstacle, so it will go somewhere that the guard would have walked--ie on the path from part a
So you only need to check the spots on the path from part a. Guaranteed the obstacles will go there

So the process is:

For each spot on the path:
Create a new temporary labmap with origin at your spot on the path
Check if the spot in front of the guard has already been visited this run. If so, you can't put an obstacle there
Place an obstacle on the temporary map in front of the guard
Propagate the guard, always checking to see if you are back in your starting location and direction.
If you ever do end up back in your starting location and direction on the temporary map, you have found a loop

'''
labmap = [line.strip('\n') for line in open('testinput')]

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

og_path = []

while 0 <= i < len(labmap) and 0 <= j < len(labmap[0]):
    og_path.append((i,j,d))
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
        if j == len(labmap[0])-1:
            continue
        if labmap[i][j+1] == '#':
            d = 'v'
            continue
        else:
            j = j+1
    if d == 'v':
        if i == len(labmap)-1:
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


def traverse_path(labmap,origin):
    visited = [[0 for x in y] for y in labmap]
    path = []
    [i,j,d] = [x for x in origin]
    while 0 <= i < len(labmap) and 0 <= j < len(labmap[0]):
        if (i,j,d) in path:
            return {'result':'loop','path':path,'visited':visited}
        path.append((i,j,d))
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
            if labmap[i][j+1] == '#':
                d = 'v'
                continue
            else:
                j = j+1
        if d == 'v':
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
    
    path.append((i,j,d))
    visited[i][j] = 1
    return {'result':'no loop','path':path,'visited':visited}


total = sum([sum(row) for row in visited])
    
possible_locations_count = 0
for step in range(len(og_path)):
    if step == 0 or step == len(og_path)-1: #We can't put the obstacle at the start and we can't go out of bounds at the end
        continue
    if og_path[step+1][0:2] in [x[0:2] for x in og_path[0:step]]: #Can't put an obstacle somewhere we have already been
        continue
    temp_map = [[x for x in y] for y in labmap] #Create the temporary map where we will put the obstacle
    temp_map[i][j] = '#' #Place the obstacle
    results = traverse_path(temp_map,og_path[step])
    if results['result'] == 'loop':
        possible_locations_count += 1
        
print(possible_locations_count)