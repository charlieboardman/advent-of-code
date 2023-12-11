import numpy as np

with open('input.txt','r') as pipe_map:
    array = pipe_map.readlines()

#Find the starting point
def find_start(array):
    for n,row in enumerate(array):
        if 'S' in row:
            for col in range(len(row)):
                if row[col] == 'S':
                    return n,col
                
#Initialize the array of distances
dists = []
for i in range(len(array)):
    dists.append(list(np.zeros(len(array[0]))))

#Right, above, left, below
connects_to_center = [['-','J','7'],['|','7','F'],['-','L','F'],['|','L','J']]

row,col = find_start(array)

def find_adj(row,col):
    if row != 0:
        above = array[row-1][col]
    else:
        above = ''
    
    if row != len(array)-1:
        below = array[row+1][col]
    else:
        below = ''
        
    if col != len(array[row])-1:
        right = array[row][col+1]
    else:
        right = ''
        
    if col != 0:
        left = array[row][col-1]
    else:
        left = ''
        
    return [right,above,left,below]

def are_connectors(adj):
    ans = []
    for n in range(len(adj)):
        ans.append(adj[n] in connects_to_center[n])
    return ans

def determine_coming(row,col,prev_row,prev_col):
    if prev_col == col+1:
        return 0
    if prev_row == row-1:
        return 1
    if prev_col == col-1:
        return 2
    if prev_row == row+1:
        return 3

def router(tile,coming):
    if tile == '|':
        if coming == 1:
            return 3
        else:
            return 1
        
    if tile == '-':
        if coming == 2:
            return 0
        else:
            return 2
        
    if tile == '7':
        if coming == 2:
            return 3
        else:
            return 2
        
    if tile == 'F':
        if coming == 0:
            return 3
        else:
            return 0
        
    if tile == 'L':
        if coming == 1:
            return 0
        else:
            return 1
        
    if tile == 'J':
        if coming == 1:
            return 2
        else:
            return 1

#Process the first tile outside the loop since we have to arbitrarily find coming and going

distance = 0

#Process the current tile
dists[row][col] = distance

#We have to choose a direction to start. Arbitrarily pick that we are coming from the first True and going to the 2nd True in connectors
connectors = are_connectors(find_adj(row,col))
coming = [i for i,n in enumerate(connectors) if n == True][0]
going = [i for i,n in enumerate(connectors) if n == True][1]

prev_row = row
prev_col = col

if going == 0:
    col = col+1
    
if going == 1:
    row = row-1

if going == 2:
    col = col-1

if going == 3:
    row = row+1 

tile = array[row][col]
distance += 1

while dists[row][col] == 0:
    
    #print(tile)
    if distance == 23:
        pass
    
    dists[row][col] = distance

    coming = determine_coming(row,col,prev_row,prev_col)
    going = router(tile,coming)
    
    connectors = are_connectors(find_adj(row,col))

    prev_row = row
    prev_col = col

    if going == 0:
        col = col+1
    
    if going == 1:
        row = row-1
    
    if going == 2:
        col = col-1
    
    if going == 3:
        row = row+1
    
    tile = array[row][col]

    distance += 1


print(dists[row][col]//2)