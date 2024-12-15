from collections import Counter
from functools import cache
from copy import deepcopy
import numpy as np

plantmap = [[plant for plant in row.strip('\n')] for row in open('testinput')]

regions = [[None for x in row] for row in plantmap]
visited = [[False for x in row] for row in plantmap]

region_id = -1

i_max = len(plantmap)
j_max = len(plantmap[0])

@cache
def lookup_plant(i,j):
    return plantmap[i][j]

#@cache #Only start using this after regions have been assigned
def lookup_region(i,j):
    return regions[i][j]

#Assign regions
checked = []
for i_prime,row in enumerate(plantmap):
    for j_prime,plant in enumerate(row):
        if regions[i_prime][j_prime] == None: #If we have hit a new region
            region_id += 1
            print(f'ID {region_id}')
            front_range = [(i_prime,j_prime)]
            while front_range:
                next_front_range = []
                for i,j in front_range:
                    regions[i][j] = region_id
                    checked.append((i,j))
                    if 0<=i-1 and (i-1,j) not in checked and lookup_plant(i-1,j)==lookup_plant(i,j):
                        if (i+1,j) not in next_front_range:
                            next_front_range.append((i-1,j))
                    if i+1<i_max and (i+1,j) not in checked and lookup_plant(i+1,j)==lookup_plant(i,j):
                        if (i+1,j) not in next_front_range:
                            next_front_range.append((i+1,j))
                    if 0<=j-1 and (i,j-1) not in checked and lookup_plant(i,j-1)==lookup_plant(i,j):
                        if (i,j-1) not in next_front_range:
                            next_front_range.append((i,j-1))
                    if j+1<j_max and (i,j+1) not in checked and lookup_plant(i,j+1)==lookup_plant(i,j):
                        if (i,j+1) not in next_front_range:
                            next_front_range.append((i,j+1))
                front_range = deepcopy(next_front_range)
                
#Get area of each region
areas = Counter()
for row in regions:
    for id_ in row:
        areas[id_] += 1
        
#Get perimeters of each region
perimeters = Counter()
for i,row in enumerate(regions):
    for j,id_ in enumerate(row):
        adjacents = 0
        tests = [0<=i-1 and lookup_region(i-1,j)==lookup_region(i,j),\
                 i+1<i_max and lookup_region(i+1,j)==lookup_region(i,j),\
                 0<=j-1 and lookup_region(i,j-1)==lookup_region(i,j),\
                 j+1<j_max and lookup_region(i,j+1)==lookup_region(i,j)]
        for test in tests:
            adjacents += test
        perimeters[id_] += (4-adjacents)
        
total_price = 0
for key in list(areas.keys()):
    total_price += areas[key]*perimeters[key]
    
print(f'Price: {total_price}')
    