dishmap = [[c for c in row.strip('\n')] for row in open('input')]

dishes = []
for i,row in enumerate(dishmap):
    for j,c in enumerate(row):
        if c.isalnum():
            dishes.append((i,j,c))
            
for dish in dishes:
    pair_dishes = [x for x in dishes if x != dish and x[2] == dish[2]]
    for pair_dish in pair_dishes:
        vector = (pair_dish[0]-dish[0],pair_dish[1]-dish[1])
        antinode = (pair_dish[0]+vector[0],pair_dish[1]+vector[1])
        i,j = antinode[0],antinode[1]
        if 0 <= i < len(dishmap) and 0 <= j < len(dishmap[0]):
            dishmap[i][j] = '#'
    
print(sum([row.count('#') for row in dishmap]))
        