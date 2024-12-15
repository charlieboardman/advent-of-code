from collections import Counter
from functools import cache
from copy import deepcopy
import numpy as np

plantmap = np.array([[plant for plant in row.strip('\n')] for row in open('input')])
regions = np.array([[None for x in row] for row in plantmap])

i_max = len(plantmap)
j_max = len(plantmap[0])

points_by_region = dict()
total_points_scanned = []

@cache
def get_plant(i,j):
    return plantmap[i][j]

@cache
def get_region(i,j):
    return regions[i][j]

def expand_region(i,j):
    points = []
    new_points = [(i,j)]
    while new_points:
        for point in new_points:
            up
            

region_id = -1
for i,row in enumerate(plantmap):
    for j,plant in enumerate(row):
        if (i,j) not in total_points_scanned:
            region_id += 1
            region_points = expand_region(i,j)
            