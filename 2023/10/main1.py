import numpy as np

with open('input.txt','r') as pipe_map:
    array = pipe_map.readlines()

#Find the starting point
def find_start(array):
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col] == 'S':
                return row,col
            
#Initialize the array of distances
dists = []
for i in range(len(array)):
    dists.append(list(np.zeros(len(array[0]))))

#Above, below, right, left
connects = [['|','7','F','S'],['|','L','J','S'],['-','L','F','S'],['-','J','7','S']]

row,col = find_start(array)

def find_adj_connectors(row,col):
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
        
    return [above,below,right,left]

def are_connectors(adj):
    ans = []
    for n in range(len(adj)):
        ans.append(adj[n] in connects[n])
    return ans

next_tile = ''
tile = 'S'

distance = 0

#We have to choose a direction to start. Arbitrarily pick that we are coming from the first True and going to the 2nd True in connectors
connectors = are_connectors(find_adj_connectors(row,col))
coming = [i for i,n in enumerate(connectors) if n == True][0]
going = [i for i,n in enumerate(connectors) if n == True][1]

while next_tile != 'S':
    
    dists[row][col] = distance

    from_row = row
    from_col = col

    if going == 0:
        row = row-1
    
    if going == 1:
        row = row-1
    
    if going == 2:
        col = col+1
    
    if going == 3:
        col = col-1
    
    connectors = are_connectors(find_adj_connectors(row,col)):
        going = [i for i,n in enumerate(connectors) if n == True and    
    
    next_tile = array[row][col]
    
    