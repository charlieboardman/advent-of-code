import numpy as np

grid = [[c for c in line.strip('\n')] for line in open('input')]
grid_array = np.array(grid) #For debugging, visibility of grid structure

count = 0

for row in range(len(grid)):
    if row == 0 or row == len(grid)-1:
        continue #This won't work on the outside rows
    for col in range(len(grid[0])):
        if col == 0 or col == len(grid[0])-1:
            continue
        if grid[row][col] != 'A':
            continue #We can only start on an A
        else:
            if set([grid[row][col],grid[row+1][col+1],grid[row-1][col-1]]) == set([grid[row][col],grid[row-1][col+1],grid[row+1][col-1]]) == set('MAS'):
                count += 1
                
print(count)
