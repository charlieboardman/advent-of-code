import numpy as np

grid = [[c for c in line.strip('\n')] for line in open('input')]
grid_array = np.array(grid) #For debugging, visibility of grid structure

count = 0

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] != 'X':
            continue #We can only start on an X
        else:
            try:
                if ''.join([grid[row][col+d] for d in range(4)]) == 'XMAS': #search right
                    count += 1
                    #print(f'XMAS found right: row {row+1}, col {col+1}')
            except IndexError:
                pass
                    
            try:
                if ''.join([grid[row-d][col+d] for d in range(4) if (row-d)>=0]) == 'XMAS': #search up right
                    count += 1
                    #print(f'XMAS found up right: row {row+1}, col {col+1}')
            except IndexError:
                pass
            
            try:
                if ''.join([grid[row-d][col] for d in range(4) if (row-d)>=0]) == 'XMAS': #search up
                    count += 1
                    #print(f'XMAS found up: row {row+1}, col {col+1}')
            except IndexError:
                pass
            
            try:
                if ''.join([grid[row-d][col-d] for d in range(4) if (row-d)>=0 and (col-d)>=0]) == 'XMAS': #search up left
                    count += 1
                    #print(f'XMAS found up left: row {row+1}, col {col+1}')
            except IndexError:
                pass
            
            try:
                if ''.join([grid[row][col-d] for d in range(4) if (col-d)>=0]) == 'XMAS': #search left
                    count += 1
                    #print(f'XMAS found left: row {row+1}, col {col+1}')
            except IndexError:
                pass
                
                
            try:
                if ''.join([grid[row+d][col-d] for d in range(4) if (col-d)>=0]) == 'XMAS': #search down left
                    count += 1
                    #print(f'XMAS found down left: row {row+1}, col {col+1}')
            except IndexError:
                pass
            
            try:
                if ''.join([grid[row+d][col] for d in range(4)]) == 'XMAS': #search down
                    count += 1
                    #print(f'XMAS found down: row {row+1}, col {col+1}')
            except IndexError:
                pass
            
            try:
                if ''.join([grid[row+d][col+d] for d in range(4)]) == 'XMAS': #search down right
                    count += 1
                    #print(f'XMAS found down right: row {row+1}, col {col+1}')
            except IndexError:
                pass
                
print(count)