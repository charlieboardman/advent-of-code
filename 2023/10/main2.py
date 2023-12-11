import numpy as np

with open('input.txt','r') as pipe_map:
    array = pipe_map.readlines()
    array = [list(x.strip('\n')) for x in array]

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
    dists.append([])
    for j in range(len(array[0])):
        dists[i].append(0)
    
#Initialize the array of locations of pipes that comprise the loop
loop = []
for i in range(len(array)):
    loop.append([])
    for j in range(len(array[0])):
        loop[i].append(0)
    
#Initialize the array of locations that are within the loop
inside = []
for i in range(len(array)):
    inside.append([])
    for j in range(len(array[0])):
        inside[i].append(0)

#Right, above, left, below
connects_to_center = [['-','J','7'],['|','7','F'],['-','L','F'],['|','L','J']]

start_row,start_col = find_start(array)

row = start_row
col = start_col

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
loop[row][col] = 1

#We have to choose a direction to start. Arbitrarily pick that we are coming from the first True and going to the 2nd True in connectors
connectors = are_connectors(find_adj(row,col))
coming = [i for i,n in enumerate(connectors) if n == True][0]
going = [i for i,n in enumerate(connectors) if n == True][1]

#Replace the S character at the start with the appropriate character. We have to do this for p2 to work
if set([coming,going]) == set([0,2]):
    array[row][col] = '-'
    
if set([coming,going]) == set([0,1]):
    array[row][col] = 'L'

if set([coming,going]) == set([1,3]):
    array[row][col] = '|'
    
if set([coming,going]) == set([1,2]):
    array[row][col] = 'J'
    
if set([coming,going]) == set([2,3]):
    array[row][col] = '7'
    
if set([coming,going]) == set([0,3]):
    array[row][col] = 'F'

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
    
    dists[row][col] = distance
    loop[row][col] = 1

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


print(f'Steps: {(dists[prev_row][prev_col])//2}')

#Traverse the loop again, this time shooting a ray out the right-hand side of your cursor that paints inside the loop

def find_painter_vecs(row,col,coming):
    char = array[row][col]
    if char in ['-','|']:
        if char == '-' and coming == 2:
            vecs = [3]
        if char == '-' and coming == 0:
            vecs = [1]
        if char == '|' and coming == 1:
            vecs = [2]
        if char == '|' and coming == 3:
            vecs = [0]
        return vecs
    
    if char in ['F','J','7','L']:
        if char == 'F':
            if coming == 3:
                vecs = []
            else:
                vecs = [1,2]
            return vecs
        
        if char == 'J':
            if coming == 1:
                vecs = []
            else:
                vecs = [0,3]
            return vecs
        
        if char == '7':
            if coming == 2:
                vecs = []
            else:
                vecs = [0,1]
            return vecs
        
        if char == 'L':
            if coming == 0:
                vecs = []
            else:
                vecs = [2,3]
            return vecs           

def paint(row,col,vecs):
    
    start_row = row
    start_col = col
    
    for vec in vecs:
        #Paint rightward
        if vec == 0:
            row = start_row
            col = start_col
            while loop[row][col+1] == 0: #While we are still inside the loop
                inside[row][col+1] = 1
                col += 1
        
        #Paint upward
        if vec == 1:
            row = start_row
            col = start_col
            while loop[row-1][col] == 0: #While we are still inside the loop
                inside[row-1][col] = 1
                row -= 1                

        #Paint leftward
        if vec == 2:
            row = start_row
            col = start_col
            while loop[row][col-1] == 0: #While we are still inside the loop
                inside[row][col-1] = 1
                col -= 1                

        #Paint downward
        if vec == 3:
            row = start_row
            col = start_col
            while loop[row+1][col] == 0: #While we are still inside the loop
                inside[row+1][col] = 1
                row += 1
    

def find_painter_loop_start():
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col] == '|' and loop[row][col] == 1:
                going = 1
                coming = 3              
                return row,col,coming,going
            
start_row,start_col,coming,going = find_painter_loop_start()
row = start_row
col = start_col

vecs = find_painter_vecs(row,col,coming)

if col == 6 and row == 0:
    pass
paint(row,col,vecs)

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


while row != start_row or col != start_col:

    #print(tile)
    if row == 6 and col == 8:
        pass

    coming = determine_coming(row,col,prev_row,prev_col)
    
    going = router(tile,coming)
    
    vecs = find_painter_vecs(row,col,coming)
    
    paint(row,col,vecs)

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
        
print(f'Enclosed: {int(sum([sum(x) for x in inside]))}')
        
