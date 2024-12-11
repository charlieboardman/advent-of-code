from copy import deepcopy

trailmap = [[int(c) if c.isnumeric() else '.' for c in row.strip('\n')] for row in open('input')]

trails_to_point = dict()

for i,row in enumerate(trailmap):
    for j,n in enumerate(row):
        if n == 9: #9s are trailheads
            trails_to_point[(i,j)] = 1
        else:
            trails_to_point[(i,j)] = 0

level_search = 8
i_max = len(trailmap)-1
j_max = len(trailmap[0])-1

while level_search >= 0:
    for i,row in enumerate(trailmap):
        for j,n in enumerate(row):
            if n == level_search:
                i_up, i_down = i-1,i+1
                j_right, j_left = j+1,j-1
                
                #Search up
                if i_up >= 0 and trailmap[i_up][j] == level_search + 1:
                        trails_to_point[(i,j)] += trails_to_point[(i_up,j)]

                #Search down
                if i_down <= i_max and trailmap[i_down][j] == level_search + 1:
                    trails_to_point[(i,j)] += trails_to_point[(i_down,j)]
                    
                #Search right
                if j_right <= j_max and trailmap[i][j_right] == level_search + 1:
                    trails_to_point[(i,j)] += trails_to_point[(i,j_right)]
                
                #Search left
                if j_left >= 0 and trailmap[i][j_left] == level_search + 1:
                    trails_to_point[(i,j)] += trails_to_point[(i,j_left)]
                    
    level_search -= 1
    
ratings = []
for point in trails_to_point.keys():
    if trailmap[point[0]][point[1]] == 0:
        ratings.append(trails_to_point[point])

print(sum(ratings))
    