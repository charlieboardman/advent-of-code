from functools import cache
from copy import deepcopy
import numpy as np

plantmap = np.array([[plant for plant in row.strip('\n')] for row in open('testinput')])

regions = [[None for x in row] for row in plantmap]
visited = [[False for x in row] for row in plantmap]

region_id = -1

i_max = len(plantmap)
j_max = len(plantmap[0])

@cache
def lookup_plant(i,j):
    return plantmap[i][j]

for i,row in enumerate(plantmap):
    for j,plant in enumerate(row):
        if regions[i][j] == None: #If we have hit a new region
            region_id += 1
            print(region_id)
            front_range = [(i,j)]
            while front_range:
                next_front_range = []
                for i,j in front_range:
                    regions[i][j] = region_id
                    if 0<=i-1 and regions[i-1][j]==None and lookup_plant(i-1,j)==lookup_plant(i,j):
                        next_front_range.append((i-1,j))
                    if i+1<i_max and regions[i+1][j]==None and lookup_plant(i+1,j)==lookup_plant(i,j):
                        next_front_range.append((i+1,j))
                    if 0<=j-1 and regions[i][j-1]==None and lookup_plant(i,j-1)==lookup_plant(i,j):
                        next_front_range.append((i,j-1))
                    if j+1<j_max and regions[i][j+1]==None and lookup_plant(i,j+1)==lookup_plant(i,j):
                        next_front_range.append((i,j+1))
                front_range = deepcopy(next_front_range)
        
                